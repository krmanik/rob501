=== 22 | Newton-Raphson Algorithm ===

[QA]
Q:
What problem does <b>Newton–Raphson</b> solve, and what is the core idea?
A:
Finding a root \(f(x^\ast)=0\) of a \(C^1\) map \(f:\mathbb{R}^n\to\mathbb{R}^n\) (the nonlinear analogue of solving \(Ax-b=0\)). Idea: <b>linearize</b> \(f\) about the current iterate and solve the linear approximation for the next iterate.
E:
\(f(x)\approx f(x_k)+\frac{\partial f(x_k)}{\partial x}(x-x_k)\); set the RHS to \(0\) and solve.

[QA]
Q:
Write the <b>standard form</b> of the Newton–Raphson iteration.
A:
\[ x_{k+1}=x_k-\Big(\frac{\partial f(x_k)}{\partial x}\Big)^{-1} f(x_k), \]
valid when the Jacobian \(\frac{\partial f(x_k)}{\partial x}\) is invertible.

[QA]
Q:
Give the <b>two-step (solve-then-update)</b> form and why it is preferred.
A:
\[ \frac{\partial f(x_k)}{\partial x}\,\Delta x_k=-f(x_k),\qquad x_{k+1}=x_k+\Delta x_k. \]
Solve the linear system for \(\Delta x_k\) via <b>LU or QR</b> rather than forming the Jacobian inverse — faster and more stable for large \(n\).

[QA]
Q:
What is the <b>damped</b> Newton–Raphson iteration, and why use it?
A:
\[ x_{k+1}=x_k+\epsilon\,\Delta x_k,\qquad \epsilon\gt0. \]
A step size \(\epsilon\lt1\) shortens the update to improve global behavior when the full Newton step would overshoot.

[QA]
Q:
On what three conditions does the validity of Newton–Raphson rest?
A:
<ul>
<li>\(f\) is differentiable;</li>
<li>the Jacobian \(\frac{\partial f}{\partial x}\) has nonzero determinant at the iterates;</li>
<li>the linearization is a good local approximation to \(f\).</li>
</ul>
E:
These give only <b>local</b> convergence — a good enough starting point is required.

[QA]
Q:
How is Newton–Raphson's local convergence proved rigorously?
A:
Show the map
\[ T(x)=x-\epsilon\Big(\tfrac{\partial f}{\partial x}(x)\Big)^{-1}(f(x)-y) \]
is a <b>contraction</b> on a closed ball (using a Lipschitz bound on the Jacobian). Its unique fixed point \(x^\ast=T(x^\ast)\) satisfies \(f(x^\ast)=y\).
E:
This ties Newton–Raphson to the Contraction Mapping Theorem: the iteration \(x_{k+1}=T(x_k)\) converges to the root.

[CLOZE]
C:
Newton–Raphson: \(x_{k+1}=x_k-{{c1::(\partial f/\partial x)^{-1}}}f(x_k)\). In practice solve {{c2::\((\partial f/\partial x)\Delta x_k=-f(x_k)\)}} by LU/QR. Its local convergence follows because the update map is a {{c3::contraction}}.
