#!/usr/bin/env python3
"""
ROB 501: Mathematics for Robotics  --  Anki deck generator.

Card content lives as **plain-text source files** in  source/NN_topic.md  (one
per lecture).  This script PARSES those text files -- nothing is hard-coded
here -- and emits a single deck with one sub-deck per lecture:

    ROB 501::01 Intro & Proofs
    ROB 501::02 Induction, Fundamental Theorem & Contradiction
    ...

Run:   python3 build_deck.py        ->  ROB501_Mathematics_for_Robotics.apkg

Source-file format (see source/README_FORMAT.txt):

    === 03 | Abstract Linear Algebra ===

    [QA]
    Q:
    <question, LaTeX + light HTML, may span several lines>
    A:
    <answer>
    E:
    <optional "why / intuition" note>

    [CLOZE]
    C:
    A {{c1::vector space}} is closed under ...
    E:
    <optional note>

Field markers (Q: A: E: C:) and block markers ([QA] [CLOZE]) each sit alone on
their own line, so colons inside the content never confuse the parser.

Math: write LaTeX with \\( ... \\) inline and \\[ ... \\] display (Anki MathJax).
Use \\lt and \\gt instead of < and > inside math so the HTML parser is happy.

Requires:  pip install genanki
"""

import os
import re
import sys
import glob
import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, "source")
OUT = os.path.join(HERE, "ROB501_Mathematics_for_Robotics.apkg")

# ---- Stable IDs (do NOT change once published) -----------------------------
TOP_DECK_ID = 1996501000
BASIC_MODEL_ID = 1996501101
CLOZE_MODEL_ID = 1996501102
TOP_DECK_NAME = "ROB 501"

CSS = r"""
.card {
  font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 19px; line-height: 1.6; color: #1c2733;
  background: #f4f6f9; text-align: left; padding: 0; margin: 0;
}
.wrap {
  max-width: 720px; margin: 18px auto; background: #ffffff;
  border-radius: 16px; box-shadow: 0 6px 22px rgba(20,40,70,.10); overflow: hidden;
}
.topic {
  background: linear-gradient(135deg, #00274c 0%, #1d4e79 100%);
  color: #ffcb05; font-size: 13px; font-weight: 700; letter-spacing: .06em;
  text-transform: uppercase; padding: 10px 22px;
}
.content { padding: 20px 22px 22px 22px; }
.q { font-weight: 600; }
hr#answer { border: none; border-top: 2px dashed #cdd7e1; margin: 16px 0; }
.extra {
  margin-top: 14px; padding: 12px 14px; background: #eef4fb;
  border-left: 4px solid #1d4e79; border-radius: 8px; font-size: 16px; color: #29485f;
}
.extra .lbl {
  display: block; font-size: 11px; font-weight: 700; letter-spacing: .08em;
  text-transform: uppercase; color: #1d4e79; margin-bottom: 4px;
}
b, strong { color: #00274c; }
code {
  background: #eef1f4; border-radius: 5px; padding: 1px 5px; font-size: .92em;
  font-family: "SF Mono", Menlo, Consolas, monospace;
}
.cloze { font-weight: 700; color: #c0392b; }
ul, ol { margin: 8px 0 8px 4px; padding-left: 22px; }
li { margin: 3px 0; }
.nightMode .card, .night_mode .card { background: #1a1d21; color: #d8dee4; }
.nightMode .wrap, .night_mode .wrap { background: #23272e; box-shadow: none; }
.nightMode .extra, .night_mode .extra { background: #2b323c; color: #c7d2dc; }
.nightMode b, .nightMode strong, .night_mode b, .night_mode strong { color: #ffcb05; }
.nightMode code, .night_mode code { background: #2b323c; }
"""

BASIC_MODEL = genanki.Model(
    BASIC_MODEL_ID, "ROB501 Basic (Q&A)",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Extra"}, {"name": "Topic"}],
    templates=[{
        "name": "Card 1",
        "qfmt": """
<div class="wrap"><div class="topic">{{Topic}}</div>
  <div class="content"><div class="q">{{Front}}</div></div></div>
""",
        "afmt": """
<div class="wrap"><div class="topic">{{Topic}}</div>
  <div class="content"><div class="q">{{Front}}</div>
    <hr id="answer"><div class="back">{{Back}}</div>
    {{#Extra}}<div class="extra"><span class="lbl">Why / Intuition</span>{{Extra}}</div>{{/Extra}}
  </div></div>
""",
    }],
    css=CSS,
)

CLOZE_MODEL = genanki.Model(
    CLOZE_MODEL_ID, "ROB501 Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}, {"name": "Topic"}],
    templates=[{
        "name": "Cloze",
        "qfmt": """
<div class="wrap"><div class="topic">{{Topic}}</div>
  <div class="content">{{cloze:Text}}</div></div>
""",
        "afmt": """
<div class="wrap"><div class="topic">{{Topic}}</div>
  <div class="content">{{cloze:Text}}
    {{#Extra}}<div class="extra"><span class="lbl">Why / Intuition</span>{{Extra}}</div>{{/Extra}}
  </div></div>
""",
    }],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)

TITLE_RE = re.compile(r"^===\s*(\d+)\s*\|\s*(.+?)\s*===\s*$")
FIELD_MARKERS = {"Q:", "A:", "E:", "C:"}


def parse_source(path):
    """Parse one source/NN_topic.md file into {'num','title','cards':[...]}."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    num = title = None
    cards = []
    cur = None          # current card dict
    field = None        # which field we're appending to
    buf = []            # accumulated lines for the current field

    def flush_field():
        nonlocal field, buf
        if cur is not None and field is not None:
            cur[field] = "\n".join(buf).strip()
        field, buf = None, []

    def flush_card():
        nonlocal cur
        flush_field()
        if cur is not None:
            cards.append(cur)
        cur = None

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()

        m = TITLE_RE.match(stripped)
        if m:
            num, title = int(m.group(1)), m.group(2)
            continue
        if stripped in ("[QA]", "[CLOZE]"):
            flush_card()
            cur = {"type": "qa" if stripped == "[QA]" else "cloze"}
            continue
        if cur is not None and stripped in FIELD_MARKERS:
            flush_field()
            field = {"Q:": "front", "A:": "back", "E:": "extra", "C:": "text"}[stripped]
            buf = []
            continue
        if field is not None:
            buf.append(line)
        # lines outside any field (blank lines between blocks) are ignored

    flush_card()

    if num is None:
        raise ValueError(f"{path}: missing '=== NN | Title ===' header")
    return {"num": num, "title": title, "cards": cards}


def build():
    files = sorted(glob.glob(os.path.join(SRC_DIR, "[0-9][0-9]_*.md")))
    if not files:
        print("No source files in", SRC_DIR)
        sys.exit(1)

    decks, total = [], 0
    for path in files:
        lec = parse_source(path)
        num, title = lec["num"], lec["title"]
        topic = f"ROB 501 • L{num:02d} — {title}"
        deck = genanki.Deck(TOP_DECK_ID + num, f"{TOP_DECK_NAME}::{num:02d} {title}")
        for c in lec["cards"]:
            tags = [f"L{num:02d}", "ROB501"]
            if c["type"] == "cloze":
                note = genanki.Note(CLOZE_MODEL,
                                    [c.get("text", ""), c.get("extra", ""), topic], tags=tags)
            else:
                note = genanki.Note(BASIC_MODEL,
                                    [c.get("front", ""), c.get("back", ""), c.get("extra", ""), topic],
                                    tags=tags)
            deck.add_note(note)
            total += 1
        decks.append(deck)
        print(f"  L{num:02d} {title:<50} {len(lec['cards']):>3} cards")

    genanki.Package(decks).write_to_file(OUT)
    print(f"\nWrote {OUT}\nDecks: {len(decks)}   Total cards: {total}")


if __name__ == "__main__":
    build()
