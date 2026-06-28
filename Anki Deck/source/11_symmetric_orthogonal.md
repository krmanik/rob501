=== 11 | Symmetric & Orthogonal Matrices ===

[QA]
Q:
For a real symmetric matrix \(A=A^\top\), what is special about its <b>eigenvalues</b>?
A:
They are all <b>real</b>. Hence the eigenvectors can be taken real (the null space of the real matrix \(A-\lambda I\) contains real vectors).
E:
Proof uses \(\langle Av,v\rangle=\langle v,Av\rangle\Rightarrow\lambda\|v\|^2=\bar\lambda\|v\|^2\Rightarrow\lambda=\bar\lambda\).

[QA]
Q:
For a real symmetric \(A\), how do eigenvectors of <b>distinct</b> eigenvalues relate?
A:
They are <b>orthogonal</b>. From \(\langle Av_1,v_2\rangle=\langle v_1,Av_2\rangle\):
\[ \lambda_1\langle v_1,v_2\rangle=\lambda_2\langle v_1,v_2\rangle\Rightarrow(\lambda_1-\lambda_2)\langle v_1,v_2\rangle=0, \]
and \(\lambda_1\ne\lambda_2\Rightarrow\langle v_1,v_2\rangle=0\).

[QA]
Q:
What basis property do real symmetric matrices always enjoy?
A:
Their eigenvectors can always be chosen to form an <b>orthonormal basis</b> of \(\mathbb{R}^n\) — even with repeated eigenvalues.
E:
This is false for general matrices: \(A=\begin{bmatrix}0&1\\0&0\end{bmatrix}\) has no basis of eigenvectors (defective).

[QA]
Q:
Define an <b>orthogonal matrix</b> \(Q\) and its key property.
A:
A real square \(Q\) with \(Q^\top Q=I\) — equivalently, its columns form an orthonormal basis of \(\mathbb{R}^n\). Then \(Q^{-1}=Q^\top\).

[QA]
Q:
Why are orthogonal matrices <b>norm-preserving</b>?
A:
For the Euclidean norm,
\[ \|Qx\|^2=(Qx)^\top(Qx)=x^\top Q^\top Q\,x=x^\top x=\|x\|^2. \]
So \(\|Qx\|=\|x\|\): orthogonal maps are rigid rotations/reflections.

[QA]
Q:
State the <b>Spectral Theorem</b> for real symmetric matrices.
A:
For any real symmetric \(A\) there exists an orthogonal \(Q\) with
\[ Q^\top A Q=\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n), \]
i.e. \(A=Q\Lambda Q^\top\). The columns of \(Q\) are orthonormal eigenvectors.
E:
Diagonalization by an <i>orthogonal</i> change of basis (no inverse needed beyond the transpose) — the cleanest possible diagonalization.

[CLOZE]
C:
Every real symmetric matrix factors as \(A=Q\Lambda Q^\top\) with \(Q\) {{c1::orthogonal}} (\(Q^\top Q=I\)) and \(\Lambda\) {{c2::diagonal}} holding the {{c3::real}} eigenvalues; the columns of \(Q\) are orthonormal eigenvectors.
