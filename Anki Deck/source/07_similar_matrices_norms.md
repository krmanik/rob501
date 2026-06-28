=== 07 | Similar Matrices & Norms ===

[QA]
Q:
When are two square matrices \(A,B\) <b>similar</b>?
A:
If there is an invertible \(P\) with
\[ B = P^{-1} A P. \]
\(A\) and \(B\) are then matrix representations of the <b>same linear operator</b> in two different bases, and \(P\) is the change-of-basis matrix.

[QA]
Q:
Which quantities are <b>invariant</b> under similarity?
A:
The characteristic polynomial, and hence <b>eigenvalues</b> (with multiplicities), <b>determinant</b>, <b>trace</b>, and <b>rank</b>.
E:
\(\det(P^{-1}AP-\lambda I)=\det\!\big(P^{-1}(A-\lambda I)P\big)=\det(A-\lambda I)\). Eigenvectors do change (they get mapped by \(P^{-1}\)).

[QA]
Q:
What three axioms define a <b>norm</b> \(\|\cdot\|\) on a vector space \((X,\mathbb{F})\)?
A:
For all \(x,y\in X\), \(\alpha\in\mathbb{F}\):
<ul>
<li><b>Positivity:</b> \(\|x\|\ge0\), with \(\|x\|=0\iff x=0\);</li>
<li><b>Homogeneity:</b> \(\|\alpha x\|=|\alpha|\,\|x\|\);</li>
<li><b>Triangle inequality:</b> \(\|x+y\|\le\|x\|+\|y\|\).</li>
</ul>
E:
\((X,\mathbb{F},\|\cdot\|)\) is then a <b>normed space</b>. A norm is the abstract notion of "length."

[QA]
Q:
Define the <b>\(p\)-norm</b>, <b>2-norm</b>, and <b>\(\infty\)-norm</b> on \(\mathbb{F}^n\).
A:
\[ \|x\|_p=\Big(\sum_{i=1}^n |x_i|^p\Big)^{1/p}\ (1\le p\lt\infty),\quad \|x\|_2=\sqrt{\textstyle\sum_i |x_i|^2},\quad \|x\|_\infty=\max_{1\le i\le n}|x_i|. \]

[QA]
Q:
What is \(\displaystyle\lim_{p\to\infty}\|x\|_p\)?
A:
\[ \lim_{p\to\infty}\|x\|_p=\|x\|_\infty=\max_i|x_i|. \]
E:
Proof idea: factor out \(\|x\|_\infty\); the remaining terms are \(\le1\) and \(\sqrt[p]{a}\to1\) for any fixed \(a\ge0\). Hence the name "\(\infty\)-norm."

[QA]
Q:
Give the function-space norms on \(X=\{f:[a,b]\to\mathbb{R}\ \text{continuous}\}\).
A:
\[ \|f\|_p=\Big(\int_a^b |f(t)|^p\,dt\Big)^{1/p},\qquad \|f\|_\infty=\sup_{a\le t\le b}|f(t)|. \]

[QA]
Q:
Define <b>distance to a set</b> \(d(x,S)\) and a <b>best approximation</b>.
A:
\[ d(x,S):=\inf_{y\in S}\|x-y\|. \]
A point \(x^\ast\in S\) is a <b>best approximation</b> of \(x\) if \(d(x,S)=\|x-x^\ast\|\) — the infimum is attained. Then \(x^\ast=\arg\min_{y\in S}\|x-y\|\).
E:
The three guiding questions of the chapter: does a best approximation <i>exist</i>, how do we <i>compute</i> it, and is it <i>unique</i>?

[QA]
Q:
Can the best-approximation problem fail to have a <b>unique</b> answer? Give the canonical example.
A:
Yes — the \(1\)-norm is not "strict." For \(x=[1\ 1]^\top\) and \(M=\{[x_1\ x_2]^\top:x_2=-x_1\}\), every point with \(|x_1|\le1,\ x_2=-x_1\) achieves \(\|x-\hat x\|_1=2\) — an uncountable set of minimizers.
E:
Strictly convex norms (like the \(2\)-norm) give a unique projection; the \(1\)- and \(\infty\)-norms need not.
