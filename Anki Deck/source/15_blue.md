=== 15 | Best Linear Unbiased Estimator (BLUE) ===

[QA]
Q:
State the <b>BLUE</b> setup and what "best", "linear", "unbiased" each mean.
A:
Model \(y=Cx+\varepsilon\), \(E\{\varepsilon\}=0\), \(\operatorname{cov}(\varepsilon)=Q\succ0\), \(\operatorname{rank}(C)=n\).
<ul>
<li><b>Linear:</b> \(\hat x=Ky\).</li>
<li><b>Unbiased:</b> \(E\{\hat x\}=x\), i.e. \(KC=I\).</li>
<li><b>Best:</b> minimize the error variance \(E\{(\hat x-x)^\top(\hat x-x)\}=\operatorname{tr}(KQK^\top)\).</li>
</ul>

[QA]
Q:
Give the <b>BLUE</b> estimator and its error covariance.
A:
\[ \hat x=\hat K y,\qquad \hat K=\big(C^\top Q^{-1}C\big)^{-1}C^\top Q^{-1}, \]
\[ \operatorname{cov}(\hat x-x)=\big(C^\top Q^{-1}C\big)^{-1}. \]

[QA]
Q:
How is BLUE related to <b>weighted least squares</b>?
A:
They are <b>identical</b> when the WLS weight is the inverse noise covariance, \(W=Q^{-1}\). So BLUE = WLS with the information matrix as weight.
E:
Interpretation: weight each measurement by how much you trust it (inverse variance).

[QA]
Q:
Why does BLUE require \(\dim(y)\ge\dim(x)\) and \(\operatorname{rank}(C)=n\)?
A:
Unbiasedness needs \(KC=I_n\), solvable only if \(C\) has full column rank \(n\), which forces \(m=\dim(y)\ge n=\dim(x)\). Otherwise \(C^\top Q^{-1}C\) is singular and no unbiased linear estimator exists.
E:
The underdetermined optimization \(\min_{C^\top k_i^\top=e_i} k_i Q k_i^\top\) is solved row-by-row using the minimum-norm solution.

[QA]
Q:
Interpret the BLUE error covariance \((C^\top Q^{-1}C)^{-1}\).
A:
\(C^\top Q^{-1}C\) is the <b>Fisher information</b>: more/cleaner measurements (small \(Q\)) ⇒ larger information ⇒ smaller error covariance. Inverting it gives the achievable uncertainty of the best linear unbiased estimate.

[CLOZE]
C:
BLUE: \(\hat K={{c1::(C^\top Q^{-1}C)^{-1}C^\top Q^{-1}}}\) with error covariance {{c2::\((C^\top Q^{-1}C)^{-1}\)}}; it equals weighted least squares with weight \(W={{c3::Q^{-1}}}\).
