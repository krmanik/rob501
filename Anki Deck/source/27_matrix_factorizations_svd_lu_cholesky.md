=== 27 | Matrix Factorizations — SVD, LU & Cholesky ===

[QA]
Q:
Why is plain "linearly independent vs dependent" inadequate numerically, motivating the SVD?
A:
Independence is binary, but a determinant can be tiny (nearly dependent) or look large yet a small perturbation makes the set dependent. The SVD gives a <b>continuous</b> measure of how close to dependent a set is, via the smallest singular value.
E:
Example: \(\det\begin{bmatrix}1&10^4\\0&1\end{bmatrix}=1\), yet adding \(10^{-4}\) in one entry makes it singular.

[QA]
Q:
State the <b>Singular Value Decomposition</b> theorem.
A:
Every real \(n\times m\) matrix factors as
\[ A=U\Sigma V^\top, \]
with \(U\) (\(n\times n\)) and \(V\) (\(m\times m\)) orthogonal, \(\Sigma\) rectangular-diagonal with \(\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_p\ge0\), \(p=\min(n,m)\).

[QA]
Q:
Where do the SVD factors come from (eigenstructure)?
A:
Columns of \(V\) are orthonormal eigenvectors of \(A^\top A\); columns of \(U\) are eigenvectors of \(AA^\top\); and the singular values satisfy
\[ \sigma_i=\sqrt{\lambda_i},\qquad q_i=\tfrac{1}{\sigma_i}A v_i, \]
where \(\sigma_i^2\) are the (non-negative) eigenvalues shared by \(A^\top A\) and \(AA^\top\).
E:
\(A^\top A\) is symmetric PSD, so its eigenvalues are real and \(\ge0\) — guaranteeing real \(\sigma_i\ge0\).

[QA]
Q:
How does the SVD quantify <b>numerical rank</b>?
A:
The number of "significant" singular values (those above a tolerance) is the numerical rank; \(\sigma_{\min}\) measures the distance to the nearest rank-deficient matrix. Tiny \(\sigma_{\min}\) ⇒ nearly dependent columns.

[QA]
Q:
State the <b>LU factorization</b> and its use.
A:
A square matrix factors (possibly after row permutation \(P\)) as
\[ PA=LU, \]
\(L\) uni-lower-triangular, \(U\) upper-triangular. Then \(Ax=b\) is solved by forward substitution \(Ly=Pb\) then back substitution \(Ux=y\).
E:
Built by "peeling the onion": successively subtract \(C_k R_k\) (a column × row) to zero out a row and column at a time.

[QA]
Q:
State the <b>Cholesky / LDL\(^\top\)</b> factorization and when it exists.
A:
A real symmetric matrix \(M\) factors as
\[ M=LDL^\top, \]
\(L\) uni-lower-triangular, \(D\) diagonal. \(M\succ0\iff\) the factorization exists with all \(D_{ii}\gt0\); \(M\succeq0\) gives \(D_{ii}\ge0\).
E:
Taking \(D^{1/2}\) gives \(M=(LD^{1/2})(LD^{1/2})^\top=N^\top N\) — a triangular square root, the efficient PSD square root.

[CLOZE]
C:
SVD: \(A={{c1::U\Sigma V^\top}}\) with \(U,V\) orthogonal and singular values \(\sigma_i={{c2::\sqrt{\lambda_i}}}\) of \(A^\top A\). A symmetric positive-definite matrix has a Cholesky factorization \(M={{c3::LDL^\top}}\) with positive diagonal \(D\).
