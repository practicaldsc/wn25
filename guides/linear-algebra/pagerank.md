---
layout: page
title: "7. Application: PageRank"
description: >-
  A description of the PageRank algorithm.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 7
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

## Overview

Larry Page and Sergey Brin developed the Google search engine (originally known as "BackRub") while PhD students at Stanford University. Their key innovation was the **PageRank** algorithm, which involves a beautiful application of linear algebra. PageRank works by assigning each page on the internet a "score" based on its relative importance. Today, PageRank is one of the many algorithms that Google uses in determining how to rank search results.

**Key idea: The more incoming links a page has, the more important it is!**

<center>

<img src="../assets/images/network.png" width=300><br><small>An example network of pages.</small>
    
</center>

There are a few naïve approaches to scoring pages given that key idea, but they have their flaws:
- One idea: the score of a page is equal to the number of pages that link to it. This doesn't work because it doesn't account for the importance of the incoming links. For example, if my personal website links to [apple.com](https://apple.com), that doesn't make [apple.com](https://apple.com) any more important than it already was. But if [apple.com](https://apple.com) links to my personal website, that must mean my personal website is important!
- Another idea: The score of a page is equal to the sum of the scores of the pages that link to it. This also doesn't work, because there is no non-zero solution!

The actual solution assigns scores to pages such that **when a page links to several other pages, the score it gives to them is shared**.

In the example graph above, we see that:
- Page 1 links to Page 2.
- Page 2 links to Pages 1 and 4.
- Page 3 links to Pages 1 and 4.
- Page 4 links to Pages 1, 2, and 3.

If we let $$x_i$$ be the score assigned to Page $$i$$, we're looking for the solution to the equations:

$$\begin{align*}
x_1 &= &\frac{1}{2}x_2 &+ \frac{1}{2}x_3 &+ \frac{1}{3}x_4 \\
x_2 &= x_1 &&           &+ \frac{1}{3}x_4 \\
x_3 &= &&               & \frac{1}{3}x_4 \\
x_4 &= &\frac{1}{2}x_2 &+ \frac{1}{2}x_3
\end{align*}$$

A more concise way to express the system above is by defining an **adjacency matrix**, $$A$$, and writing the system in terms of matrix-vector multiplication:

$$\vec{x} = A \vec{x}, \qquad A = \begin{bmatrix}
0 & \frac{1}{2} & \frac{1}{2} & \frac{1}{3} \\
1 & 0 & 0 & \frac{1}{3} \\
0 & 0 & 0 & \frac{1}{3} \\
0 & \frac{1}{2} & \frac{1}{2} & 0
\end{bmatrix} \qquad \vec x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix}$$

{: .green }

Click [**here**](../matrices) for a review of how matrix-vector (and matrix-matrix) multiplication works.

**Our goal**: Given an adjacency matrix $$A$$, find the solution to the equation $$\vec{x} = A \vec{x}$$. The solution vector, $$\vec x$$, will contain the PageRank scores of each page!

Let's make sure we understand the structure of adjacency matrices, like $$A$$.
- Each **column** of an adjacency matrix describes the movement **from** a given page; the sums of the columns in an adjacency matrix are equal to 1.
- Each **row** of an adjacency matrix describes the movement **into** a given page; the sums of the rows in an adjacency matrix don't necessarily add to 1.

---

## Finding PageRank scores

Now that we've framed the problem of assigning a score to each page in terms of linear algebra, our problem is purely mathematical. Specifically, we need to find the solution to $$\vec x$$ in the equation:

$$\vec x = A \vec x$$

{: .green }
**Fact**: If $$A$$ is a valid adjacency matrix, then the solution to $$\vec x = A \vec x$$ is the eigenvector that corresponds to an **eigenvalue of 1**.

Not sure what that means? That's okay – you can learn about the basics of eigenvalues and eigenvectors in our guide, linked [here](../eigenvalues). But for the purposes of running the PageRank algorithm, you don't actually _need_ to know about eigenvalues and eigenvectors. That's because, due to properties of eigenvalues and eigenvectors that are outside of the scope of this course, we can estimate $$\vec x$$ with great accuracy if we follow the following process:

1. Start by initializing $$\vec x^{(0)}$$ to a uniform vector that sums to 1. This is our initial, or 0th, guess of the true value of $$\vec x$$. Our example network has four pages, meaning that $$\vec x \in \mathbb{R}^4$$, so we'd initialize $$\vec x^{(0)} = \begin{bmatrix} \frac{1}{4} \\ \frac{1}{4} \\ \frac{1}{4} \\ \frac{1}{4} \end{bmatrix}$$. You can imagine this means that a user is equally likely to be on any of the four pages before clicking anything.
1. Simulate the process of the user clicking one link by multiplying $$A$$ by $$\vec x^{(0)}$$, and call this $$\vec x^{(1)}$$, our next guess of the true $$\vec x$$. In other words, $$\vec x^{(1)} = A \vec x^{(0)}$$.
1. Repeat this again, so $$\vec x^{(2)} = A \vec x^{(1)}$$. But since $$\vec x^{(1)}$$ is itself just $$A \vec x^{(0)}$$, we have that $$\vec x^{(2)} = A (A \vec x^{(0)}) = A^2 \vec x^{(0)}$$. Here, $$A^2$$ is the result of multiplying the matrix $$A$$ by itself.
1. Repeat this again, so $$\vec x^{(3)} = A^3 \vec x^{(0)}$$.
1. Repeat many, many times, until the difference between $$\vec x^{(t)}$$ and $$\vec x^{(t-1)}$$ is minimal.

Eventually, our guesses $$\vec x^{(t)}$$ will converge on the true value of $$\vec x$$, which we can interpret as containing the probability that a user is on any particular page in the long run. **Larger probabilities mean more important pages!**

In short, to estimate $$\vec x$$, we evaluate $$A^{m} \vec x^{(0)}$$, where $$m$$ is some large integer and $$x^{(0)}$$ is a uniform vector. $$m = 100$$ is usually sufficient. This is sometimes called the **power method** for estimating eigenvectors.

---

## Implementation in Python

As a refresher, our adjacency matrix $$A$$ is shown below, along with the original network graph.

$$A = \begin{bmatrix}
0 & \frac{1}{2} & \frac{1}{2} & \frac{1}{3} \\
1 & 0 & 0 & \frac{1}{3} \\
0 & 0 & 0 & \frac{1}{3} \\
0 & \frac{1}{2} & \frac{1}{2} & 0
\end{bmatrix}$$

<center>

<img src="../assets/images/network.png" width=200>
    
</center>

Let's implement the power method in Python to assign PageRank scores to the four pages in our example network.

First, we'll define a 2D `numpy` array, `A`, corresponding to our adjacency matrix $$A$$:

```python
A = np.array([[0, 1 / 2, 1 / 2, 1 / 3],
              [1, 0, 0, 1 / 3],
              [0, 0, 0, 1 / 3],
              [0, 1 / 2, 1 / 2, 0]])
```

We'll also instantiate `x` to an array of length 4 in which each value is `1 / 4`. 

```python
x = np.ones(4) / 4
```

A better solution than writing:

```python
A @ A @ A @ A @ A @ A @ ... @ x
```

or even:

```python
for i in range(100):
    x = A @ x
```

is using `np.linalg.matrix_power`:

```python
scores = np.linalg.matrix_power(A, 100) @ x
```

If we peek at `scores`, we see the solution to $$\vec x = A \vec x$$:

```python
array([0.30769231, 0.38461538, 0.07692308, 0.23076923])
```

Above are what we call the PageRank scores of each page. Remember, larger scores are more important! This is telling us that:
- Page 2 is the most important,
- then Page 1,
- then Page 4,
- then Page 3.

So, if we were Google, we'd show Page 2 first, then Page 1, then Page 4, then Page 3.

Great work! You understand the magic behind Google. (Does this mean you automatically get a job at Google now? Unfortunately, no...)

---

## Further reading

We've explained the necessary components of PageRank in this guide, but you may also want to refer to these slides, which inspired our exposition: [The Billion Dollar Eigenvector](https://jdc.math.uwo.ca/M1600b-2014/l/pagerank-1600.pdf).

Another great book that touches on this subject (and many other mathematical topics that are of relevance to everyday life) is [The Joy of $$x$$](https://www.stevenstrogatz.com/books/the-joy-of-x) by award-winning author and professor Steven Strogatz.