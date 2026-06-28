=== 12 | Positive Semi-Definite Matrices & Schur Complement ===

[QA]
Q:
Define a <b>quadratic form</b>, and why may we always assume the matrix is symmetric?
A:
\(x^\top M x\) for \(x\in\mathbb{R}^n\). Only the symmetric part matters:
\[ x^\top M x=x^\top\Big(\tfrac{M+M^\top}{2}\Big)x, \]
since the skew part \(\tfrac{M-M^\top}{2}\) contributes \(x^\top W x=0\) for all \(x\).
E:
Any square \(M\) splits as symmetric \(\tfrac{M+M^\top}{2}\) plus skew-symmetric \(\tfrac{M-M^\top}{2}\).

[QA]
Q:
State the eigenvalue <b>bounds</b> of a quadratic form for symmetric \(M\).
A:
\[ \lambda_{\min}\,x^\top x \le x^\top M x \le \lambda_{\max}\,x^\top x \quad\forall x\in\mathbb{R}^n. \]
E:
Expand \(x\) in an orthonormal eigenbasis: \(x^\top M x=\sum_i\lambda_i\alpha_i^2\), bounded by \(\lambda_{\min}\sum\alpha_i^2\) and \(\lambda_{\max}\sum\alpha_i^2\).

[QA]
Q:
Define <b>positive definite</b> (\(P\succ0\)) and <b>positive semidefinite</b> (\(P\succeq0\)).
A:
\(P=P^\top\) and
<ul>
<li>\(P\succ0\): \(x^\top P x\gt0\) for all \(x\ne0\);</li>
<li>\(P\succeq0\): \(x^\top P x\ge0\) for all \(x\).</li>
</ul>
E:
<b>Warning:</b> \(P\succ0\) does <i>not</i> mean the entries are positive — e.g. \(\begin{bmatrix}2&-1\\-1&2\end{bmatrix}\succ0\).

[QA]
Q:
State the <b>eigenvalue test</b> for definiteness of a symmetric matrix.
A:
\[ P\succ0 \iff \text{all }\lambda_i\gt0,\qquad P\succeq0 \iff \text{all }\lambda_i\ge0. \]
E:
Follows from \(\lambda_{\min}x^\top x\le x^\top Px\): the sign of the smallest eigenvalue controls definiteness.

[QA]
Q:
Why are \(A^\top A\) and \(AA^\top\) always positive <b>semidefinite</b>?
A:
They are symmetric, and for \(A^\top A\): \(x^\top A^\top A x=\|Ax\|^2\ge0\). Hence all eigenvalues are \(\ge0\).
E:
This is why Gram matrices \(A^\top A\) are \(\succeq0\), and \(\succ0\) exactly when \(A\) has full column rank.

[QA]
Q:
State the matrix <b>square-root</b> characterization of PSD.
A:
\[ P\succeq0 \iff \exists N\ \text{with}\ N^\top N=P. \]
E:
\((\Leftarrow)\) \(x^\top P x=\|Nx\|^2\ge0\). \((\Rightarrow)\) write \(P=O^\top\Lambda O\), set \(N=\Lambda^{1/2}O\) with \(\Lambda^{1/2}=\operatorname{diag}(\sqrt{\lambda_i})\).

[QA]
Q:
State the <b>Schur Complement</b> theorem for \(M=\begin{bmatrix}A&B\\B^\top&C\end{bmatrix}\) (symmetric, \(A\) and \(C\) symmetric).
A:
The following are equivalent:
<ul>
<li>\(M\succ0\);</li>
<li>\(A\succ0\) and \(C-B^\top A^{-1}B\succ0\);</li>
<li>\(C\succ0\) and \(A-BC^{-1}B^\top\succ0\).</li>
</ul>
E:
\(C-B^\top A^{-1}B\) is the <b>Schur complement</b> of \(A\). It reduces definiteness of a block matrix to two smaller tests — central to covariance/Kalman algebra.

[CLOZE]
C:
For symmetric \(P\): \(P\succ0\) iff all eigenvalues are {{c1::strictly positive}}; \(P\succeq0\) iff \(\exists N\) with {{c2::\(N^\top N=P\)}}. The block matrix \(\begin{bmatrix}A&B\\B^\top&C\end{bmatrix}\succ0\) iff \(A\succ0\) and the Schur complement {{c3::\(C-B^\top A^{-1}B\succ0\)}}.
