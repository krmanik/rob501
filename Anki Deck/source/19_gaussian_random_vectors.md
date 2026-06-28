=== 19 | Gaussian Random Vectors ===

[QA]
Q:
Give the <b>multivariate normal</b> density of \(X\sim N(\mu,\Sigma)\), \(\Sigma\succ0\).
A:
\[ f_X(x)=\frac{1}{\sqrt{(2\pi)^p|\Sigma|}}\,\exp\!\Big(-\tfrac12 (x-\mu)^\top\Sigma^{-1}(x-\mu)\Big), \]
with \(\mu=E\{X\}\in\mathbb{R}^p\), \(\Sigma=\operatorname{cov}(X)\), \(|\Sigma|=\det\Sigma\ne0\) ("non-degenerate").

[QA]
Q:
What are the <b>marginals</b> of a Gaussian vector?
A:
Each component (or sub-block) is again Gaussian, read straight off \(\mu\) and \(\Sigma\): \(X_i\sim N(\mu_i,\Sigma_{ii})\). No integration needed.
E:
The univariate density depends only on \(\mu_i\) and \(\sigma_i^2=\Sigma_{ii}\), which you already have.

[QA]
Q:
For Gaussians, how do <b>uncorrelated</b> and <b>independent</b> relate?
A:
They are <b>equivalent</b>: \(X_i,X_j\) jointly Gaussian are independent \(\iff\Sigma_{ij}=0\). (This equivalence is special to Gaussians.)

[QA]
Q:
What is the distribution of a <b>linear transform</b> \(Y=AX+b\) of a Gaussian \(X\sim N(\mu,\Sigma)\)?
A:
\(Y\) is Gaussian with
\[ E\{Y\}=A\mu+b,\qquad \operatorname{cov}(Y)=A\Sigma A^\top. \]
E:
\(A\Sigma A^\top\succ0\) when \(A\) has full row rank and \(\Sigma\succ0\). Picking \(A\) as a selector row recovers the marginals.

[QA]
Q:
State <b>Key Fact 1</b>: the conditional distribution of jointly Gaussian \(X_1\mid X_2=x_2\).
A:
It is Gaussian \(N(\mu_{1|2},\Sigma_{1|2})\) with
\[ \mu_{1|2}=\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),\qquad \Sigma_{1|2}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}. \]
E:
The <b>mean</b> shifts with the observed \(x_2\); the <b>covariance</b> does not depend on \(x_2\). \(\Sigma_{1|2}\) is the Schur complement of \(\Sigma_{22}\).

[QA]
Q:
Interpret the conditioning update \(\Sigma_{1|2}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\).
A:
The term \(\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\) is the uncertainty <b>removed</b> by observing \(X_2\) — the "value of the information." If \(X_1,X_2\) are uncorrelated it is \(0\) (knowing \(X_2\) tells you nothing); as \(\Sigma_{22}\to\infty\) it also vanishes.
E:
This is exactly the algebra behind the Kalman measurement update — conditioning a Gaussian state on a new measurement.

[QA]
Q:
What does <b>conditional independence</b> of Gaussians look like in \(\Sigma\)?
A:
If \(X_1,X_3\) are each independent of \(X_2\) (so \(\Sigma_{12}=\Sigma_{23}=0\)), then \(X_1\mid X_3\) and \(X_2\mid X_3\) are independent. The cross-blocks with \(X_2\) are zero in \(\Sigma\).

[CLOZE]
C:
For jointly Gaussian vectors, \(X_1\mid X_2=x_2\) is normal with mean {{c1::\(\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2)\)}} and covariance {{c2::\(\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\)}}; the covariance is {{c3::independent of \(x_2\)}}. This is the heart of the Kalman update.
