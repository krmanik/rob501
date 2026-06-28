=== 10 | Normal Equations & Least Squares ===

[QA]
Q:
Starting from the Projection Theorem, derive the <b>Normal Equations</b> for \(\hat x=\sum_{j}\alpha_j y_j\in M=\operatorname{span}\{y_1,\dots,y_k\}\).
A:
Orthogonality \((x-\hat x)\perp y_i\) for all \(i\) gives \(\langle\hat x,y_i\rangle=\langle x,y_i\rangle\), i.e.
\[ \sum_{j=1}^k \alpha_j\langle y_j,y_i\rangle=\langle x,y_i\rangle,\quad i=1,\dots,k. \]

[QA]
Q:
Write the Normal Equations in matrix form (define the <b>Gram matrix</b>).
A:
\[ G\,\alpha=\beta,\qquad G_{ij}=\langle y_i,y_j\rangle,\quad \beta_i=\langle x,y_i\rangle. \]
Over \(\mathbb{R}\), \(G=G^\top\) is symmetric, and \(\hat x=\sum_j\alpha_j y_j\) is the best approximation of \(x\) in \(M\).
E:
"What changes in each application is the inner product." Choose the inner product to match the problem (e.g. weighted).

[QA]
Q:
When is the Gram matrix \(G\) <b>invertible</b>?
A:
\[ \det G\ne0 \iff \{y_1,\dots,y_k\}\ \text{linearly independent}. \]
E:
\(G\alpha=0\Rightarrow\sum\alpha_j y_j\in M\cap M^\perp=\{0\}\Rightarrow\sum\alpha_j y_j=0\Rightarrow\alpha=0\) by independence. So independence ⇔ trivial null space ⇔ invertible.

[QA]
Q:
What does it mean for \(Ax=b\) to be <b>overdetermined</b>, and when is there still an exact solution?
A:
Roughly, \(A\) has more rows than columns. Usually no \(x\) gives \(Ax=b\); an exact solution exists iff \(b\in\operatorname{col\,span}(A)\). With independent columns, overdetermined \(\iff b\notin\operatorname{col\,span}(A)\).
E:
When there's no exact solution, seek the <b>best approximate solution</b> \(\hat x=\arg\min_x\|Ax-b\|\).

[QA]
Q:
Give the closed-form <b>least-squares</b> solution of \(\min_\alpha\|A\alpha-b\|_2\) for \(A\) (\(n\times m\), \(n\ge m\)) of full column rank.
A:
\[ \hat\alpha=(A^\top A)^{-1}A^\top b. \]
E:
This is exactly the Normal Equations \(A^\top A\,\alpha=A^\top b\) with the Euclidean inner product. \(A^\top A\) is the Gram matrix of the columns of \(A\); full column rank makes it invertible. \(A^{+}=(A^\top A)^{-1}A^\top\) is the (left) pseudoinverse.

[QA]
Q:
Give the <b>weighted</b> least-squares solution of \(\min_\alpha (A\alpha-b)^\top S (A\alpha-b)\), \(S\succ0\).
A:
\[ \hat\alpha=(A^\top S A)^{-1}A^\top S\,b. \]
E:
Uses the weighted inner product \(\langle u,v\rangle_S=u^\top S v\). Larger weights = more trust in those measurements. \(A^\top S A\) is the corresponding Gram matrix.

[CLOZE]
C:
Ordinary least squares solves the normal equations \(A^\top A\,\hat\alpha = {{c1::A^\top b}}\), giving \(\hat\alpha={{c2::(A^\top A)^{-1}A^\top b}}\), which requires \(A\) to have {{c3::full column rank}}.
