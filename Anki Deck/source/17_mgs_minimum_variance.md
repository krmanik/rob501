=== 17 | Modified Gram-Schmidt & Minimum Variance Estimator ===

[QA]
Q:
What goes wrong with <b>classical</b> Gram–Schmidt numerically, and how does <b>Modified</b> GS fix it?
A:
In finite precision, classical GS subtracts all projections of the <i>original</i> \(y_k\) at once; rounding makes the \(v_i\) lose orthogonality. <b>Modified</b> GS subtracts each projection <b>sequentially</b>, updating \(v_k\) before computing the next coefficient — far better orthogonality.
E:
Mathematically identical in exact arithmetic; MGS is the numerically preferred way to build \(Q\) in a QR factorization.

[QA]
Q:
State the <b>Minimum Variance Estimator (MVE)</b> model and assumptions.
A:
\(y=Cx+\varepsilon\) with priors \(E\{x\}=0,\ E\{\varepsilon\}=0\), \(\operatorname{cov}(x)=P\), \(\operatorname{cov}(\varepsilon)=Q\), \(E\{\varepsilon x^\top\}=0\), and \(CPC^\top+Q\succ0\).
E:
Unlike BLUE, MVE uses a <b>prior</b> covariance \(P\) on \(x\); it can even handle \(\dim(y)\lt\dim(x)\).

[QA]
Q:
Give the <b>MVE</b> estimator in its two equivalent forms.
A:
\[ \hat x=Ky,\qquad K=PC^\top\big(CPC^\top+Q\big)^{-1}=\big(C^\top Q^{-1}C+P^{-1}\big)^{-1}C^\top Q^{-1}. \]
E:
The two forms are linked by the <b>Matrix Inversion Lemma</b>. The first needs only \(CPC^\top+Q\succ0\); the second needs \(P,Q\succ0\).

[QA]
Q:
What is the MVE <b>error covariance</b>, and how does the Schur complement appear?
A:
\[ \operatorname{cov}(\hat x-x)=P-PC^\top(CPC^\top+Q)^{-1}CP, \]
which is the <b>Schur complement</b> of \(\operatorname{cov}(x)\) in \(\operatorname{cov}\!\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}P&PC^\top\\CP&CPC^\top+Q\end{bmatrix}\).
E:
The term \(PC^\top(CPC^\top+Q)^{-1}CP\) is exactly the covariance reduction — the "value of the measurement."

[QA]
Q:
How are <b>BLUE and MVE</b> related?
A:
\[ \text{BLUE: }(C^\top Q^{-1}C)^{-1}C^\top Q^{-1}y,\qquad \text{MVE: }(C^\top Q^{-1}C+P^{-1})^{-1}C^\top Q^{-1}y. \]
They coincide when \(P^{-1}=0\) (infinite prior covariance — "no prior knowledge of \(x\)").
E:
MVE adds the prior-information term \(P^{-1}\). With a vague prior it reduces to the BLUE.

[QA]
Q:
State the <b>Matrix Inversion Lemma</b> (Woodbury) used to relate the MVE forms.
A:
If \(A,C,(C^{-1}+DA^{-1}B)\) are invertible,
\[ (A+BCD)^{-1}=A^{-1}-A^{-1}B\big(C^{-1}+DA^{-1}B\big)^{-1}DA^{-1}. \]
E:
With \(A=P^{-1},B=C^\top,C=Q^{-1},D=C\) it gives \((C^\top Q^{-1}C+P^{-1})^{-1}=P-PC^\top(Q+CPC^\top)^{-1}CP\).

[CLOZE]
C:
MVE: \(\hat x=PC^\top({{c1::CPC^\top+Q}})^{-1}y\); it equals BLUE when {{c2::\(P^{-1}=0\)}} (vague prior). Its error covariance is the {{c3::Schur complement}} of \(\operatorname{cov}(x)\) in \(\operatorname{cov}([x;y])\).
