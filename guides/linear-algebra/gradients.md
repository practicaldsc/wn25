---
layout: page
title: 6. Gradients
description: >-
  The gradient of a multivariate function.
parent: 🧮 Linear Algebra
grand_parent: 🧑‍🤝‍🧑 Guides
nav_order: 6
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

The concepts explained in the first four guides are typically covered – or, are related to what's covered – in a linear algebra course. In addition to all of that, though, we'll also need a few concepts that are traditionally covered in a multivariate calculus course, such as Math 215.

To start, let's remember the idea of derivatives from single variable calculus. Consider, for example, the function $$f(t) = 5t^4 - t^3 - 5t^2 + 2t - 9$$. Then, we have:

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

- The derivative, $$\frac{df}{dt}(t) = 20t^3 - 3t^2 - 10t + 2$$, is the <span style="color:red">slope of the tangent line</span> to $$f$$ at the point $$(t, f(t))$$. For example, at $$t = 0$$, the derivative is 2, which means the slope of the tangent line at $$(0, -9)$$ is 2.
- The derivative at a point describes the instantaneous rate of change of the function at that point – the larger the derivative is at a point, the more quickly the function is increasing at that point (i.e. the steeper it is).
- The closer $$t$$ is to a minimum, the shallower the <span style="color:red">slope of the tangent line</span> is – at a minimum, the <span style="color:red">slope of the tangent line</span> is 0!

<center>

<iframe src="../assets/slopes_changing.html" frameBorder=0 width=800 height=450></iframe>

<small>The animation above might automatically start playing – to restart it, click "⏯️ Stop animation" and then "▶️ Start animation."</small>

</center>

Moving forward, we will encounter functions that take in multiple inputs, such as:

$$f(x, y) = (x - 2)^2 + 2x - (y - 3)^2$$

The [graph of a function like this](https://www.desmos.com/3d/3ifa5tljma) is a _surface_ in 3 dimensions.

<iframe src="https://www.desmos.com/3d/3ifa5tljma" width="800" height="400"></iframe>

Now, since $$f$$ has multiple input variables, it has multiple rates of change – one in the $$x$$ direction and one in the $$y$$ direction. So, instead of just a single derivative, $$f$$ has two partial derivatives, $$\frac{\partial f}{\partial x}$$ and $$\frac{\partial f}{\partial y}$$.

$$\frac{\partial f}{\partial x}$$ describes the rate of change in the $$x$$ direction – that is, the rate of change of $$f$$ when $$x$$ changes, but $$y$$ is held constant. To compute $$\frac{\partial f}{\partial x}$$, we treat $$y$$ as a constant and take the derivative with respect to $$x$$. Since $$f(x, y) = (x - 2)^2 + 2x - (y - 3)^2$$, we have that:

$$\frac{\partial f}{\partial x} = 2(x-2) + 2 \qquad \frac{\partial f}{\partial y} = -2(y-3)$$

We expand on this idea, and its connection to linear algebra, below, but it's advised that you first work through the following articles on Khan Academy:
- [Introduction to partial derivatives](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives).
- [The gradient](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/the-gradient).


<center>
<iframe width="800" height="225" src="https://www.youtube.com/embed/q_OJDHWNpOU?si=61AgG89aHLgT_kyS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>


<small>
[📝 slides](../assets/10-gradients.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/q_OJDHWNpOU){: .btn }
</small>

<details markdown="1">

<summary><b>Question 1</b></summary>

**Question 1.1**

Suppose $$g: \mathbb{R}^2 \rightarrow \mathbb{R}$$ is the function:

$$g(\vec x) = (x_1 - 3)^2 + (x_1^2 - x_2)^2$$

**(a)** Find $$\nabla g(\vec x)$$, the gradient of $$g$$, and use it to show that $$\nabla g \left( \begin{bmatrix} -1 \\ 1 \end{bmatrix} \right) = \begin{bmatrix} -8 \\ 0 \end{bmatrix}$$.

**(b)** Using $$\nabla g(\vec x)$$, determine the vector $$\vec x^*$$ that minimizes the output of $$g$$. How can you tell, without the use of any second derivative tests, that $$g$$ has a global minimum?

---

**Question 1.2**

**(a)** Suppose $$\vec{a} \in \mathbb{R}^3$$, and suppose $$f: \mathbb{R}^3 \rightarrow \mathbb{R}$$ is the function:

$$f(\vec x) = \vec{a}^T \vec{x} = a_1x_1 + a_2x_2 + a_3x_3$$

What is the gradient of $$f$$?

**(b)** Suppose $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is the function:

$$f(\vec x) = \vec x \cdot \vec x = x_1^2 + x_2^2 + ... + x_n^2$$

What is the gradient of $$f$$?

</details>
