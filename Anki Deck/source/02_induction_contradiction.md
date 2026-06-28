=== 02 | Induction, Fundamental Theorem & Contradiction ===

[QA]
Q:
State the <b>First Principle of Induction</b> (standard / weak induction).
A:
Let \(P(n)\) be a statement about the natural numbers such that
<br><b>(a) Base case:</b> \(P(1)\) is true;
<br><b>(b) Inductive step:</b> for every \(k\), \(P(k)\Rightarrow P(k+1)\).
<br>Then \(P(n)\) is true for all \(n\ge 1\).
E:
If the base case starts at some \(k_0\ne1\), either re-index, or use \(P(k)\Rightarrow P(k+1)\) for \(k\ge k_0\) to conclude \(P(n)\) for all \(n\ge k_0\).

[QA]
Q:
What are the three <b>steps</b> of a proof by induction?
A:
<ol>
<li><b>Step 0:</b> write down \(P(k)\) precisely.</li>
<li><b>Step 1:</b> verify the <b>base case</b> \(P(1)\).</li>
<li><b>Step 2:</b> assume \(P(k)\) and prove \(P(k+1)\) — usually by rewriting \(P(k+1)\) so the terms of \(P(k)\) reappear.</li>
</ol>

[QA]
Q:
Prove by induction: \(1+3+5+\cdots+(2n-1)=n^2\) for all \(n\ge1\).
A:
<b>Base:</b> \(P(1)\): \(1=1^2\). ✓
<br><b>Step:</b> assume \(1+3+\cdots+(2k-1)=k^2\). Then
\[ \underbrace{1+\cdots+(2k-1)}_{k^2}+(2(k+1)-1) = k^2+2k+1 = (k+1)^2. \]
So \(P(k+1)\) holds; by induction the formula is true for all \(n\ge1\). \(\blacksquare\)

[QA]
Q:
Why must the inductive step \(P(k)\Rightarrow P(k+1)\) work <b>for every</b> \(k\), including the base?
A:
If the step fails for even one \(k\) (e.g. \(P(1)\Rightarrow P(2)\)), the chain breaks. The classic "all horses are the same color" fallacy hides exactly such a broken \(P(1)\Rightarrow P(2)\) step.
E:
Moral: don't quietly start the inductive step at \(k=2\) to dodge a failure at \(k=1\).

[QA]
Q:
State the <b>Second Principle of Induction</b> (strong induction). How does it differ from weak induction?
A:
<b>(a) Base:</b> \(P(1)\) true. <b>(b) Step:</b> if \(P(j)\) is true for <i>all</i> \(1\le j\le k\), then \(P(k+1)\) is true. Then \(P(n)\) holds for all \(n\ge1\).
<br>Difference: in the step you may use <b>all</b> prior statements \(P(1),\dots,P(k)\), not just \(P(k)\).
E:
Use strong induction when proving \(P(k+1)\) needs to "reach back" to some \(P(j)\) with \(j\lt k\) — as in the Fundamental Theorem of Arithmetic.

[QA]
Q:
Are strong and weak induction <b>equivalent</b> in power?
A:
<b>Yes.</b> Strong induction on \(P\) is exactly ordinary induction on the accumulated statement
\[ Q(k) := P(1)\wedge P(2)\wedge\cdots\wedge P(k). \]
Neither proves more theorems; strong induction is just sometimes more convenient.
E:
Key step: \(\big(P(1)\wedge\cdots\wedge P(k)\big)\Rightarrow P(k+1)\) is equivalent to \(Q(k)\Rightarrow Q(k+1)\).

[QA]
Q:
Define <b>prime</b> and <b>composite</b> natural numbers.
A:
A natural number \(n\ge2\) is <b>composite</b> if \(n=a\cdot b\) with natural numbers \(1\lt a,b\lt n\); otherwise it is <b>prime</b>. Every \(n\ge2\) is exactly one of the two; the first prime is \(2\).
E:
\(1\) is neither prime nor composite.

[QA]
Q:
State the <b>Fundamental Theorem of Arithmetic</b> (existence part proved in class).
A:
Every natural number \(n\ge2\) can be factored as a product of one or more primes: \(n=p_1 p_2\cdots p_i\).
E:
Proved by <b>strong</b> induction — the composite case \(k+1=a\cdot b\) needs the factorizations of \(a\) and \(b\), which are smaller than \(k\).

[QA]
Q:
Sketch the strong-induction proof that every \(n\ge2\) is a product of primes.
A:
Base \(P(2)\): \(2=2\). ✓ Step: assume \(P(j)\) for \(2\le j\le k\); show \(P(k+1)\).
<br><b>Case 1</b> — \(k+1\) prime: done (itself is the product).
<br><b>Case 2</b> — \(k+1\) composite: \(k+1=a\cdot b\) with \(2\le a,b\le k\). By hypothesis \(a=\prod p_i\), \(b=\prod q_j\), so \(k+1=\big(\prod p_i\big)\big(\prod q_j\big)\), a product of primes. \(\blacksquare\)

[QA]
Q:
What is a <b>logical contradiction</b>, and why can't true statements produce one?
A:
A contradiction is a statement \(R\) with \(R\wedge(\sim R)=T\) (both true and false). Starting only from true statements and applying valid logic can <b>never</b> yield a contradiction — so if your reasoning produces one, a starting assumption must be false.

[QA]
Q:
Describe the <b>game plan</b> for a proof by contradiction (Version I).
A:
To prove \(p\) true: assume instead \(\sim p\). From \(\sim p\), derive some \(R\) that is both true and false (a contradiction). Conclude \(\sim p=F\), hence \(p=T\).
E:
<b>Version II</b> for \(p\Rightarrow q\): assume \(p\wedge(\sim q)\), derive a contradiction, conclude \((p\wedge\sim q)=F\), i.e. \(p\Rightarrow q\).

[QA]
Q:
Prove by contradiction that \(\sqrt{2}\) is irrational.
A:
Assume \(\sqrt2=\tfrac{m}{n}\), \(m,n\) integers, \(n\ne0\), <b>no common factor</b> (true statement \(R\)). Then
\[ 2=\frac{m^2}{n^2}\Rightarrow 2n^2=m^2 \Rightarrow m^2\text{ even}\Rightarrow m\text{ even},\ m=2k. \]
So \(2n^2=4k^2\Rightarrow n^2=2k^2\Rightarrow n\) even. Now \(m,n\) share factor \(2\): \(\sim R\). Thus \(R\wedge\sim R\) — contradiction. Hence \(\sqrt2\) is irrational. \(\blacksquare\)
E:
Reuses the lemma "\(m^2\) even \(\Rightarrow m\) even" (the contrapositive proof from Lecture 1).

[CLOZE]
C:
In the \(\sqrt2\) proof the contradicted statement is {{c1::\(m\) and \(n\) have no common factor}}; we derive that both are {{c2::even}}, so they share the factor {{c3::2}}.

[QA]
Q:
Summarize the main <b>proof techniques</b> of the course.
A:
<ul>
<li><b>Direct:</b> \(p\Rightarrow q\).</li>
<li><b>Contrapositive:</b> \(\sim q\Rightarrow\sim p\).</li>
<li><b>Contradiction I:</b> assume \(\sim p\), derive \(R\wedge\sim R\).</li>
<li><b>Contradiction II:</b> assume \(p\wedge\sim q\), derive a contradiction.</li>
<li><b>Induction</b> (weak / strong).</li>
<li><b>Exhaustion:</b> finitely many checked cases.</li>
<li><b>Iff:</b> prove \(p\Rightarrow q\) and \(q\Rightarrow p\).</li>
</ul>
