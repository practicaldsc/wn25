---
layout: page
title: 5. Eigenvalues
description: >-
  Eigenvalues and eigenvectors.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 5
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

{: .red }
**This guide is incomplete and is under active development.**

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

## Eigenvalues and eigenvectors

Eigenvalues and eigenvectors appear often in data science. We'll start by establishing their fundamentals; the applications will become clear as the semester progresses.

$$\lambda_i$$ is an **eigenvalue** of square matrix $$A$$, corresponding to the **eigenvector** $$\vec{v}_i$$, if:

$$A \vec{v}_i = \lambda_i \vec{v}_i$$

In other words, $$\vec{v}_i$$ is an eigenvalue of $$A$$ if, when left-multiplied by $$A$$, its direction doesn't change, only its length. The amount $$\vec{v}_i$$'s length is scaled by is $$\lambda_i$$. We also say that $$\lambda_i$$ and $$\vec{v}_i$$ form an **eigenvalue-eigenvector pair of $$A$$**. (Note that $$\vec{0}$$ is never considered to be an eigenvector, since any matrix times $$\vec{0}$$ is always just $$\vec{0}$$.)

For example, if $$A = \begin{bmatrix} -5 & 2 \\ -7 & 4 \end{bmatrix}$$, then $$\vec{v}_1 = \begin{bmatrix} 2 \\ 7 \end{bmatrix}$$ is an eigenvector of $$A$$ corresponding to the eigenvalue $$\lambda_1 = 2$$, because:

$$A\vec{v}_1 = \begin{bmatrix} -5 & 2 \\ -7 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ 7 \end{bmatrix} = \begin{bmatrix} -5(2) + 2(7) \\ -7(2) + 4(7) \end{bmatrix} = \begin{bmatrix} 4 \\ 14 \end{bmatrix} = 2 \begin{bmatrix} 2 \\ 7 \end{bmatrix} = 2 \vec{v}_1$$

So, when $$\vec{v}_1$$ is multiplied by $$A$$, it still points in the same direction, it's just doubled in length.

**Verify yourself that $$\lambda_2 = -3$$ is also an eigenvalue of $$A$$, corresponding to the eigenvector $$\vec{v}_2 = \begin{bmatrix} 1 \\ 1\end{bmatrix}$$.**

## Invertibility and rank

Fact: An $$n \times n$$ matrix can have at most $$n$$ non-zero eigenvalues. The **rank** of a square matrix is equal to the number of non-zero eigenvalues it has.

<br>

Okay, so what did we need all of that for? It's to use this fact:

<center><b>A square matrix is invertible <i>if and only if</i> none of its eigenvalues are 0.</b></center>

More coming soon!

<!-- We will use this particular fact without proof, mostly because its proof is similar to the proof you're about to do yourself. If we can prove that none of $$X^TX + n \lambda_\text{ridge} I$$'s eigenvalues are 0, then we know it must be invertible, and so $$\vec{w}_\text{ridge}^*$$ is uniquely defined. This is especially useful if some of $$X^TX$$'s eigenvalues are 0, which is the case when $$X$$ (and $$X^TX$$) isn't full rank, and hence $$X^TX$$ isn't invertible. -->

Read more about eigenvalues and eigenvectors [**here**](https://math.libretexts.org/Bookshelves/Linear_Algebra/A_First_Course_in_Linear_Algebra_(Kuttler)/07%3A_Spectral_Theory/7.01%3A_Eigenvalues_and_Eigenvectors_of_a_Matrix), or watch [**this**](https://youtu.be/PhfbEr2btGQ?si=1diIM4b31qSYrDOZ) Khan Academy video.