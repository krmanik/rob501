# ROB 501 — Anki Deck (Mathematics for Robotics)

A clean, math-rich [Anki](https://apps.ankiweb.net/) deck covering the full
ROB 501 (Fall 2018) lecture sequence — **216 notes** organized into **27
chapter sub-decks**, one per lecture (plus a supplemental factorizations deck).
Every card uses real LaTeX (rendered by Anki's built-in MathJax), a styled
two-tone "Michigan" card template, light/dark-mode support, and a **Why /
Intuition** box on most cards.

> Import file: **`ROB501_Mathematics_for_Robotics.apkg`** — double-click it
> (or *File → Import* in Anki) and the whole `ROB 501::NN Topic` tree appears.

---

## What's inside

Decks are named `ROB 501::01 Intro & Proofs`, `ROB 501::02 …`, etc., so they
nest under a single **ROB 501** parent and stay in lecture order.

| # | Sub-deck | Cards |
|---|----------|------:|
| 01 | Intro & Proofs | 18 |
| 02 | Induction, Fundamental Theorem & Contradiction | 14 |
| 03 | Abstract Linear Algebra | 7 |
| 04 | Subspaces & Linear Independence | 9 |
| 05 | Basis Vectors & Dimension | 9 |
| 06 | Linear Operators & Eigenvalues | 9 |
| 07 | Similar Matrices & Norms | 8 |
| 08 | Inner Product Spaces | 8 |
| 09 | Projection Theorem & Gram-Schmidt | 7 |
| 10 | Normal Equations & Least Squares | 7 |
| 11 | Symmetric & Orthogonal Matrices | 7 |
| 12 | Positive Semi-Definite Matrices & Schur Complement | 8 |
| 13 | Recursive Least Squares & Kalman Filter | 8 |
| 14 | Least Squares & Probability | 7 |
| 15 | Best Linear Unbiased Estimator (BLUE) | 6 |
| 16 | QR Factorization | 5 |
| 17 | Modified Gram-Schmidt & Minimum Variance Estimator | 7 |
| 18 | Probability Space & Random Variables | 8 |
| 19 | Gaussian Random Vectors | 8 |
| 20 | Real Analysis & Normed Spaces | 8 |
| 21 | Real Analysis & Interior of a Set | 7 |
| 22 | Newton-Raphson Algorithm | 7 |
| 23 | Cauchy Sequences | 8 |
| 24 | Continuous Functions | 5 |
| 25 | Weierstrass Theorem | 7 |
| 26 | Final Class & Linear Programming | 7 |
| 27 | Matrix Factorizations — SVD, LU & Cholesky *(supplemental)* | 7 |

Lecture order and titles follow the course plan in the repository
[README](../README.md). Subtitle files carry only the topic **name** (no
number), so names were matched to that plan to recover the ordering.
Deck 27 collects textbook factorization material (SVD / LU / Cholesky) that is
not a separately numbered lecture.

## Two note types

- **ROB501 Basic (Q&A)** — Front / Back / *Extra* (Why-Intuition) / Topic.
- **ROB501 Cloze** — fill-in-the-blank for key formulas and definitions.

## Sources

Content was authored from the course's own materials in this repo:

- **Textbook** — `../Textbook/ROB501_Textbook2022_03_21.pdf` (primary, authoritative).
- **Subtitles** — `../Subtitles/*.srt` (lecture emphasis / intuition).
- Lecture-note PDFs in `../Lecture Notes/` are scanned handwriting (no text
  layer), so the textbook was used as the rigorous source for statements,
  theorems, and notation.

---

## Editing & rebuilding

**You do not edit Python to change cards.** All content lives as plain text in
[`source/`](source/), one file per lecture (`NN_topic.md`). The build script
parses those files and regenerates the `.apkg`.

```bash
cd "Anki Deck"
pip install genanki          # one-time
python3 build_deck.py        # -> ROB501_Mathematics_for_Robotics.apkg
```

Source-file format is documented in
[`source/README_FORMAT.txt`](source/README_FORMAT.txt). In short:

```
=== 03 | Abstract Linear Algebra ===

[QA]
Q:
What is a field?            ← LaTeX with \( … \) inline, \[ … \] display
A:
A set with two operations …
E:
Optional "Why / Intuition" note.

[CLOZE]
C:
A {{c1::vector space}} is closed under {{c2::linear combinations}}.
```

Tips:
- Use `\lt` / `\gt` instead of `<` / `>` inside math so HTML parsing stays safe.
- Re-importing the rebuilt `.apkg` **updates** existing cards (stable note IDs)
  without creating duplicates or losing your review history.

## License

Course content © Jessy Grizzle / Michigan Robotics, released under
**CC BY-NC 4.0** (see the repository [LICENSE](../LICENSE)). This deck is a
study aid derived from those materials under the same terms.
