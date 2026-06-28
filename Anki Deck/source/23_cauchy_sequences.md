=== 23 | Cauchy Sequences ===

[QA]
Q:
Define a <b>Cauchy sequence</b>.
A:
\((x_n)\) is Cauchy if
\[ \forall\epsilon\gt0,\ \exists N\ \text{s.t.}\ \forall n,m\ge N,\ \|x_n-x_m\|\lt\epsilon. \]
E:
"Terms eventually get arbitrarily close to <i>each other</i>" — no limit point is referenced.

[QA]
Q:
Prove: every <b>convergent</b> sequence is Cauchy.
A:
If \(x_n\to x\), pick \(N\) with \(\|x_n-x\|\lt\epsilon/2\) for \(n\ge N\). Then for \(n,m\ge N\),
\[ \|x_n-x_m\|\le\|x_n-x\|+\|x-x_m\|\lt\tfrac\epsilon2+\tfrac\epsilon2=\epsilon. \]
\(\blacksquare\)

[QA]
Q:
Is every Cauchy sequence convergent? Give the standard counterexample.
A:
<b>No.</b> In \(C[0,1]\) with \(\|f\|_1=\int_0^1|f|\,dt\), the piecewise-linear "ramps" approaching a step function are Cauchy (\(\|f_n-f_m\|_1=\tfrac12|\tfrac1n-\tfrac1m|\to0\)) but converge to a <b>discontinuous</b> step function \(\notin C[0,1]\).
E:
All such counterexamples live in <b>infinite-dimensional</b> spaces.

[QA]
Q:
Define a <b>complete</b> normed space (Banach space).
A:
A normed space in which <b>every</b> Cauchy sequence has a limit <i>within the space</i>. A complete normed space is called a <b>Banach space</b>.
E:
\((C[a,b],\|\cdot\|_\infty)\) is complete; \((C[a,b],\|\cdot\|_1)\) is not.

[QA]
Q:
State key completeness facts about subspaces and subsets.
A:
<ul>
<li>Every <b>finite-dimensional</b> subspace is complete.</li>
<li>Any <b>closed</b> subset of a complete set is complete.</li>
<li>Complete \(\Rightarrow\) closed.</li>
</ul>

[QA]
Q:
Define a <b>contraction mapping</b> and a <b>fixed point</b>.
A:
\(T:S\to S\) is a contraction if \(\exists\,0\le c\lt1\) with \(\|T(x)-T(y)\|\le c\|x-y\|\) for all \(x,y\in S\). A point \(x^\ast\) is a fixed point if \(T(x^\ast)=x^\ast\).

[QA]
Q:
State the <b>Contraction Mapping Theorem</b>.
A:
If \(T\) is a contraction on a <b>complete</b> subset \(S\), there is a <b>unique</b> fixed point \(x^\ast\in S\). Moreover, for any \(x_0\in S\), the iteration \(x_{n+1}=T(x_n)\) is Cauchy and \(x_n\to x^\ast\).
E:
Proof: \(\|x_{n+1}-x_n\|\le c^n\|x_1-x_0\|\) gives \(\|x_{n+k}-x_n\|\le\frac{c^n}{1-c}\|x_1-x_0\|\to0\) (Cauchy); completeness gives the limit; the contraction bound forces uniqueness.

[CLOZE]
C:
Convergent \(\Rightarrow\) {{c1::Cauchy}}, but the converse needs {{c2::completeness}} (a Banach space). A {{c3::contraction}} on a complete set has a unique fixed point, reached by iterating \(x_{n+1}=T(x_n)\).
