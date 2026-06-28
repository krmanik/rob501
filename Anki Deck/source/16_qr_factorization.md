=== 16 | QR Factorization ===

[QA]
Q:
State the <b>QR factorization</b> theorem for \(A\) (\(n\times m\), \(n\ge m\), independent columns).
A:
\[ A=QR, \]
where \(Q\) is \(n\times m\) with orthonormal columns (\(Q^\top Q=I_m\)) and \(R\) is \(m\times m\) upper triangular. The columns of \(A\) are independent \(\iff R\) is invertible.

[QA]
Q:
How is QR computed, and what are the entries of \(R\)?
A:
By <b>Gram–Schmidt with normalization</b> on the columns of \(A\). The \(i\)-th column of \(Q\) is the \(i\)-th orthonormalized vector \(v_i\), and
\[ R_{ij}=\langle A_j,v_i\rangle\quad(i\le j),\qquad R_{ij}=0\ (i\gt j). \]
E:
\(R_i=[A_i]_{\{v_1,\dots,v_m\}}\) — the \(i\)-th column of \(R\) is the representation of \(A_i\) in the orthonormal basis. No extra work beyond Gram–Schmidt.

[QA]
Q:
How does QR turn the normal equations into back-substitution for \(\min_x\|Ax-b\|_2\)?
A:
With \(A=QR\), \(Q^\top Q=I\):
\[ A^\top A\hat x=A^\top b \;\Rightarrow\; R^\top R\hat x=R^\top Q^\top b \;\Rightarrow\; R\hat x=Q^\top b. \]
Since \(R\) is upper triangular and invertible, solve \(\hat x\) by <b>back-substitution</b> — no matrix inverse.
E:
QR is more numerically stable than forming \(A^\top A\) (which squares the condition number).

[QA]
Q:
How does QR solve the <b>minimum-norm</b> solution of an underdetermined \(Ax=b\) (independent rows)?
A:
Factor \(A^\top=QR\). The minimum-norm solution \(\hat x=A^\top(AA^\top)^{-1}b\) simplifies to
\[ \hat x=Q(R^\top)^{-1}b, \]
again avoiding an explicit inverse of \(AA^\top\).

[CLOZE]
C:
QR writes \(A=QR\) with \(Q\) having {{c1::orthonormal columns}} (\(Q^\top Q=I\)) and \(R\) {{c2::upper triangular}}; it is computed by {{c3::Gram–Schmidt}}, and least squares reduces to \(R\hat x=Q^\top b\) solved by back-substitution.
