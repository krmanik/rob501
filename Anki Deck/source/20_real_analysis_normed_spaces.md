=== 20 | Real Analysis & Normed Spaces ===

[QA]
Q:
Define the <b>open ball</b> \(B_a(x_0)\) in a normed space.
A:
\[ B_a(x_0)=\{x\in X:\|x-x_0\|\lt a\},\qquad a\gt0. \]
E:
The shape of the ball depends on the norm: \(\|\cdot\|_2\) gives a disk, \(\|\cdot\|_1\) a diamond, \(\|\cdot\|_\infty\) a square.

[QA]
Q:
Characterize \(d(x,S)=0\) and \(d(x,S)\gt0\) using balls.
A:
\[ d(x,S)=0 \iff \forall\epsilon\gt0,\ B_\epsilon(x)\cap S\ne\emptyset, \]
\[ d(x,S)\gt0 \iff \exists\epsilon\gt0,\ B_\epsilon(x)\cap S=\emptyset\ (\text{i.e. }B_\epsilon(x)\subset\,\sim\! S). \]
E:
When \(d(x,S)\gt0\), the witness is \(\epsilon=d(x,S)/2\).

[QA]
Q:
Define an <b>open set</b> (via interior) and give the distance form.
A:
\(P\) is open if \(P=\mathring P\) (every point is interior). Equivalently
\[ P\ \text{open} \iff P=\{x\in X: d(x,\sim\! P)\gt0\}. \]
E:
\((0,1)\subset\mathbb{R}\) is open: each \(x\) has \(d(x,\sim\!P)=\min\{x,1-x\}\gt0\). \([0,1)\) is not open (the point \(0\) fails).

[QA]
Q:
Define a <b>closed set</b> via closure points.
A:
\(x\) is a closure point of \(P\) if \(d(x,P)=0\) (every ball around \(x\) meets \(P\)). \(P\) is <b>closed</b> if \(P=\bar P\) (it contains all its closure points).
E:
\([0,1)\) is not closed: \(1\notin[0,1)\) yet \(d(1,[0,1))=0\). \([0,1]\) is closed.

[QA]
Q:
State the open/closed <b>duality</b> theorem.
A:
\[ P\ \text{open} \iff \sim\! P\ \text{closed},\qquad P\ \text{closed}\iff \sim\! P\ \text{open}. \]
E:
One-line proof: \(\mathring P=\{x:d(x,\sim\!P)\gt0\}\) and \(\overline{\sim\!P}=\{x:d(x,\sim\!P)=0\}\) are complements.

[QA]
Q:
Define <b>convergence</b> \(x_n\to x\) of a sequence in a normed space.
A:
\[ \forall\epsilon\gt0,\ \exists N\lt\infty\ \text{s.t.}\ \forall n\ge N,\ \|x_n-x\|\lt\epsilon. \]
E:
Limits are unique. Sequences are the bridge between the algebra (norms) and topology (open/closed, continuity).

[QA]
Q:
How do sequences characterize <b>closed</b> sets?
A:
\(P\) is closed \(\iff\) for every sequence \((x_n)\) in \(P\) with \(x_n\to x_0\), the limit \(x_0\in P\). "Closed = closed under taking limits."

[CLOZE]
C:
A set \(P\) is open iff \(P=\{x:d(x,\sim\!P){{c1::\gt0}}\}\); it is closed iff it contains all its {{c2::closure points}} (\(d(x,P)=0\)). The two notions are dual: \(P\) open \(\iff\) {{c3::\(\sim\!P\) closed}}.
