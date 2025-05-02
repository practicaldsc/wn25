---
layout: page
title: 1. Vectors and angles
description: >-
  An introduction to vectors, the dot product, angles, and orthogonality.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 1
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

## Vectors and the dot product

<center>

<iframe width="800" height="225" src="https://www.youtube.com/embed/wT2wI9FuYZw?si=FPVqCerYGxSqLqWs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</center>

<small>
[📝 slides](../assets/1-vectors-dot-product.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/wT2wI9FuYZw){: .btn }
</small>

<details markdown="1">

<summary><b>Question 1</b></summary>

**Question 1.1**

Consider the vectors $$\vec{u}$$ and $$\vec{v}$$ defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix}$$

Determine the values of the following quantities.

**(a)** $$\lVert \vec u \rVert$$

**(b)** $$\vec u \cdot \vec v$$

**(c)** $$\vec v^T \vec u$$

---

**Question 1.2**

Suppose that on your way home from discussion section on North Campus, you drive 2 miles east and 7 miles north. (For the purposes of this question, assume that North Campus can be represented by just a single point.)

**(a)** How far do you live from North Campus, in miles?

**(b)** Suppose we draw a horizontal line passing through North Campus, and a line passing through North Campus and your home. Determine the angle between the two lines in **degrees**. (You'll need to use a calculator – Google works just fine!)

---

**Question 1.3**

Suppose $$\vec{1} \in \mathbb{R}^n$$ is a vector containing the value 1 for each element, i.e. $$\vec{1} = \begin{bmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{bmatrix}$$. For any other vector $$\vec{b} = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}$$, what is the value of $$\vec{1} \cdot \vec{b}$$?

</details>

---

## The dot product, angles, and orthogonality

<center>

<iframe width="800" height="225" src="https://www.youtube.com/embed/-PrfZdGh11g?si=sIKE-MPmrMI_q9B3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</center>

<small>
[📝 slides](../assets/2-dot-product-angle-orthogonality.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/-PrfZdGh11g){: .btn }
</small>

<details markdown="1">

<summary><b>Question 2</b></summary>

**Question 2.1**

Consider the vectors $$\vec{u}$$ and $$\vec{v}$$ defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix}$$

Determine the angle between $$\vec u$$ and $$\vec v$$ in the form of $$\cos^{-1} ( \cdot )$$. _Hint: You'll know you did this correctly if you find that, when converted to degrees, the angle between $$\vec u$$ and $$\vec v$$ is approximately $$101º$$._

---

**Question 2.2**

_Note: In addition to reviewing the concepts in the video, this question is also designed to refresh your understanding of limits from Calculus 1._

Consider the vectors $$\vec{x}$$ and $$\vec{y}_c$$ defined below:

$$\vec{x} = \begin{bmatrix} -4 \\ 3 \end{bmatrix} \qquad \vec{y}_c = \begin{bmatrix} 3 \\ c \end{bmatrix}$$

Here, $$c$$ is an unknown real number. For example:

$$\vec{y}_2 = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$$

**(a)** On a piece of paper (or on a tablet), draw $$\vec x$$, $$\vec y_0$$, $$\vec y_{20}$$, and $$\vec y_{-30}$$.

**(b)** Define $$\theta_c$$ to be the angle between $$\vec{x}$$ and $$\vec{y}_c$$. Using properties of limits, show that:

$$\lim_{c \rightarrow \infty} \theta_c = \cos^{-1} \left( \frac{3}{5} \right)$$

**(c)** Is $$\cos^{-1} \left( \frac{3}{5} \right)$$ the largest possible value of $$\theta_c$$, or the smallest possible value?
- If you believe this is the largest possible value of $$\theta_c$$, determine the smallest possible value of $$\theta_c$$.
- If you believe this is the smallest possible value of $$\theta_c$$, determine the largest possible value of $$\theta_c$$.

**(d)** $$\cos^{-1} \left( \frac{3}{5} \right)$$ – which, recall, is $$\displaystyle \lim_{c \rightarrow \infty} \theta_c$$ – is also equal to the angle between $$\vec{x}$$ and a particular unit vector, $$\vec u$$. (A unit vector $$\vec u$$ is a vector such that $$\lVert \vec u \rVert$$ = 1.) What is the vector $$\vec u$$?

---

**Question 2.3**

As we saw in the first two videos, the dot product $$\vec u \cdot \vec v$$ of two vectors $$\vec u, \vec v \in \mathbb{R}^n$$:
- returns a **scalar** – that is, a single number.
- is valid for any $$n \geq 1$$, as long as both $$\vec u$$ and $$\vec v$$ have the same number of components.
- measures how similar $$\vec u$$ and $$\vec v$$ are.

The **cross product** $$\vec u \times \vec v$$ of two vectors is only defined when both vectors are in $$\mathbb{R}^3$$. If $$\vec{u} = \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix}$$ and $$\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}$$, then:

$$\vec u \times \vec v = \begin{bmatrix} u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1 \end{bmatrix}$$

Note that the cross product of two vectors in $$\mathbb{R}^3$$ is another **vector** in $$\mathbb{R}^3$$, rather than a scalar! In particular, the cross product $$\vec u \times \vec v$$ is defined to be a vector **orthogonal** to both $$\vec u$$ and $$\vec v$$, with a length of $$\lVert \vec u \rVert \lVert \vec v \rVert \sin \theta$$, pointing [in the direction determined by the right hand rule](https://en.wikipedia.org/wiki/Cross_product#Definition):

<center>
<img src="../assets/images/right-hand-rule.png" width=250>
</center>

**(a)** Prove that $$\vec u \times \vec v$$ is orthogonal to both $$\vec u$$ and $$\vec v$$.

**(b)** What is the vector $$\vec u \times \vec u$$?

**(c)** Once again, consider the vectors $$\vec{u}$$ and $$\vec{v}$$ defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix}$$
 
There are infinitely many vectors that are orthogonal to both $$\vec u$$ and $$\vec v$$, but they all point in the same direction. Determine the vector $$\vec w = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix}$$ that is orthogonal to both $$\vec u$$ and $$\vec v$$ such that $$w_1 + w_2 + w_3 = 1$$.

</details>