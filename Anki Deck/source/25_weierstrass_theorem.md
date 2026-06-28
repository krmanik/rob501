=== 25 | Weierstrass Theorem ===

[QA]
Q:
Define a <b>subsequence</b> and a <b>bounded</b> set.
A:
A subsequence \((x_{n_i})\) picks indices \(1\le n_1\lt n_2\lt\cdots\). A set \(S\) is <b>bounded</b> if \(S\subset B_r(0)\) for some \(r\lt\infty\), equivalently \(\sup_{x\in S}\|x\|\lt\infty\).
E:
If \(x_n\to x\), then every subsequence also \(\to x\).

[QA]
Q:
Define a <b>compact</b> set (sequential compactness).
A:
\(C\) is compact if every sequence in \(C\) has a subsequence converging to a limit <b>in \(C\)</b>.

[QA]
Q:
State the <b>Bolzano–Weierstrass / Sequential Compactness Theorem</b>.
A:
In a <b>finite-dimensional</b> normed space, for \(C\subset X\):
\[ C\ \text{closed and bounded} \iff C\ \text{compact (every sequence has a convergent subsequence with limit in }C). \]
E:
The equivalence "closed + bounded = compact" holds in finite dimensions; in infinite dimensions it can fail.

[QA]
Q:
State the result on <b>equivalent norms</b> in finite dimensions.
A:
On a finite-dimensional vector space, <b>all norms are equivalent</b>: for any two norms \(\exists K_1,K_2\gt0\) with
\[ K_1|||x|||\le\|x\|\le K_2|||x|||\quad\forall x. \]
E:
Consequence: convergence, Cauchy-ness, open/closed, and compactness are <i>norm-independent</i> in finite dimensions. (A space is finite-dimensional iff all its norms are equivalent.)

[QA]
Q:
State the <b>Weierstrass (Extreme Value) Theorem</b>.
A:
If \(C\) is <b>compact</b> and \(f:C\to\mathbb{R}\) is <b>continuous</b>, then \(f\) attains its sup and inf:
\[ \exists x^\ast,x_\ast\in C:\quad f(x^\ast)=\sup_{x\in C}f(x),\quad f(x_\ast)=\inf_{x\in C}f(x). \]
E:
This is the theorem that guarantees a minimizer <i>exists</i> — the foundation under every "\(\arg\min\)" we write.

[QA]
Q:
Sketch why Weierstrass holds.
A:
Take \(x_n\) with \(f(x_n)\to\sup f\). Compactness gives a subsequence \(x_{n_i}\to x^\ast\in C\); continuity gives \(f(x_{n_i})\to f(x^\ast)\). A contradiction argument first shows \(\sup f\) is finite. Hence \(f(x^\ast)=\sup f\). \(\blacksquare\)

[CLOZE]
C:
In finite dimensions, \(C\) is compact iff it is {{c1::closed and bounded}}, and all norms are {{c2::equivalent}}. Weierstrass: a {{c3::continuous}} function on a compact set attains its maximum and minimum.
