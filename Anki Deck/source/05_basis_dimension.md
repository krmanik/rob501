=== 05 | Basis Vectors & Dimension ===

[QA]
Q:
Define a <b>basis</b> of a vector space \((X,\mathbb{F})\).
A:
A set of vectors that is (i) <b>linearly independent</b> and (ii) <b>spans</b> \(X\). Equivalently, every \(x\in X\) is a finite linear combination of basis vectors, and no basis vector is redundant.

[QA]
Q:
Define the <b>dimension</b> of \((X,\mathbb{F})\).
A:
\((X,\mathbb{F})\) has finite dimension \(n\gt0\) if there exists a linearly independent set of \(n\) vectors and <b>every</b> set of \(n+1\) vectors is linearly dependent. It is <b>infinite dimensional</b> if for every \(n\) there is an independent set of size \(\ge n\).
E:
Equivalently, dimension = cardinality of any basis. By convention \(\dim\{0\}=0\).

[QA]
Q:
Give the dimensions: \(\dim(\mathbb{F}^n,\mathbb{F})\), \(\dim(\mathbb{C}^n,\mathbb{R})\), \(\dim(\mathcal{P}(t),\mathbb{R})\).
A:
\[ \dim(\mathbb{F}^n,\mathbb{F})=n,\quad \dim(\mathbb{C}^n,\mathbb{R})=2n,\quad \dim(\mathcal{P}(t),\mathbb{R})=\infty. \]
E:
\((\mathbb{C}^n,\mathbb{R})\) needs \(\{e_i\}\cup\{j e_i\}\) — \(2n\) vectors — because the reals can't supply the factor \(j\).

[QA]
Q:
Theorem: in an \(n\)-dimensional space, any \(n\) linearly independent vectors form a basis. Why?
A:
Given independent \(\{v^1,\dots,v^n\}\) and any \(x\), the set \(\{x,v^1,\dots,v^n\}\) has \(n+1\) vectors, hence is dependent: \(\beta_0 x+\sum\beta_i v^i=0\) nontrivially. If \(\beta_0=0\) the \(v^i\) would be dependent (contradiction), so \(\beta_0\ne0\) and \(x=\sum(-\beta_i/\beta_0)v^i\). Thus they span. \(\blacksquare\)
E:
So once you know the dimension \(n\), checking just <i>independence</i> of \(n\) vectors is enough — you get spanning for free.

[QA]
Q:
Proposition: relative to a basis, the representation of a vector is <b>unique</b>. Prove it.
A:
If \(x=\sum\alpha_i v^i=\sum\beta_i v^i\), then \(0=\sum(\alpha_i-\beta_i)v^i\). Linear independence forces \(\alpha_i-\beta_i=0\), i.e. \(\alpha_i=\beta_i\) for all \(i\). \(\blacksquare\)

[QA]
Q:
Define the <b>representation</b> \([x]_v\) of \(x\) with respect to basis \(v=\{v^1,\dots,v^n\}\).
A:
If \(x=\alpha_1 v^1+\cdots+\alpha_n v^n\) then
\[ [x]_v:=\begin{bmatrix}\alpha_1\\\vdots\\\alpha_n\end{bmatrix}\in\mathbb{F}^n. \]
E:
Once a basis is fixed, abstract vectors (polynomials, matrices, functions) become concrete \(n\)-tuples you can compute with numerically.

[QA]
Q:
Can any linearly independent set be extended to a basis?
A:
<b>Yes</b> (finite dimension). If \(\{v^1,\dots,v^k\}\) is independent with \(k\lt n=\dim X\), there exists \(v^{k+1}\) keeping independence; repeating (induction) completes it to a basis \(\{v^1,\dots,v^n\}\).
E:
Proof idea: if no such \(v^{k+1}\) existed, the \(k\) vectors would span \(X\), forcing \(n\le k\) — contradiction.

[QA]
Q:
What is the <b>change-of-basis matrix</b> \(P\) between bases \(v\) and \(w\), and how does it act?
A:
Let \(P\) have columns \([w^j]_v\) (each new basis vector expressed in the old basis \(v\)). Then for any \(x\),
\[ [x]_v = P\,[x]_w, \qquad [x]_w = P^{-1}[x]_v. \]
\(P\) is invertible because both \(v\) and \(w\) are bases.

[QA]
Q:
Compute \([x]_v\) for \(x=\begin{bmatrix}5&3\\1&4\end{bmatrix}\) in the standard basis of \(\mathbb{R}^{2\times2}\).
A:
With \(v=\{E_{11},E_{12},E_{21},E_{22}\}\) (read across rows),
\[ [x]_v=\begin{bmatrix}5\\3\\1\\4\end{bmatrix}. \]
E:
Matrices are vectors: a \(2\times2\) real matrix is a point in the \(4\)-dimensional space \((\mathbb{R}^{2\times2},\mathbb{R})\).
