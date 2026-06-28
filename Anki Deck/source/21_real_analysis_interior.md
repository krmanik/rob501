=== 21 | Real Analysis & Interior of a Set ===

[QA]
Q:
Define an <b>interior point</b> and the <b>interior</b> \(\mathring P\) of a set \(P\).
A:
\(p\in P\) is an interior point if \(\exists\epsilon\gt0\) with \(B_\epsilon(p)\subset P\). The interior is
\[ \mathring P=\{p\in P: p\ \text{interior}\}=\{x\in X: d(x,\sim\! P)\gt0\}. \]
E:
An interior point sits "strictly inside" \(P\), with room to wiggle in every direction.

[QA]
Q:
Define the <b>closure</b> \(\bar P\) and the <b>boundary</b> \(\partial S\).
A:
\(\bar P=\{x: d(x,P)=0\}\) (all closure points). The boundary is
\[ \partial S=\bar S\cap\overline{(\sim\! S)}=\bar S\setminus\mathring S. \]
E:
Boundary points are arbitrarily close to both \(S\) and its complement.

[QA]
Q:
Can a set be both open and closed (<b>clopen</b>)? Give examples.
A:
Yes. In any normed space, both \(X\) and \(\emptyset\) are clopen.
E:
\(\emptyset\) is open and closed by convention so that complements of open sets are closed and vice versa.

[QA]
Q:
State the union/intersection rules for open and closed sets.
A:
<ul>
<li><b>Arbitrary</b> union of open sets is open; <b>arbitrary</b> intersection of closed sets is closed.</li>
<li><b>Finite</b> intersection of open sets is open; <b>finite</b> union of closed sets is closed.</li>
</ul>
E:
"Finite" is essential: \(\bigcap_{n\ge1}\big(-1-\tfrac1n,\,1\big)=[-1,1)\) — an infinite intersection of open sets that is not open.

[QA]
Q:
Are the rationals \(\mathbb{Q}\subset\mathbb{R}\) open, closed, or neither?
A:
<b>Neither.</b> Every ball around a rational contains irrationals (not open), and every real is a limit of rationals, so \(\bar{\mathbb{Q}}=\mathbb{R}\ne\mathbb{Q}\) (not closed).

[QA]
Q:
Give the distance characterizations of interior and closure in one place.
A:
\[ \mathring P=\{x: d(x,\sim\! P)\gt0\},\qquad \bar P=\{x: d(x,P)=0\}. \]
E:
These reduce all open/closed/interior/closure questions to computing a single distance to a set.

[CLOZE]
C:
\(p\) is an interior point of \(P\) iff some {{c1::ball}} \(B_\epsilon(p)\subset P\). An <b>arbitrary</b> union of {{c2::open}} sets is open, but only a <b>finite</b> {{c3::intersection}} of open sets is guaranteed open.
