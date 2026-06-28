=== 14 | Least Squares & Probability ===

[QA]
Q:
Why move from deterministic least squares to a <b>probabilistic</b> view of estimation?
A:
Measurements carry noise. Modeling the error \(\varepsilon\) as a random vector lets us (i) justify <i>which</i> norm/weights to use, (ii) quantify the <b>uncertainty</b> of the estimate via its error covariance, and (iii) fuse measurements optimally.

[QA]
Q:
Define <b>mean</b>, <b>covariance</b>, and <b>correlation</b> of random vectors.
A:
\[ \mu=E\{X\},\qquad \Sigma=\operatorname{cov}(X)=E\{(X-\mu)(X-\mu)^\top\}, \]
\[ \operatorname{cov}(X_1,X_2)=E\{(X_1-\mu_1)(X_2-\mu_2)^\top\}=\Sigma_{12}=\Sigma_{21}^\top. \]
E:
\(\Sigma\) is symmetric positive semidefinite; diagonal entries are variances \(\Sigma_{ii}=\sigma_i^2\).

[QA]
Q:
What is the elegant <b>inner product on random variables</b> used for minimum-variance estimation?
A:
On zero-mean random variables, define
\[ \langle z_1,z_2\rangle:=E\{z_1 z_2\}. \]
Then \(\langle z,z\rangle=\operatorname{var}(z)\), so "minimize variance" becomes "minimize norm" — and the Projection Theorem applies directly.
E:
This recasts estimation as best approximation in an inner-product space whose "vectors" are random variables (functions on \(\Omega\)).

[QA]
Q:
How does the choice of weight matrix \(W\) in weighted least squares relate to noise statistics?
A:
Solving \(\min(A\alpha-b)^\top W(A\alpha-b)\) implicitly assumes the measurement noise is zero-mean with covariance
\[ Q=W^{-1}. \]
The optimal choice is \(W=Q^{-1}\), the <b>information matrix</b>.
E:
Large variance (uncertain measurement) ⇒ small weight. "Low information when the covariance is large."

[QA]
Q:
What does <b>uncorrelated</b> mean, and does it imply independence?
A:
\(X_1,X_2\) are uncorrelated if \(\operatorname{cov}(X_1,X_2)=0\). Uncorrelated does <b>not</b> imply independent in general — <i>except</i> for jointly Gaussian random vectors, where the two coincide.

[QA]
Q:
For a linear estimator \(\hat x=Ky\) of \(x\) from \(y=Cx+\varepsilon\), what is the <b>error covariance</b> when \(KC=I\)?
A:
Then \(\hat x-x=K\varepsilon\), so
\[ \operatorname{cov}(\hat x-x)=E\{K\varepsilon\varepsilon^\top K^\top\}=KQK^\top. \]
E:
Unbiasedness needs \(KC=I\); minimizing \(\operatorname{tr}(KQK^\top)\) subject to \(KC=I\) yields BLUE.

[CLOZE]
C:
On zero-mean random variables, \(\langle z_1,z_2\rangle=E\{z_1z_2\}\) makes \(\langle z,z\rangle={{c1::\operatorname{var}(z)}}\). A weighted least-squares weight \(W\) corresponds to assuming noise covariance \(Q={{c2::W^{-1}}}\), so the optimal weight is the {{c3::information matrix}} \(Q^{-1}\).
