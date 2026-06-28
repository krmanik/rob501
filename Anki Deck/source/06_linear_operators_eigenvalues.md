=== 06 | Linear Operators & Eigenvalues ===

[QA]
Q:
Define a <b>linear operator</b> \(L:X\to Y\).
A:
A map satisfying, for all \(x,z\in X\) and \(\alpha,\beta\in\mathbb{F}\),
\[ L(\alpha x+\beta z)=\alpha L(x)+\beta L(z). \]
E:
Examples: \(L(x)=Ax\) for a matrix \(A\); differentiation \(L(p)=\tfrac{d}{dt}p\) on polynomials; integration. Linearity is what lets a finite matrix capture the whole map.

[QA]
Q:
Define the <b>matrix representation</b> \(A\) of \(L:X\to Y\) relative to bases \(u\) (for \(X\)) and \(v\) (for \(Y\)).
A:
The \(n\times m\) matrix \(A\) with
\[ [L(x)]_v = A\,[x]_u \quad\forall x\in X. \]

[QA]
Q:
How do you <b>build</b> the matrix representation column by column?
A:
The \(i\)-th column is the representation of where the \(i\)-th input basis vector goes:
\[ A_i=[\,L(u^i)\,]_v,\qquad i=1,\dots,m. \]
E:
"Feed in each input basis vector, write the output in the output basis, stack as columns."

[QA]
Q:
Find the matrix of \(L(p)=\tfrac{d}{dt}p\) on \(\mathcal{P}_3=\{\deg\le3\}\) with basis \(\{1,t,t^2,t^3\}\).
A:
Columns are \([L(1)],[L(t)],[L(t^2)],[L(t^3)]=[0],[1],[2t],[3t^2]\):
\[ A=\begin{bmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\\0&0&0&0\end{bmatrix}. \]
E:
\(A\) is nilpotent (\(A^4=0\)) — matching the fact that the 4th derivative of a cubic is zero.

[QA]
Q:
Define <b>eigenvalue</b> and <b>eigenvector</b> of a square matrix / operator \(A\).
A:
A scalar \(\lambda\) and nonzero vector \(v\) with
\[ Av=\lambda v. \]
\(\lambda\) is an eigenvalue, \(v\) a corresponding eigenvector. The \(v\ne0\) requirement is essential.

[QA]
Q:
How are eigenvalues found via the <b>characteristic polynomial</b>?
A:
\(Av=\lambda v\iff (A-\lambda I)v=0\) has a nonzero solution \(\iff A-\lambda I\) is singular:
\[ \det(A-\lambda I)=0. \]
The roots are the eigenvalues; for each, the null space of \(A-\lambda I\) gives the eigenvectors.

[QA]
Q:
When is \(A\) (\(n\times n\)) <b>diagonalizable</b>, and what is the form?
A:
\(A\) is diagonalizable iff it has \(n\) linearly independent eigenvectors. Stacking them as columns of \(V\),
\[ A V = V\Lambda \;\Longrightarrow\; A = V\Lambda V^{-1},\quad \Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n). \]
E:
Diagonalization is a <b>change of basis</b> into eigen-coordinates where \(A\) acts as independent scalings. \(A^k=V\Lambda^k V^{-1}\) then makes powers trivial.

[QA]
Q:
Give a sufficient condition for diagonalizability over \(\mathbb{C}\).
A:
If the \(n\times n\) matrix has \(n\) <b>distinct</b> eigenvalues, their eigenvectors are automatically linearly independent, so \(A\) is diagonalizable.
E:
Distinct eigenvalues is sufficient, not necessary — e.g. \(I\) has a single repeated eigenvalue yet is (already) diagonal.

[CLOZE]
C:
\(\lambda\) is an eigenvalue of \(A\) iff {{c1::\(\det(A-\lambda I)=0\)}}. An \(n\times n\) matrix is diagonalizable iff it has {{c2::\(n\) linearly independent eigenvectors}}, giving \(A=V\Lambda V^{-1}\).
