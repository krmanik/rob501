=== 03 | Abstract Linear Algebra ===

[QA]
Q:
Define a <b>field</b> \((\mathbb{F},+,\cdot)\).
A:
A set \(\mathbb{F}\) of scalars with two operations \(+\) and \(\cdot\) such that, for all \(\alpha,\beta,\gamma\in\mathbb{F}\):
<ul>
<li>closure under \(+\) and \(\cdot\);</li>
<li>both operations commutative and associative;</li>
<li>\(\cdot\) distributes over \(+\);</li>
<li>additive identity \(0\) and multiplicative identity \(1\) exist;</li>
<li>every \(\alpha\) has an additive inverse; every \(\alpha\ne0\) has a multiplicative inverse.</li>
</ul>
E:
Seven axioms. To <i>prove</i> a set is a field, check all seven; to <i>disprove</i>, exhibit one failure. Canonical example to keep in mind: \(\mathbb{F}=\mathbb{R}\).

[QA]
Q:
Give examples and non-examples of <b>fields</b>.
A:
<b>Fields:</b> \(\mathbb{R},\ \mathbb{C},\ \mathbb{Q}\).
<br><b>Not fields:</b> the irrationals (not closed under \(+\)), \(2\times2\) real matrices (\(\cdot\) not commutative), \(2\times2\) real <i>diagonal</i> matrices (a nonzero one can fail to have a multiplicative inverse).

[QA]
Q:
Define a <b>vector space</b> \((X,\mathbb{F})\).
A:
A set \(X\) of <b>vectors</b> over a field \(\mathbb{F}\) with vector addition and scalar multiplication satisfying ten axioms: \(X\) is an abelian group under \(+\) (closure, commutativity, associativity, a zero vector \(0\), additive inverses), and scalar multiplication is associative, distributes over vector and scalar addition, and \(1\cdot v=v\).
E:
The field and the vector set are <i>both</i> part of the data — write \((X,\mathbb{F})\). Changing the field can change everything (see \((\mathbb{C}^n,\mathbb{C})\) vs \((\mathbb{C}^n,\mathbb{R})\)).

[QA]
Q:
Why is the <b>field part</b> of \((X,\mathbb{F})\) essential? Contrast \((\mathbb{C},\mathbb{R})\) with \((\mathbb{C},\mathbb{C})\).
A:
The same vector set \(\mathbb{C}\) gives <i>different</i> vector spaces depending on the field. \((\mathbb{C},\mathbb{C})\) is \(1\)-dimensional; \((\mathbb{C},\mathbb{R})\) is \(2\)-dimensional (basis \(\{1,j\}\)) because you may only scale by reals.
E:
A scalar-times-vector product must land back in \(X\). \((\mathbb{R},\mathbb{C})\) fails: a complex scalar times a real vector is not real.

[QA]
Q:
Show that the set of functions \(X=\{f:D\to\mathbb{R}\}\) with pointwise operations is a vector space — illustrate one axiom.
A:
Define \((f+g)(t):=f(t)+g(t)\) and \((\alpha f)(t):=\alpha f(t)\). Distributivity of scalar mult. over vector addition: for any \(t\in D\),
\[ [\alpha(f+g)](t)=\alpha[f(t)+g(t)]=\alpha f(t)+\alpha g(t)=[\alpha f+\alpha g](t). \]
Since LHS = RHS for all \(t\), the functions are equal. \(\blacksquare\)
E:
Proofs about function spaces reduce to evaluating "at a point \(t\)" and then using the known arithmetic of \(\mathbb{R}\).

[QA]
Q:
Give three standard examples of vector spaces used throughout the course.
A:
<ul>
<li>\((\mathbb{F}^n,\mathbb{F})\) — \(n\)-tuples (columns) with entrywise operations.</li>
<li>\((\mathbb{F}^{n\times m},\mathbb{F})\) — matrices are vectors too.</li>
<li>\((\mathcal{P}(t),\mathbb{R})\) — polynomials with real coefficients.</li>
</ul>

[QA]
Q:
List the strategy for <b>proving</b> vs <b>disproving</b> that \((X,\mathbb{F})\) is a vector space.
A:
<b>Prove:</b> verify all ten axioms hold. <b>Disprove:</b> exhibit a single violated axiom — most efficiently, show closure under \(+\) or scalar multiplication fails, or that \(0\notin X\).
E:
Example non-vector-space: \(X=\{x\in\mathbb{R}:x\ge0\}\) over \(\mathbb{R}\) fails — scaling by \(\alpha\lt0\) leaves \(X\).
