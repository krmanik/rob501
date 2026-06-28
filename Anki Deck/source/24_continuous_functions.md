=== 24 | Continuous Functions ===

[QA]
Q:
State the <b>ε–δ definition</b> of continuity at a point.
A:
\(f:(X,\|\cdot\|)\to(Y,|||\cdot|||)\) is continuous at \(x_0\) if
\[ \forall\epsilon\gt0,\ \exists\delta(\epsilon,x_0)\gt0\ \text{s.t.}\ \|x-x_0\|\lt\delta\Rightarrow|||f(x)-f(x_0)|||\lt\epsilon. \]
\(f\) is continuous if it is continuous at every \(x_0\).
E:
Ball form: \(\forall\epsilon\gt0,\exists\delta\gt0\) with \(f(B_\delta(x_0))\subset B_\epsilon(f(x_0))\).

[QA]
Q:
Negate the definition: when is \(f\) <b>discontinuous</b> at \(x_0\)?
A:
\[ \exists\epsilon\gt0\ \text{s.t.}\ \forall\delta\gt0,\ \exists x\in B_\delta(x_0)\ \text{with}\ |||f(x)-f(x_0)|||\ge\epsilon. \]
E:
No matter how small you make \(\delta\), some nearby point is thrown at least \(\epsilon\) away in the output.

[QA]
Q:
State the <b>sequential characterization</b> of continuity.
A:
\(f\) is continuous at \(x_0\) <b>iff</b> for every sequence \(x_n\to x_0\), \(f(x_n)\to f(x_0)\):
\[ f\ \text{continuous at }x_0 \iff \big(x_n\to x_0\Rightarrow f(x_n)\to f(x_0)\big). \]
E:
Just as sequences characterize closed sets, they characterize continuity — often easier to use than ε–δ.

[QA]
Q:
How do you use the sequential characterization to <b>prove discontinuity</b>?
A:
Exhibit a single sequence \(x_n\to x_0\) for which \(f(x_n)\not\to f(x_0)\). One failing sequence suffices.

[CLOZE]
C:
Continuity at \(x_0\): \(\forall\epsilon\gt0,\exists\delta\gt0\) s.t. \(\|x-x_0\|\lt\delta\Rightarrow|||f(x)-f(x_0)|||\lt{{c1::\epsilon}}\). Equivalently (sequential form) \(x_n\to x_0\Rightarrow{{c2::f(x_n)\to f(x_0)}}\).
