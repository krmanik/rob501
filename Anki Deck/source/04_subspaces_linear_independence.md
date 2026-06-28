=== 04 | Subspaces & Linear Independence ===

[QA]
Q:
Define a <b>subspace</b> of a vector space \((X,\mathbb{F})\).
A:
A subset \(Y\subset X\) such that \((Y,\mathbb{F})\) is itself a vector space under the addition and scalar multiplication inherited from \(X\).

[QA]
Q:
State the <b>subspace test</b> (the practical TFAE conditions).
A:
\(Y\subset X\) is a subspace iff any one of these holds:
<ul>
<li>closed under addition <b>and</b> scalar multiplication;</li>
<li>\(\forall v^1,v^2\in Y,\ \forall\alpha\in\mathbb{F}:\ \alpha v^1+v^2\in Y\);</li>
<li>\(\forall v^1,v^2\in Y,\ \forall\alpha_1,\alpha_2\in\mathbb{F}:\ \alpha_1 v^1+\alpha_2 v^2\in Y\) (closed under linear combinations).</li>
</ul>
E:
<b>First thing to check:</b> is \(0\in Y\)? If not, \(Y\) is not a subspace — fast disproof.

[QA]
Q:
Why is \(Y=\left\{\begin{bmatrix}\beta\\2\beta\end{bmatrix}+\begin{bmatrix}1\\0\end{bmatrix}:\beta\in\mathbb{R}\right\}\) <b>not</b> a subspace of \((\mathbb{R}^2,\mathbb{R})\)?
A:
It is an affine line not through the origin: \(0\notin Y\) (no \(\beta\) gives the zero vector). Failing to contain \(0\) immediately disqualifies it.
E:
Likewise \(\{f:\mathbb{R}\to\mathbb{R}\mid f(2)=1\}\) is not a subspace — the zero function gives \(f(2)=0\ne1\).

[QA]
Q:
Define a <b>linear combination</b>. What subtlety is emphasized?
A:
A <b>finite</b> sum \(\alpha_1 v^1+\cdots+\alpha_n v^n\) with \(n\ge1\), \(\alpha_i\in\mathbb{F}\), \(v^i\in X\).
E:
An infinite sum \(\sum_{i=1}^{\infty}\alpha_i v^i\) is <b>not</b> a linear combination — finiteness matters (convergence/limits are a separate, later story).

[QA]
Q:
Define the <b>span</b> of a set of vectors.
A:
\(\operatorname{span}\{v^1,\dots,v^k\}\) is the set of <b>all finite linear combinations</b> \(\sum_i\alpha_i v^i\), \(\alpha_i\in\mathbb{F}\). It is always a subspace of \(X\) — the smallest one containing the \(v^i\).

[QA]
Q:
Define <b>linearly dependent</b> and <b>linearly independent</b> sets.
A:
\(\{v^1,\dots,v^k\}\) is <b>linearly dependent</b> if there exist scalars \(\alpha_1,\dots,\alpha_k\), <b>not all zero</b>, with
\[ \alpha_1 v^1+\cdots+\alpha_k v^k = 0. \]
Otherwise it is <b>linearly independent</b> (the equation forces all \(\alpha_i=0\)).

[QA]
Q:
If \(\{v^1,\dots,v^k\}\) is linearly dependent with \(\alpha_k\ne0\), what follows?
A:
One vector is a linear combination of the others:
\[ v^k = -\tfrac{\alpha_1}{\alpha_k}v^1-\cdots-\tfrac{\alpha_{k-1}}{\alpha_k}v^{k-1}. \]
So dependence \(\iff\) some vector is redundant (lies in the span of the rest).

[QA]
Q:
Show \(\{e_1,\dots,e_n\}\) is linearly independent in \((\mathbb{F}^n,\mathbb{F})\).
A:
\[ \alpha_1 e_1+\cdots+\alpha_n e_n=\begin{bmatrix}\alpha_1\\\vdots\\\alpha_n\end{bmatrix}=0 \;\Longrightarrow\; \alpha_1=\cdots=\alpha_n=0. \]
So the only combination giving \(0\) is the trivial one — independent (and it spans \(\mathbb{F}^n\)).

[CLOZE]
C:
A set is linearly {{c1::dependent}} iff some nontrivial combination equals \(0\); equivalently iff one vector lies in the {{c2::span}} of the others. The standard basis \(\{e_i\}\) is linearly {{c3::independent}}.
