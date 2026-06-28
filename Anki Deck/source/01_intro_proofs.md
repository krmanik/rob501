=== 01 | Intro & Proofs ===

[QA]
Q:
What does <b>ROB 501</b> aim to give you?
A:
A working command of <b>applied mathematics for robotics</b>: how to <i>read, write, and trust</i> mathematical arguments, plus the tools — linear algebra, inner-product spaces, least squares, estimation / Kalman filtering, real analysis, optimization — that underpin perception, estimation, and control.
E:
Course philosophy: math is a language you <i>use</i>. Proofs are practiced in a "safe environment" (linear algebra) before being applied to estimation and optimization.

[QA]
Q:
Define: <b>Theorem</b>, <b>Proposition</b>, <b>Lemma</b>, <b>Corollary</b>.
A:
<ul>
<li><b>Theorem</b> — an important statement proven true.</li>
<li><b>Proposition</b> — a less important but interesting true statement.</li>
<li><b>Lemma</b> — a true statement used as a stepping stone to prove other results.</li>
<li><b>Corollary</b> — a true statement following by a "simple" deduction from a theorem/proposition.</li>
</ul>
E:
All of these (plus axioms, definitions, claims) carry the <b>same logical power</b> in a proof — they are all true statements. The labels signal role and importance, not strength.

[QA]
Q:
What is an <b>axiom</b>, and how does it differ from a definition?
A:
An <b>axiom</b> is a basic assumption taken to be true without proof — the "bedrock" on which everything else is built (e.g. Euclid's parallel postulate, or \(a+b=b+a\) for integers). It resembles a definition but is reserved for the most fundamental assumptions of the system.

[QA]
Q:
In a <b>definition</b>, what does the word "if" actually mean?
A:
It means <b>"if and only if"</b>. "An integer \(n\) is even if \(n=2k\) for some integer \(k\)" is understood as a two-way characterization.
E:
<b>Caution:</b> in a <i>theorem/lemma/claim</i>, "if" means only one direction — there "if" and "iff" differ. The collapse happens only inside definitions.

[QA]
Q:
Define an <b>even</b> and an <b>odd</b> integer.
A:
\(n\) is <b>even</b> if \(n = 2k\) for some integer \(k\); \(n\) is <b>odd</b> if \(n = 2k+1\) for some integer \(k\).

[QA]
Q:
What is a <b>direct proof</b>?
A:
A proof that reaches the conclusion by directly applying simple rules of logic (\(p \Rightarrow q\)) to the given hypotheses, definitions, axioms, and known theorems — with no detour through contradiction.

[QA]
Q:
Give a direct proof that the <b>sum of two odd integers is even</b>.
A:
Let \(n_1=2k_1+1\) and \(n_2=2k_2+1\) (definition of odd). Then
\[ n_1+n_2 = (2k_1+1)+(2k_2+1) = 2(k_1+k_2+1). \]
Since \(k_1+k_2+1\) is an integer, \(n_1+n_2\) is even. \(\blacksquare\)

[QA]
Q:
What is the <b>contrapositive</b> of \(p \Rightarrow q\), and why is it useful?
A:
The contrapositive is \(\sim q \Rightarrow \sim p\). It is <b>logically equivalent</b> to \(p\Rightarrow q\):
\[ (p \Rightarrow q) \iff (\sim q \Rightarrow \sim p). \]
Proving the contrapositive often turns a hard implication into something that reads like a direct proof.
E:
Do <b>not</b> confuse contrapositive with <i>converse</i> (\(q\Rightarrow p\)). The converse is <b>not</b> equivalent to \(p\Rightarrow q\).

[QA]
Q:
Prove by contrapositive: if \(n^2\) is even, then \(n\) is even.
A:
Contrapositive: if \(n\) is odd then \(n^2\) is odd. Let \(n=2k+1\). Then
\[ n^2 = (2k+1)^2 = 4k^2+4k+1 = 2(2k^2+2k)+1, \]
which is odd. Hence the original implication holds. \(\blacksquare\)
E:
This lemma is exactly what gets reused later to prove \(\sqrt{2}\) is irrational.

[QA]
Q:
What is a <b>proof by exhaustion</b>?
A:
A proof that reduces the claim to a <b>finite number of cases</b> and verifies each separately. Famous example: the <i>Four Color Theorem</i> (≈1,482 map configurations checked by computer).
E:
In ROB 501, "four cases will already be a lot."

[CLOZE]
C:
A <b>rookie mistake</b> is to prove a statement <i>both</i> directly ({{c1::\(p\Rightarrow q\)}}) and by its {{c2::contrapositive}} (\(\sim q\Rightarrow\sim p\)) — because these are {{c3::logically equivalent}}, so you've proven the same thing twice instead of, say, an iff.

[QA]
Q:
To prove \(p \iff q\), what must you show?
A:
Both directions: \(p \Rightarrow q\) <b>and</b> its converse \(q \Rightarrow p\). One implication alone never establishes an "if and only if".

[QA]
Q:
Distinguish <b>logical and</b> (\(\wedge\)) from <b>logical or</b> (\(\vee\)).
A:
\(p_1 \wedge p_2\) is true only when <b>both</b> are true. \(p_1 \vee p_2\) is true when <b>at least one</b> is true (inclusive or): \(T\vee T=T\vee F=F\vee T=T\) and \(F\vee F=F\).
E:
This course uses inclusive "or" only — never exclusive or.

[CLOZE]
C:
Truth table for implication: \(p\Rightarrow q\) is <b>false in exactly one row</b> — when {{c1::\(p=T\) and \(q=F\)}}. In every other row it is {{c2::true}} (a false hypothesis makes the implication vacuously true).
E:
Equivalently \((p\Rightarrow q)\iff \sim(p\wedge\sim q)\).

[QA]
Q:
Express \(p \Rightarrow q\) using only <b>and</b> and <b>negation</b>.
A:
\[ (p \Rightarrow q) \;\iff\; \sim\!\big(p \wedge (\sim q)\big). \]
E:
This identity is the logical engine behind <b>proof by contradiction, Version II</b>: assume \(p\wedge\sim q\) and derive a contradiction.

[QA]
Q:
How do you <b>negate</b> a quantified statement, e.g. \(\forall x,\ P(x)\)?
A:
Swap the quantifier and negate the predicate:
\[ \sim\big(\forall x,\ P(x)\big) \iff \exists x,\ \sim P(x), \qquad \sim\big(\exists x,\ P(x)\big) \iff \forall x,\ \sim P(x). \]
E:
Negating "for all" gives "there exists a counterexample" — the basis of disproof.

[QA]
Q:
What does <b>QED</b> (\(\blacksquare\) / \(\square\)) mark?
A:
<i>quod erat demonstrandum</i> — "thus it was demonstrated". It signals the proof is complete. Modern texts use \(\square\) or \(\blacksquare\).

[QA]
Q:
Name the structural properties of the real numbers \(\mathbb{R}\) assumed in this course.
A:
\(\mathbb{R}\) is a <b>complete ordered field</b>:
<ul>
<li><b>Field axioms</b> — closure, commutativity, associativity, distributivity, additive & multiplicative inverses.</li>
<li><b>Order</b> — a total order compatible with \(+\) and \(\times\).</li>
<li><b>Completeness</b> — every nonempty set bounded above has a least upper bound (supremum).</li>
</ul>
E:
Completeness is what later guarantees Cauchy sequences converge and continuous functions attain extrema on compact sets.
