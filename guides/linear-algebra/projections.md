---
layout: page
title: 4. Projections
description: >-
  Projecting onto the span of one or more vectors.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 4
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

## Projecting onto a single vector

<center>

<iframe width="800" height="225" src="https://www.youtube.com/embed/yMAcj3qrMa8?si=ZxOHPAT_RFGOSDUx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

<small>
[📝 slides](../resources/lin-alg/5-projecting-onto-single-vector.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/yMAcj3qrMa8){: .btn }
</small>

<details markdown="1">

<summary><b>Question 1</b></summary>

**Question 1.1**

Before we get into any calculations, we'll start by recapping the most recent video through some proofs. Our conclusion was that the vector in $$\text{span}(\vec x)$$ that was closest to $$\vec y$$ was the vector $$w^* \vec x$$, where:

$$w^* = \frac{\vec x \cdot \vec y}{\vec x \cdot \vec x}$$

**(a)** Use the dot product to show that $$\vec y - w^* \vec x$$ is orthogonal to $$\vec x$$.

**(b)** Consider the function $$\text{error}(w) = \lVert \vec y - w \vec x \rVert$$. Note that $$\text{error}$$ takes in a single real number as input and returns a single real number as output.

Show, using **calculus**, that $$w^*$$ minimizes $$\text{error}(w)$$. _Hint: Note that minimizing $$\lVert \vec y - w \vec x \rVert$$ is equivalent to minimizing $$\lVert \vec y - w \vec x \rVert^2$$, and that if $$\vec v$$ is a vector, then $$\lVert \vec v \rVert^2 = \vec v \cdot \vec v$$._

---

**Question 1.2**

Vectors get lonely, and so we will give each vector one friend to keep them company.

Specifically, if $$\vec{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$$, $$\vec{v}_f$$ is the friend of $$\vec v$$, where $$\vec{v}_f = \begin{bmatrix} -v_2 \\ v_1 \end{bmatrix}$$.

**(a)** Prove that $$\vec{v}$$ and $$\vec{v}_f$$ are orthogonal.

Now, consider the vectors $$\vec{c}$$ and $$\vec{d}$$ defined below:

$$\vec{c} = \begin{bmatrix} 1 \\ 7 \end{bmatrix} \qquad \vec{d} = \begin{bmatrix} -2 \\ 1 \end{bmatrix}$$

The next few parts ask you to write various vectors as scalar multiples of either $$\vec c$$, $$\vec{c}_f$$, $$\vec{d}$$, or $$\vec{d}_f$$, where $$\vec{c}_f$$ and $$\vec{d}_f$$ are the friends of $$\vec{c}$$ and $$\vec{d}$$, respectively. In each part, you should select one of the four vectors provided, and fill a scalar in the blank. Part of part (b) is done for you.

**(b)** A vector in $$\text{span}(\vec d)$$ that is twice as long as $$\vec d$$.

$$\underset{\text{scalar goes here}}{\underline{\hspace{0.5in}}} \qquad \times \qquad \qquad \underbrace{\vec{c} \qquad \qquad \vec{c}_f \qquad \qquad \boxed{\vec{d}} \qquad \qquad \vec{d}_f}_{\text{pick one of these four}}$$

**(c)** The projection of $$\vec c$$ onto $$\text{span}(\vec d)$$.

$$\underset{\text{scalar goes here}}{\underline{\hspace{0.5in}}} \qquad \times \qquad \qquad \underbrace{\vec{c} \qquad \qquad \vec{c}_f \qquad \qquad \vec{d} \qquad \qquad \vec{d}_f}_{\text{pick one of these four}}$$

**(d)** The error vector of the projection of $$\vec c$$ onto $$\text{span}(\vec d)$$.

$$\underset{\text{scalar goes here}}{\underline{\hspace{0.5in}}} \qquad \times \qquad \qquad \underbrace{\vec{c} \qquad \qquad \vec{c}_f \qquad \qquad \vec{d} \qquad \qquad \vec{d}_f}_{\text{pick one of these four}}$$

**(e)** The projection of $$\vec d$$ onto $$\text{span}(\vec c)$$.

$$\underset{\text{scalar goes here}}{\underline{\hspace{0.5in}}} \qquad \times \qquad \qquad \underbrace{\vec{c} \qquad \qquad \vec{c}_f \qquad \qquad \vec{d} \qquad \qquad \vec{d}_f}_{\text{pick one of these four}}$$

**(f)** The error vector of the projection of $$\vec d$$ onto $$\text{span}(\vec c)$$.

$$\underset{\text{scalar goes here}}{\underline{\hspace{0.5in}}} \qquad \times \qquad \qquad \underbrace{\vec{c} \qquad \qquad \vec{c}_f \qquad \qquad \vec{d} \qquad \qquad \vec{d}_f}_{\text{pick one of these four}}$$

_Note that this question appeared in an exam for the class these videos are from!_

</details>

---

## Projecting onto the span of multiple vectors

<center>
<iframe width="800" height="225" src="https://www.youtube.com/embed/wKc2Oxx0FpU?si=I6765VyHA9SkxZYe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/dJcbJKpYywk?si=lVLDKPQs2iUc6P9K" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

<small>
[📝 slides](../assets/6-projecting-onto-multiple-vectors.pdf){: .btn } &nbsp; [🎥 video 1 on YouTube](https://youtu.be/wKc2Oxx0FpU){: .btn } &nbsp; [🎥 video 2 (animation by Jack Determan) on YouTube](https://youtu.be/dJcbJKpYywk){: .btn }
</small>


---

## Projecting onto the span of multiple vectors, again

Before watching the following video, you may want to review the idea of matrix inverses – [here's a link to a relevant lesson on Khan Academy](https://www.khanacademy.org/math/precalculus/matrices/intro-to-matrix-inverses/v/inverse-matrix-introduction).

<center>
<iframe width="800" height="225" src="https://www.youtube.com/embed/d6Z-r_j8EYg?si=DB8uhRCZYmrSVoqP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

The video below summarizes the last few videos on projections. It doesn't introduce any new content – so you don't _need_ it to solve the questions below – but you may want to watch it nevertheless for review.

<center>
<iframe width="800" height="225" src="https://www.youtube.com/embed/OpThKsgUffY?si=00scur_99TqGvLih" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

<small>
[📝 slides 1](../assets/8-projecting-onto-multiple-again.pdf){: .btn } &nbsp; [📝 slides 2](../assets/9-recap.pdf){: .btn } &nbsp; [🎥 video 1 on YouTube](https://youtu.be/d6Z-r_j8EYg){: .btn } &nbsp; [🎥 video 2 on YouTube](https://youtu.be/OpThKsgUffY){: .btn }
</small>

<details markdown="1">

<summary><b>Question 2</b></summary>

Consider the vectors $$\vec{u}$$, $$\vec{v}$$, defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$

We define $$X \in \mathbb{R}^{3 \times 2}$$ to be the matrix whose first column is $$\vec u$$ and whose second column is $$\vec v$$.

**(a)** In this part only, let $$\vec y = \begin{bmatrix} -1 \\ k \\ 252 \end{bmatrix}$$. Find a scalar $$k$$ such that $$\vec y$$ is in $$\text{span}(\vec u, \vec v)$$.

**(b)** Show that:

$$(X^TX)^{-1}X^T = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} \end{bmatrix}$$

_Hint: If $$A = \begin{bmatrix} a_1 & 0 \\ 0 & a_2 \end{bmatrix}$$, then $$A^{-1} = \begin{bmatrix} \frac{1}{a_1} & 0 \\ 0 & \frac{1}{a_2} \end{bmatrix}$$._

**(c)** Now, let $$\vec y = \begin{bmatrix} 4 \\ 2 \\ 8 \end{bmatrix}$$.

Find scalars $$a$$ and $$b$$ such that $$a \vec u + b \vec v$$ is the vector in $$\text{span}(\vec u, \vec v)$$ that is as close to $$\vec y$$ as possible.

**(d)** Let $$\vec e = \vec y - (a \vec u + b \vec v)$$, where $$a$$ and $$b$$ are the values you found in part (c).

You should notice that the sum of the entries in $$\vec e$$ is 0. Why is that the case?

</details>