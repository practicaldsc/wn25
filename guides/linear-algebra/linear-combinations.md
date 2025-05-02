---
layout: page
title: 2. Linear combinations
description: >-
  Adding and scaling vectors; linear combinations and span.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 2
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>


## Adding and scaling vectors

<center>

<iframe width="800" height="225" src="https://www.youtube.com/embed/p4XV6x4ytJc?si=DBIm8FyUcgkE-Pdt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</center>

<small>
[📝 slides](../assets/3-adding-and-scaling.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/p4XV6x4ytJc){: .btn }
</small>

<details markdown="1">

<summary><b>Question 1</b></summary>

Consider the vectors $$\vec{u}$$ and $$\vec{v}$$ defined below:

$$\vec{u} = \begin{bmatrix} 2 \\ -1 \\ 0 \\ 5 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 1 \\ 2 \\ 4 \\ -3 \end{bmatrix}$$

**(a)** Show that $$\vec u + \vec v$$ and $$\vec u - \vec v$$ are orthogonal.

**(b)** Now, suppose that $$\vec u, \vec v \in \mathbb{R}^n$$ are two arbitrary vectors with the same number of components. Is it always true that $$\vec u + \vec v$$ and $$\vec u - \vec v$$ are orthogonal?

- If so, prove why.
- If not, specify conditions under which it's guaranteed that $$\vec u + \vec v$$ and $$\vec u - \vec v$$ are orthogonal, and show your work.

_Hint: You'll need to use the [distributive property of the dot product](https://proofwiki.org/wiki/Dot_Product_Distributes_over_Addition)._

</details>

---


## Linear combinations and span

<center>

<iframe width="560" height="315" src="https://www.youtube.com/embed/k7RM-ot2NWY?si=q9uJtHyWXME6pvGS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="800" height="225" src="https://www.youtube.com/embed/GIMVvXHj9y8?si=-6ciWNNZ___zbGvU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</center>

<small>
[📝 slides](../assets/4-linear-combinations-and-span.pdf){: .btn } &nbsp; [🎥 video 1 (3Blue1Brown) on YouTube](https://youtu.be/k7RM-ot2NWY?si=Wnu77kbGduollatl){: .btn } &nbsp; [🎥 video 2 on YouTube](https://youtu.be/GIMVvXHj9y8){: .btn }
</small>

<details markdown="1">

<summary><b>Question 2</b></summary>

Consider the vectors $$\vec{a}$$ and $$\vec{b}_k$$ defined below:

$$\vec a = \begin{bmatrix} 2 \\ -1 \end{bmatrix} \qquad \vec{b}_k = \begin{bmatrix} k \\ 3 \end{bmatrix}$$

**(a)** Write $$\vec{c} = \begin{bmatrix} 2 \\ -17 \end{bmatrix}$$ as a linear combination of $$\vec a$$ and $$\vec{b}_2$$.

**(b)** There is exactly one value of $$k$$ such that $$\text{span}(\vec{a}, \vec{b}_k) \neq \mathbb{R}^2$$. What is that value of $$k$$, and why?

</details>

---

## Linear independence

There's no past lecture video that addresses this idea in detail, but it's an important one.

In the 3Blue1Brown video in the section above, you saw a graphical depiction of when three vectors in $$\mathbb{R}^3$$ **do** span all of $$\mathbb{R}^3$$, and of when they **don't** span all of $$\mathbb{R}^3$$. But, given three vectors in $$\mathbb{R}^3$$ in component form, how do we determine whether or not they span all of $$\mathbb{R}^3$$?

It turns out that this question will be of great importance to us when we study machine learning later on in the quarter. Our ability to make predictions about the future in some cases, strangely enough, will depend on whether or not a collection of $$d$$ vectors in $$\mathbb{R}^n$$ are linearly independent. When we get to that point, our vectors will contain data about the individuals in our dataset – for instance, we may have a height vector, that contains the height of every person in our dataset in inches, and a weight vector, that contains the weight of every person in our dataset in pounds. (That's not terribly important right now – but it's important to keep that in perspective. There's a reason you need to know all of this.)

Vectors $$\vec v_1, \vec v_2, ..., \vec v_d$$ are **linearly independent** **if and only if** the only solution to:

$$a_1 \vec v_1 + a_2 \vec v_2 + ... + a_d \vec v_d = \vec{0}$$

is:

$$a_1 = a_2 = ... = a_d = 0$$

If there is any solution $$a_1 \vec v_1 + a_2 \vec v_2 + ... + a_d \vec v_d = \vec{0}$$ in which at least one of $$a_1, a_2, ..., a_d \neq 0$$, then $$\vec v_1, \vec v_2, ... \vec v_d$$ are **linearly dependent**.

In general, there is a computational strategy for determining whether $$d$$ vectors in $$\mathbb{R}^n$$ are linearly independent, which you can learn more about [here](https://youtu.be/yLi8RxqfowA?feature=shared). But for us, the conceptual understanding will be more useful. Intuitively, a set of vectors is linearly dependent – that is, **not** linearly independent – if at least one vector in the set can be written as a linear combination of other vectors in the set.

For instance, consider the vectors $$\vec{u}$$, $$\vec{v}$$, and $$\vec{w}$$, defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix} \qquad \vec{w} = \begin{bmatrix} -1 \\ -6 \\ 17 \end{bmatrix}$$

Here, $$\vec{w} = 2 \vec{u} - \vec{v}$$, which means that $$\vec{w} \in \text{span}(\vec{u}, \vec{v})$$, i.e. that $$\vec{w}$$ can be written as a linear combination of other vectors in the set. Therefore, vectors $$\vec{u}, \vec{v}, \vec{w}$$ are **not** linearly independent, and are instead linearly **dependent**.

If you want to see how this ties into the formal definition of linear independence, note that starting with $$\vec{w} = 2 \vec{u} - \vec{v}$$, we can re-arrange to get $$2 \vec{u} - \vec{v} - \vec{w} = \vec{0}$$, which means that we've found a solution to $$a \vec{u} + b \vec{v} + c \vec{w} = \vec{0}$$ **that isn't** $$a = b = c = 0$$. Specifically, we've found that $$a = 2, b = -1, c = -1$$ also satisfies $$a \vec u + b \vec v + c \vec w = \vec 0$$. This means, again, that $$\vec u, \vec v, \vec w$$ are not linearly independent.

Practically, this means that $$\text{span}(\vec{u}, \vec{v}, \vec{w}) = \text{span}(\vec{u}, \vec{v})$$, i.e. $$\vec{w}$$ doesn't "contribute" or "unlock any new vectors" to the span of just $$\vec{u}$$ and $$\vec{v}$$.

Thinking back to the heights and weights example, suppose that in addition to a vector that has everyone's height in inches and another vector that has everyone's weight in pounds, we also have a vector that has everyone's height in centimeters. Since 1 inch = 2.54 centimeters, we'd have that:

$$\text{vector with heights in centimeters} = 2.54 (\text{vector with heights in inches})$$

which means that the vector with everyone's height in centimeters is redundant with the vector with everyone's height in inches. It doesn't change the span of our vectors, and down the road, that'll mean that it doesn't improve the quality of our predictions.

<details markdown="1">

<summary><b>Question 3</b></summary>

<!-- In the case where we have 3 arbitrary vectors $$\vec u, \vec v, \vec w \in \mathbb{R}^3$$ – that is, $$n = d = 3$$ – there is a special way we can determine whether $$\vec u, \vec v, \vec w$$ are linearly independent. -->

The **scalar triple product** of three vectors $$\vec u, \vec v, \vec w \in \mathbb{R}^3$$ is defined as:

$$\vec u \cdot (\vec v \times \vec w)$$

The scalar triple product has several interesting properties, which you can read about [here](https://en.wikipedia.org/wiki/Triple_product). One of the many uses of the scalar triple product is that it can be used to determine whether the vectors $$\vec u, \vec v, \vec w$$ are linearly independent! **Specifically, if the scalar triple product is equal to 0, then $$\vec u, \vec v, \vec w$$ are linearly dependent; otherwise, $$\vec u, \vec v, \vec w$$ are linearly independent.**

(Remember that the cross product is only defined for two vectors in $$\mathbb{R}^3$$, meaning that the scalar triple product is only defined for three vectors in $$\mathbb{R}^3$$. In all other cases, we'd need to use some other technique for determining whether the vectors are linearly independent.)

**(a)** Using the scalar triple product, determine whether or not the three vectors defined below are linearly independent.

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix} \qquad \vec{w} = \begin{bmatrix} 3 \\ 2 \\ -2 \end{bmatrix}$$

**(b)** Suppose again that $$\vec u, \vec v, \vec w \in \mathbb{R}^3$$ are arbitrary vectors. **Argue** why it must be the case that, if the scalar triple product $$\vec u \cdot (\vec v \times \vec w)$$ is equal to 0, then $$\vec u$$ must be in $$\text{span}(\vec{v}, \vec{w})$$, indicating that $$\vec u, \vec v, \vec w$$ are not linearly independent.

</details>