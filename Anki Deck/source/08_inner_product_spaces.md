=== 08 | Inner Product Spaces ===

[QA]
Q:
Define an <b>inner product</b> \(\langle\cdot,\cdot\rangle:X\times X\to\mathbb{C}\) on \((X,\mathbb{C})\).
A:
For all \(x_1,x_2,y\in X\), \(\alpha_1,\alpha_2\in\mathbb{C}\):
<ul>
<li><b>Conjugate symmetry:</b> \(\langle a,b\rangle=\overline{\langle b,a\rangle}\);</li>
<li><b>Linearity (left):</b> \(\langle \alpha_1 x_1+\alpha_2 x_2,\,y\rangle=\alpha_1\langle x_1,y\rangle+\alpha_2\langle x_2,y\rangle\);</li>
<li><b>Positive definiteness:</b> \(\langle x,x\rangle\ge0\), with \(=0\iff x=0\).</li>
</ul>
E:
Over \(\mathbb{R}\), conjugate symmetry becomes plain symmetry \(\langle a,b\rangle=\langle b,a\rangle\). Note \(\langle x,x\rangle\) is always real, so comparing to \(0\) makes sense.

[QA]
Q:
How does linearity behave in the <b>right</b> argument of a complex inner product?
A:
It is <b>conjugate</b>-linear:
\[ \langle x,\ \beta_1 y_1+\beta_2 y_2\rangle=\overline{\beta_1}\,\langle x,y_1\rangle+\overline{\beta_2}\,\langle x,y_2\rangle. \]
Over \(\mathbb{R}\) the conjugates vanish and it is linear in both arguments.

[QA]
Q:
List the standard inner products used in the course.
A:
<ul>
<li>\((\mathbb{R}^n,\mathbb{R})\): \(\langle x,y\rangle=x^\top y\).</li>
<li>\((\mathbb{C}^n,\mathbb{C})\): \(\langle x,y\rangle=x^\top \overline{y}\).</li>
<li>real \(n\times m\) matrices: \(\langle A,B\rangle=\operatorname{tr}(A^\top B)\).</li>
<li>\(\{f:[a,b]\to\mathbb{R}\}\): \(\langle f,g\rangle=\int_a^b f(t)g(t)\,dt\).</li>
</ul>

[QA]
Q:
State the <b>Cauchy–Schwarz inequality</b>.
A:
\[ |\langle x,y\rangle|\le \langle x,x\rangle^{1/2}\,\langle y,y\rangle^{1/2}=\|x\|\,\|y\|. \]
E:
Proof: for \(y\ne0\), expand \(0\le\|x-\lambda y\|^2\) and minimize over \(\lambda\); the minimizer \(\lambda=\langle x,y\rangle/\langle y,y\rangle\) gives \(0\le\langle x,x\rangle-|\langle x,y\rangle|^2/\langle y,y\rangle\).

[QA]
Q:
How does an inner product <b>induce a norm</b>, and what makes it a norm?
A:
\[ \|x\|:=\sqrt{\langle x,x\rangle}. \]
Positivity and homogeneity are immediate; the triangle inequality follows from Cauchy–Schwarz:
\[ \|x+y\|^2=\|x\|^2+\|y\|^2+2\,\mathrm{Re}\langle x,y\rangle\le(\|x\|+\|y\|)^2. \]

[QA]
Q:
Define <b>orthogonal</b>, <b>orthogonal set</b>, and <b>orthonormal set</b>.
A:
\(x\perp y\iff\langle x,y\rangle=0\). A set is <b>orthogonal</b> if every distinct pair is orthogonal; it is <b>orthonormal</b> if additionally \(\|x\|=1\) for every element.
E:
Normalize any \(x\ne0\) via \(x/\|x\|\), which has unit norm.

[QA]
Q:
State and prove the <b>Pythagorean Theorem</b> in an inner product space.
A:
If \(x\perp y\) then
\[ \|x+y\|^2=\|x\|^2+\|y\|^2. \]
Proof: \(\|x+y\|^2=\|x\|^2+\|y\|^2+2\langle x,y\rangle\), and \(\langle x,y\rangle=0\). \(\blacksquare\)

[CLOZE]
C:
Cauchy–Schwarz: \(|\langle x,y\rangle|\le\) {{c1::\(\|x\|\,\|y\|\)}}, with equality iff \(x,y\) are {{c2::linearly dependent}}. It is the key step proving the {{c3::triangle inequality}} for the induced norm.
