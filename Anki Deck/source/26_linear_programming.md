=== 26 | Final Class & Linear Programming ===

[QA]
Q:
Define a <b>convex set</b> and a <b>convex function</b>.
A:
\(C\) is convex if \(\forall x,y\in C,\ 0\le\lambda\le1\): \(\lambda x+(1-\lambda)y\in C\) (the segment stays inside).
<br>\(f:C\to\mathbb{R}\) is convex if
\[ f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y). \]
E:
Geometrically: the chord between any two points lies on or above the graph. All norms are convex; balls are convex sets.

[QA]
Q:
State and explain the key optimization property of convexity.
A:
<b>Local = Global:</b> if \(D\) and \(f\) are convex, every local minimum of \(f\) is a <b>global</b> minimum.
E:
Why convexity matters: a local search can't get trapped in a bad local optimum. Proof is by contrapositive — if \(f(y)\lt f(x)\), points on the segment toward \(y\) (arbitrarily close to \(x\)) beat \(x\), so \(x\) isn't even a local min.

[QA]
Q:
What is a <b>Quadratic Program (QP)</b>?
A:
Minimize a quadratic-plus-linear cost subject to linear constraints:
\[ \min_x\ \tfrac12 x^\top Q x+qx \quad\text{s.t.}\quad A_{in}x\preceq b_{in},\ A_{eq}x=b_{eq},\ lb\preceq x\preceq ub, \]
with \(Q=Q^\top\succeq0\).
E:
If \(Q\succ0\) and the feasible set is nonempty, the solution <b>exists and is unique</b>. (\(\preceq\) means componentwise \(\le\).)

[QA]
Q:
What is a <b>Linear Program (LP)</b>?
A:
A QP with no quadratic term — a <b>linear</b> cost under linear constraints:
\[ \min_x\ f^\top x \quad\text{s.t.}\quad A_{in}x\preceq b_{in},\ A_{eq}x=b_{eq}. \]
E:
Flip a "\(\ge\)" constraint to "\(\le\)" by multiplying by \(-1\): \(\tilde A x\ge\tilde b\iff -\tilde A x\le-\tilde b\).

[QA]
Q:
How are \(\min\|Ax-b\|_1\) and \(\min\|Ax-b\|_\infty\) turned into LPs (slack variables)?
A:
<b>1-norm:</b> introduce \(s\in\mathbb{R}^m\), minimize \(\sum_i s_i\) s.t. \(-s\preceq b-Ax\preceq s\) (so \(s_i\ge|b-Ax|_i\)).
<br><b>∞-norm:</b> one scalar slack \(s\), minimize \(s\) s.t. \(-s\,\mathbf{1}\preceq b-Ax\preceq s\,\mathbf{1}\).
E:
Slack variables convert a nonsmooth (piecewise-linear) objective into a clean LP — clever and very practical.

[QA]
Q:
Why are LP and QP central to real-time robotics?
A:
They are <b>convex</b> (global optimum guaranteed) and fast enough to solve online with dedicated solvers (e.g. OSQP, quadprog). Robot tasks like computing ground-reaction forces or torques under actuator/contact constraints map naturally onto QPs.

[CLOZE]
C:
For convex \(D\) and \(f\), every {{c1::local}} minimum is also a {{c2::global}} minimum. A QP minimizes \(\tfrac12 x^\top Qx+qx\) with \(Q\succeq0\); minimizing \(\|Ax-b\|_1\) becomes an LP by adding {{c3::slack variables}} \(s\) with \(-s\preceq b-Ax\preceq s\).
