=== 09 | Projection Theorem & Gram-Schmidt ===

[QA]
Q:
State the <b>Gram–Schmidt recursion step</b>.
A:
Given a linearly independent set \(\{y_1,\dots,y_k\}\) and an orthogonal set \(\{v_1,\dots,v_{k-1}\}\) with the same span as \(\{y_1,\dots,y_{k-1}\}\), define
\[ v_k = y_k - \sum_{j=1}^{k-1}\frac{\langle y_k,v_j\rangle}{\|v_j\|^2}\,v_j. \]
Then \(\{v_1,\dots,v_k\}\) is orthogonal and spans \(\{y_1,\dots,y_k\}\).
E:
Subtract from \(y_k\) its components along the already-built orthogonal directions. Divide each \(v_j\) by \(\|v_j\|\) for an orthonormal set.

[QA]
Q:
Why is the new vector \(v_k\) in Gram–Schmidt never zero?
A:
Because \(\operatorname{span}\{v_1,\dots,v_{k-1}\}=\operatorname{span}\{y_1,\dots,y_{k-1}\}\) and \(y_k\) is linearly independent of \(\{y_1,\dots,y_{k-1}\}\). If \(v_k=0\), then \(y_k\) would lie in that span — contradiction.

[QA]
Q:
Define the <b>orthogonal complement</b> \(S^\perp\) and a key fact about it.
A:
\[ S^\perp:=\{x\in X:\langle x,y\rangle=0\ \forall y\in S\}. \]
\(S^\perp\) is always a <b>subspace</b> (even if \(S\) is not). For \(M=\operatorname{span}\{y_1,\dots,y_k\}\), \(x\in M^\perp\iff\langle x,y_i\rangle=0\) for all \(i\).

[QA]
Q:
State the orthogonal-decomposition result \(X=M\oplus M^\perp\) and what \(\oplus\) means.
A:
For a finite-dimensional inner product space and subspace \(M\), every \(x\) splits <b>uniquely</b> as \(x=m+m^\perp\) with \(m\in M,\ m^\perp\in M^\perp\). The "\(\oplus\)" (direct sum) means \(M\cap M^\perp=\{0\}\), which forces uniqueness.
E:
Proof: \(x\in M\cap M^\perp\Rightarrow\langle x,x\rangle=0\Rightarrow x=0\). Apply Gram–Schmidt to a basis of \(X\) extending a basis of \(M\); then \(M^\perp=\operatorname{span}\{v_{k+1},\dots,v_n\}\).

[QA]
Q:
State the <b>Classical Projection Theorem</b>.
A:
Let \(M\) be a subspace of a finite-dimensional real inner product space \(X\). For every \(x\in X\) there is a <b>unique</b> \(\hat x\in M\) with
\[ \|x-\hat x\|=\min_{m\in M}\|x-m\|=d(x,M), \]
and \(\hat x\) is characterized by the <b>orthogonality condition</b>
\[ (x-\hat x)\perp M. \]
E:
"The best approximation is the foot of the perpendicular." Existence + uniqueness come from \(X=M\oplus M^\perp\).

[QA]
Q:
Why does the orthogonality condition \((x-\hat x)\perp M\) imply \(\hat x\) is the minimizer?
A:
For any \(m\in M\), \(x-\hat x\perp(\hat x-m)\in M\), so by Pythagoras
\[ \|x-m\|^2=\|x-\hat x\|^2+\|\hat x-m\|^2\ge\|x-\hat x\|^2, \]
with equality only when \(m=\hat x\). \(\blacksquare\)

[CLOZE]
C:
The Projection Theorem: the best approximation \(\hat x\) of \(x\) in subspace \(M\) is the unique point such that {{c1::\((x-\hat x)\perp M\)}}. Existence and uniqueness rely on the decomposition {{c2::\(X=M\oplus M^\perp\)}}.
