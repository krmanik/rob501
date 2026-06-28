ROB 501 Anki — source file format
==================================

One file per lecture:  NN_topic.md   (NN = 01..26, two digits, sets order).
build_deck.py reads every source/NN_*.md and turns it into one Anki sub-deck.

Header (once, at top of file):

    === 03 | Abstract Linear Algebra ===

        NN  -> lecture number (also the sub-deck order / id offset)
        text after | -> sub-deck title shown in Anki

Cards.  Two kinds of block:

    [QA]              ->  Basic question/answer card
    Q:                ->  question     (LaTeX + light HTML, can span lines)
    <text...>
    A:                ->  answer
    <text...>
    E:                ->  optional "Why / Intuition" note (blue box)
    <text...>

    [CLOZE]           ->  Cloze-deletion card
    C:                ->  text with {{c1::...}} {{c2::...}} blanks
    <text...>
    E:                ->  optional note

Rules
-----
* The markers [QA] [CLOZE] and the field markers Q: A: E: C: each sit ALONE
  on their own line.  Colons inside the content are therefore harmless.
* A field runs from its marker until the next marker / block / EOF.
* Math: \( ... \) inline, \[ ... \] display  (Anki's built-in MathJax).
  Inside math use \lt \gt \leq \geq instead of < > so HTML parsing is safe.
* Light HTML allowed: <b> <i> <ul><li> <ol> <br>.
* Blank lines between blocks are ignored — use them for readability.

Rebuild:  python3 build_deck.py
