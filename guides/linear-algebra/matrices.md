---
layout: page
title: 3. Matrices
description: >-
  Matrices and matrix-vector multiplication.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 3
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

<!-- ## Matrices and matrix-vector multiplication -->

<center>
<iframe width="800" height="225" src="https://www.youtube.com/embed/SqqmMRKwNw8?si=o7UBbbVEf0JgUM8i" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

<small>
[📝 slides](../assets/7-matrices.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/SqqmMRKwNw8){: .btn }
</small>

<!-- We're working on adding more detail to this guide, but for now, we've added detail that's relevant to understanding the guide on [PageRank](../pagerank). -->

## Mechanics of matrix-vector multiplication

The act of multiplying a matrix by a vector has profound meaning in mathematics, even as it relates to data science. As you read this guide further (and we have time to write more of it!), we'll expose you to more of that beauty. But in this first section, we'll focus on the mechanics.


{: .green }
**Golden Rule of Matrix Multiplication**: If $$A$$ and $$B$$ are two matrices, in order for the product $$AB$$ to be valid, **the number of columns in $$A$$ must equal the number of rows in $$B$$**. Sometimes, this is phrased as "the inner dimensions of $$A$$ and $$B$$ must match", for reasons we'll see shortly.

Let's suppose $$M$$ is a matrix with 4 rows and 3 columns:

$$M = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 1 & 9 \\ 0 & -1 & 0 \\ 2 & -2 & 0 \end{bmatrix}$$

And let's suppose $$\vec v$$ is some vector. Note that we can think of an $$n$$-dimensional vector as a matrix with $$n$$ rows and 1 column. In order for the product $$M \vec v$$ to be valid, $$\vec v$$ must have 3 elements in it, by the Golden Rule above. To make the example concrete, let's suppose:

$$\vec v = \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix}$$

How do we multiply $$M \vec v$$? To compute the output, we'll need to take the dot product between **every row of $$M$$ and every column of $$\vec v$$**. $$M$$ has 4 rows, and $$\vec v$$ has 1 column (itself), so we'll need to compute 4 dot products. More on this shortly.

Before actually performing the multiplication, we should be aware of what the dimensions of the output are going to be. Below, we've written the dimensions of $$M$$ ($$4 \times 3$$) and $$\vec v$$ ($$3 \times 1$$) next to each other. By the Golden Rule, the **inner dimensions, both of which are bolded**, must be equal in order for the multiplication to be valid. The dimensions of the output will be the result of looking at the $$\boxed{\text{outer dimensions}}$$, which here are $$4 \times 1$$.

$$
\underbrace{M}_{\boxed{4} \times \textbf{3}} \:\:\:\: \underbrace{\vec v}_{\textbf{3} \times \boxed{1}} = \underbrace{\text{output}}_{4 \times 1}
$$

So, the result of multiplying $$M \vec v$$ will be $$4 \times 1$$ matrix, or in other words, a vector with 4 components. Indeed, the result of multiply a matrix by a vector always results in another vector, and this act of multiplying a matrix by a vector is often thought of as **transforming** the vector.

So, how do we find those 4 components? As mentioned earlier, we compute each component by taking the dot product of a row in $$M$$ with $$\vec v$$.

$$M = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 1 & 9 \\ 0 & -1 & 0 \\ 2 & -2 & 0 \end{bmatrix} \qquad \vec v = \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix}$$

Let's start with the top row of $$M$$, which looks like $$\begin{bmatrix} 3 \\ 1 \\ 4\end{bmatrix}$$ if we treat as being its own vector. The dot product of two vectors is only defined if they have equal lengths. **This is why we've instituted the Golden Rule!** The Golden Rule tells us we can only multiply $$M$$ and $$\vec v$$ if the number of columns in $$M$$ is the same as the length of $$\vec v$$, and the number of columns in $$M$$ is equal to the length of each row of $$M$$.

If $$\vec u$$ and $$\vec v$$ both have the same number of components – say, $$n$$ – then:

$$\vec u \cdot \vec v = \sum_{i = 1}^n u_i v_i = u_1v_1 + u_2v_2 + ... + u_nv_n$$

So, the dot product of the first row of $$M$$ with $$\vec v$$ is:

$$\begin{bmatrix} 3 \\ 1 \\ 4 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix} = 3 \cdot 1 + 1 \cdot 0 + 4 \cdot 3 = \boxed{15}$$

Nice! We're a quarter of the way there. Now, we just need to compute the remaining three dot products:

The dot product of the second row of $$M$$ with $$\vec v$$ is $$\begin{bmatrix} 2 \\ 1 \\ 9 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix} = 2 \cdot 1 + 1 \cdot 0 + 9 \cdot 3 = \boxed{29}$$.

The dot product of the third row of $$M$$ with $$\vec v$$ is $$\begin{bmatrix} 0 \\ -1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix} = 0 \cdot 1 - 1 \cdot 0 + 0 \cdot 3 = \boxed{0}$$.

And finally, the dot product of the fourth row of $$M$$ with $$\vec v$$ is $$\begin{bmatrix} 2 \\ -2 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix} = 2 \cdot 1 - 2 \cdot 0 + 0 \cdot 3 = \boxed{2}$$.

The result of our matrix-vector multiplication, then, is the result of stacking all 4 dot products together into the vector $$\begin{bmatrix} 15 \\ 29 \\ 0 \\ 2\end{bmatrix}$$. To summarize:

$$M \vec v = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 1 & 9 \\ 0 & -1 & 0 \\ 2 & -2 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix} = \begin{bmatrix} 15 \\ 29 \\ 0 \\ 2 \end{bmatrix}$$

Python agrees with us, too. To verify yourself, run:

```python
import numpy as np
M = np.array([[3, 1, 4],
              [2, 1, 9],
              [0, -1, 0],
              [2, -2, 0]])

v = np.array([[1],
              [0],
              [3]])

M @ v
```

and you'll see:

```python
array([[15],
       [29],
       [ 0],
       [ 2]])
```

---

## Matrix-vector multiplication as a linear combination

We've described matrix-vector multiplication as the result of taking the dot product of each row of $$M$$ with $$\vec v$$. But, there's another interpretation. In the above dot products, you may have noticed:

- Entries in the first column of $$M$$ ($$3$$, $$2$$, $$0$$, and $$2$$) were always multiplied by the first element of $$\vec v$$ ($$1$$).
- Entries in the second column of $$M$$ ($$1$$, $$1$$, $$-1$$, and $$-2$$) were always multiplied by the second element of $$\vec v$$ ($$0$$).
- Entries in the third column of $$M$$ ($$4$$, $$9$$, $$0$$, and $$0$$) were always multiplied by the third element of $$\vec v$$ ($$3$$).

In other words:

$$M \vec v = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 1 & 9 \\ 0 & -1 & 0 \\ 2 & -2 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix} = \underbrace{1 \begin{bmatrix} 3 \\ 2 \\ 0 \\ 2 \end{bmatrix} + 0 \begin{bmatrix} 1 \\ 1 \\ -1 \\ -2 \end{bmatrix} + 3 \begin{bmatrix} 4 \\ 9 \\ 0 \\ 0 \end{bmatrix}}_{\text{constant$_1$ $\cdot$ vector$_1$ + constant$_2$ $\cdot$ vector$_2$ + constant$_3$ $\cdot$ vector$_3$}} = \begin{bmatrix} 15 \\ 29 \\ 0 \\ 2 \end{bmatrix}$$

A **linear combination** of vectors $$\vec u_1, \vec u_2, ... \vec u_d$$ is another vector of the form $$a_1 \vec u_1 + a_2 \vec u_2 + ... + a_d \vec u_d$$. In the example above, the $$a$$'s are 1, 0, and 3 (coming from $$\vec v$$), and the $$\vec u$$'s are the columns of $$M$$.

We'll see linear combinations quite a bit as the semester progresses. For now, this gives us another way to interpret matrix-vector multiplication: **by multiplying $$M$$ by $$\vec v$$, we are computing a linear combination of the columns of $$M$$, using the weights in $$\vec v$$!** 

---

## Matrix-matrix multiplication

<!-- $$
\begin{array}{rc}
\vec{v}^T &= \begin{bmatrix} 1 & \;\;0 & \;\;3 \end{bmatrix} \\[0.3em]
M &= \begin{bmatrix} 
3 & 1 & 4 \\ 
2 & 1 & 9 \\ 
0 & -1 & 0 \\ 
2 & -2 & 0
\end{bmatrix}
\end{array}
$$ -->

Matrix-matrix multiplication is a generalization of matrix-vector multiplication. Let's present matrix-matrix multiplication in its most general terms.

{: .green }
> Suppose:
> - $$A$$ is a $$n \times d$$ matrix, and
> - $$B$$ is a $$d \times p$$ matrix.
>
> Then, $$AB$$ is a $$n \times p$$ matrix such that:
> - the element in row $$i$$ and column $$j$$ of $$AB$$ is the **dot product of row $$i$$ of $$A$$ and column $$j$$ of $$B$$**, for $$i = 1, 2, ..., n$$ and $$j = 1, 2, ..., p$$.

Note that if $$p = 1$$, this reduces to the matrix-vector multiplication case from before. In that case, the only possible value of $$j$$ is 1, since the output only has 1 column, and the element in row $$i$$ of the output vector is the dot product of row $$i$$ in $$A$$ and the vector $$B$$ (which we earlier referred to as $$\vec v$$ in the less general case).

For a concrete example, suppose $$A$$ and $$B$$ are defined below:

$$A = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 1 & 9 \\ 0 & -1 & 0 \\ 2 & -2 & 0 \end{bmatrix} \qquad B = \begin{bmatrix} 1 & 2\\ 0 & 7\\ 3 & 2 \end{bmatrix}$$

Since $$A$$ has shape $$4 \times 3$$ and $$B$$ has shape $$3 \times 2$$, the output matrix will have shape $$4 \times 2$$. Each of those 8 elements will be the dot product of a row in $$A$$ with a column in $$B$$.

Work out the multiplication yourself, and verify that:

$$AB = \begin{bmatrix} 3 & 1 & 4 \\ 2 & 1 & 9 \\ 0 & -1 & 0 \\ 2 & -2 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2\\ 0 & 7\\ 3 & 2 \end{bmatrix} = \boxed{\begin{bmatrix} 15 & 21 \\ 29 & 29 \\ 0 & -7 \\ 2 & -10 \end{bmatrix}}$$

You should notice that many of the numbers in the output look familiar! That's because $$A$$ is the same matrix as $$M$$ in the matrix-vector example, and the first column of $$B$$ is just $$\vec v$$ from the matrix-vector example. So, the first column in $$AB$$ is the same as the vector $$M \vec v = \begin{bmatrix} 15 \\ 29 \\ 0 \\ 2\end{bmatrix}$$ as we computed earlier. The difference now is that the output $$AB$$ isn't just a single vector, but is a matrix with 2 columns. The second column, $$\begin{bmatrix} 21 \\ 29 \\ -7 \\ -10\end{bmatrix}$$, comes from multiplying $$A$$ by the second column in $$B$$, namely $$\begin{bmatrix} 2 \\ 7 \\ 2\end{bmatrix}$$.

Note that as we add columns to $$B$$, we'd add columns to the output. If $$B$$ had 10 columns, then $$AB$$ would have 10 columns, too, without $$A$$ needing to change. As long as the Golden Rule – that the number of columns in $$A$$ equals the number of rows in $$B$$ – holds, the product $$AB$$ can be computed.


<details markdown="1">

<summary><b>Question 1</b></summary>

**Question 1.1**

Suppose $$M \in \mathbb{R}^{m \times n}$$ is a matrix, $$\vec{v} \in \mathbb{R}^n$$ is a vector, and $$s \in \mathbb{R}$$ is a scalar.

Determine whether each of the following quantities is a matrix, vector, scalar, or undefined. If the result is a matrix or vector, determine its dimensions.

**(a)** $$M\vec{v}$$

**(b)** $$\vec{v} M$$

**(c)** $$\vec{v}^2$$

**(d)** $$M^TM$$

**(e)** $$MM^T$$

**(f)** $$\vec{v}^T M \vec{v}$$

**(g)** $$(sM\vec{v}) \cdot (sM\vec{v})$$

**(h)** $$(s \vec{v}^T M^T)^T$$

**(i)** $$\vec{v}^T M^T M \vec{v}$$

**(j)** $$\vec{v}\vec{v}^T + M^TM$$

**(k)** $$\frac{M \vec{v}}{\lVert \vec{v} \rVert} + (\vec{v}^T M^T M \vec{v}) M \vec{v}$$

---

**Question 1.2**

Consider the matrix $$X$$ and vector $$\vec w$$ defined below:

$$X = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \\ 5 & 1 & -2 \end{bmatrix} \qquad \vec{w} = \begin{bmatrix} 4 \\ 3 \\ -1 \end{bmatrix}$$

**(a)** Evaluate $$X \vec{w}$$.

**(b)** As we learned in the video above, the matrix-vector product $$X \vec{w}$$ is a linear combination of the columns of the matrix, $$X$$, using weights from the vector $$\vec{w}$$.

Fill in each blank below with a single number from the start of Question 13.

$$X \vec{w} = \underline{\hspace{0.5cm}} \begin{bmatrix} \underline{\hspace{0.5cm}} \\ \underline{\hspace{0.5cm}} \\ \underline{\hspace{0.5cm}} \end{bmatrix} + \underline{\hspace{0.5cm}} \begin{bmatrix} \underline{\hspace{0.5cm}} \\ \underline{\hspace{0.5cm}} \\ \underline{\hspace{0.5cm}} \end{bmatrix} + \underline{\hspace{0.5cm}} \begin{bmatrix} \underline{\hspace{0.5cm}} \\ \underline{\hspace{0.5cm}} \\ \underline{\hspace{0.5cm}} \end{bmatrix}$$

**(c)** Let's generalize the idea from part (b). Now, suppose $$X \in \mathbb{R}^{n \times d}$$ is a matrix whose columns, $$\vec{x}^{(1)}, \vec{x}^{(2)}, ..., \vec{x}^{(d)}$$ are all vectors in $$\mathbb{R}^n$$, and suppose that $$\vec{w} \in \mathbb{R}^d$$.

Fill in the blanks:

$$X \vec{w} = \sum_{i = 1}^{\boxed{\:\:\:}} \boxed{\:\:\:}$$

**(e)** Evaluate $$X^TX$$ and $$XX^T$$.

</details>
