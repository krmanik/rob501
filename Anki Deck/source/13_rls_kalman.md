=== 13 | Recursive Least Squares & Kalman Filter ===

[QA]
Q:
What problem does <b>Recursive Least Squares (RLS)</b> solve, and why recursively?
A:
For the streaming model \(y_i=C_i x+e_i\) it computes the weighted least-squares estimate
\[ \hat x_k=\arg\min_{x}\sum_{i=1}^k (y_i-C_i x)^\top S_i (y_i-C_i x) \]
<b>without</b> recomputing a batch solution each step. As each new \(y_{k+1}\) arrives, the old estimate is corrected — \(O(1)\) work per sample instead of inverting a growing matrix.

[QA]
Q:
Write the <b>RLS update</b> equations.
A:
\[ \hat x_{k+1}=\hat x_k+\underbrace{P_{k+1}C_{k+1}^\top S_{k+1}}_{\text{gain}}\underbrace{(y_{k+1}-C_{k+1}\hat x_k)}_{\text{innovation}}, \]
\[ P_{k+1}=P_k-P_k C_{k+1}^\top\big(C_{k+1}P_k C_{k+1}^\top+S_{k+1}^{-1}\big)^{-1}C_{k+1}P_k. \]
E:
"New estimate = old estimate + gain × (measured − predicted)." \(P_k=(\sum_{i\le k}C_i^\top S_i C_i)^{-1}\) is the running inverse Gram matrix; it shrinks as data accumulates.

[QA]
Q:
What initializes RLS, and what is \(k_0\)?
A:
\(k_0\) is the smallest \(k\) with \(\operatorname{rank}[C_1^\top\cdots C_k^\top]=n\) (enough measurements to identify \(x\)). Then
\[ P_{k_0}=\Big(\sum_{i=1}^{k_0}C_i^\top S_i C_i\Big)^{-1}. \]

[QA]
Q:
State the discrete-time <b>Kalman filter model</b> and assumptions.
A:
\[ x_{k+1}=A_k x_k+G_k w_k,\qquad y_k=C_k x_k+v_k, \]
with \(w_k\sim N(0,R_k)\), \(v_k\sim N(0,Q_k)\) white, mutually independent and independent of \(x_0\sim N(\bar x_0,P_0)\).
E:
\(w_k\) = process noise, \(v_k\) = measurement noise. "White" = flat power spectral density (uncorrelated across time).

[QA]
Q:
Give the Kalman filter <b>measurement-update</b> (correction) equations.
A:
\[ K_k=P_{k|k-1}C_k^\top\big(C_k P_{k|k-1}C_k^\top+Q_k\big)^{-1}, \]
\[ \hat x_{k|k}=\hat x_{k|k-1}+K_k\big(y_k-C_k\hat x_{k|k-1}\big),\qquad P_{k|k}=P_{k|k-1}-K_k C_k P_{k|k-1}. \]
E:
\(K_k\) is the Kalman gain; \(y_k-C_k\hat x_{k|k-1}\) the innovation. Conditioning on \(y_k\) reduces the covariance.

[QA]
Q:
Give the Kalman filter <b>time-update</b> (prediction) equations.
A:
\[ \hat x_{k+1|k}=A_k\hat x_{k|k},\qquad P_{k+1|k}=A_k P_{k|k}A_k^\top+G_k R_k G_k^\top. \]
E:
Push the estimate through the dynamics; the model/process noise \(G_k R_k G_k^\top\) <i>inflates</i> the covariance.

[QA]
Q:
In one sentence, what <b>is</b> the Kalman filter conceptually?
A:
A <b>recursive Minimum Variance Estimator</b> for a linear-Gaussian state-space model: it propagates the conditional mean \(\hat x_{k|k}=E\{x_k\mid y_0,\dots,y_k\}\) and covariance \(P_{k|k}\) by alternating predict and update steps.
E:
Same idea as RLS (recursive WLS), but it estimates an <i>evolving</i> state \(x_k\), not a fixed constant.

[CLOZE]
C:
Kalman gain \(K_k={{c1::P_{k|k-1}C_k^\top(C_k P_{k|k-1}C_k^\top+Q_k)^{-1}}}\); update \(\hat x_{k|k}=\hat x_{k|k-1}+K_k(y_k-{{c2::C_k\hat x_{k|k-1}}})\); predict covariance \(P_{k+1|k}={{c3::A_k P_{k|k}A_k^\top+G_k R_k G_k^\top}}\).
