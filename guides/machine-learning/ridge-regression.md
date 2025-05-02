---
layout: page
title: Ridge Regression
description: >-
  More details on ridge regression.
parent: 🤖 Machine Learning
grand_parent: 🧑‍🤝‍🧑 Guides
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .green }

> This guide is designed to:
> 1. Give you a better understanding of regularization, as covered in [Lecture 19](https://practicaldsc.org/resources/lectures/lec19/lec19-filled.html).
> 2. Prepare you for Homework 9, Question 1, which is on the theory of regularization.
>
> This guide is essential, but it is **not** a substitute for reading and watching Lecture 19.

---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

## Overview

As we will see in Lecture 19, **ridge regression** is the problem of finding the vector $$\vec{w}$$ that minimizes the following **objective function**:

$$R_\text{ridge}(\vec{w}) = \frac{1}{n} \lVert \vec{y} - X \vec{w} \rVert_2^2 + \underbrace{\lambda \sum_{j = 1}^d w_j^2}_{\text{regularization penalty!}}$$

Once we find that vector, we can make predictions using $$\vec{h} = X \vec{w}_\text{ridge}^*$$, where $$X$$ is a design matrix with information about the individuals we want to make predictions for. The fact that we've added a penalty, $$\lambda \sum_{j = 1}^d w_j^2$$, on the norm of our parameter vector $$\vec{w}$$ to our objective function means that we are regularizing our objective function, i.e. we are performing **regularization**. 

The vector that minimizes $$R_\text{ridge}(\vec{w})$$ is:

$$\vec{w}_\text{ridge}^* = (X^TX + n \lambda I)^{-1} X^T \vec{y}$$

$$\vec{w}_\text{ridge}^*$$ is unique, whether or not $$X$$ is full rank. 

This is different from $$\vec{w}_\text{OLS}^* = (X^TX)^{-1}X^T \vec{y}$$, which is only uniquely defined when $$X^TX$$ is invertible; otherwise, all of the infinitely many solutions to the normal equations, $$X^TX \vec{w}_\text{OLS}^* = X^T \vec{y}$$, minimize mean squared error. Remember, "OLS" refers to "ordinary least squares", the process of minimizing mean squared error, $$R_\text{sq}(\vec{w}) = \frac{1}{n} \lVert \vec y - X \vec w \rVert_2^2$$, with no regularization.

Some lingering questions:
- When there are infinitely many solutions to the normal equations, which solution(s) does Python return?
- Why is it called ridge regression?
- Why is $$\vec{w}_\text{ridge}^*$$ always uniquely-defined, i.e. why does the ridge regression objective function always have a unique solution?

The purpose of this guide is to explore these lingering ideas.

---

## Framing the problem

To start, we load in the dataset containing the weights and heights of 25,000 18 year olds we used in Lecture 16 to demonstrate multicollinearity.

```python
heights.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height (Inches)</th>
      <th>Height (Feet)</th>
      <th>Weight (Pounds)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>65.78331</td>
      <td>5.481942</td>
      <td>112.9925</td>
    </tr>
    <tr>
      <th>1</th>
      <td>71.51521</td>
      <td>5.959601</td>
      <td>136.4873</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69.39874</td>
      <td>5.783228</td>
      <td>153.0269</td>
    </tr>
    <tr>
      <th>3</th>
      <td>68.21660</td>
      <td>5.684717</td>
      <td>142.3354</td>
    </tr>
    <tr>
      <th>4</th>
      <td>67.78781</td>
      <td>5.648984</td>
      <td>144.2971</td>
    </tr>
  </tbody>
</table>
</div>

Note that there are two height columns, `'Height (Inches)'` and `'Height (Feet)'`. Remember that 1 foot is equal to 12 inches, so the values in the `'Height (Inches)'` column are 12 times the values in the `'Height (Feet)'` column.

Throughout this question, we'll aim to predict `'Weight (Pounds)'` using the other two features. Let's start by plotting `'Weight (Pounds)'` vs. `'Height (Inches)'`:

<center>
<iframe src="../assets/ridge-1.html" width="85%" height="400" frameborder="0"></iframe>
</center>

And `'Weight (Pounds)'` vs. `'Height (Inches)'` and `'Height (Feet)'`:

<iframe src="../assets/ridge-2.html" width="85%" height="400" frameborder="0"></iframe>

Drag the plot above around. You should notice that the points form a flat "patty" that resembles the 2D plot from above, not a cloud ☁️
like in other 3D scatter plots we've seen in class. This is because `'Height (Feet)'` and `'Height (Inches)'` are the same values, just in different units. For a particular `'Height (Feet)'` value, there is only one possible `'Height (Inches)'` value – specifically, 12 times the `'Height (Feet)'` value – and so all points in the plot sit on the flat plane:

$$\text{Height (Inches)} = 12 \cdot \text{Height (Feet)}$$

We'll start by fitting a multiple linear regression model to predict `'Weight (Pounds)'` from `'Height (Inches)'` and `'Height (Feet)'`, without regularization. Our model is of the form:

$$\text{predicted Weight (Pounds)}_i = w_0 + w_1 \cdot \text{Height (Inches)}_i + w_2 \cdot \text{Height (Feet)}_i$$

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(people[['Height (Inches)', 'Height (Feet)']], 
                                                    people['Weight (Pounds)'])
```

The design matrix for our training data, `X_train_design`, is defined below:

```python
X_train_design = X_train.copy()
X_train_design['1'] = 1
X_train_design = X_train_design[['1', 'Height (Inches)', 'Height (Feet)']]
X_train_design
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>Height (Inches)</th>
      <th>Height (Feet)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10903</th>
      <td>1</td>
      <td>68.92271</td>
      <td>5.743559</td>
    </tr>
    <tr>
      <th>7740</th>
      <td>1</td>
      <td>65.18871</td>
      <td>5.432392</td>
    </tr>
    <tr>
      <th>6636</th>
      <td>1</td>
      <td>70.49243</td>
      <td>5.874369</td>
    </tr>
    <tr>
      <th>23722</th>
      <td>1</td>
      <td>68.71113</td>
      <td>5.725928</td>
    </tr>
    <tr>
      <th>10148</th>
      <td>1</td>
      <td>65.69257</td>
      <td>5.474381</td>
    </tr>
  </tbody>
</table>

We know that our design matrix isn't full rank. Python knows this, too:

```python
np.linalg.matrix_rank(X_train_design)
```

```
2
```

Note that $$X$$ and $$X^TX$$ have the same rank:

```python
np.linalg.matrix_rank(X_train_design.T @ X_train_design)
```

```
2
```

So, $$X^TX$$ is not invertible, and there are infinitely many solutions to the normal equations, 

$$X^TX \vec{w}_\text{OLS}^* = X^T \vec{y}$$

No line of code can return an infinitely long output (at least, not in finite time), so there's no way to see **all** of the infinitely many possible solutions in code. Instead, to find the relationship between the infinitely many possible $$\vec{w}^*_\text{OLS}$$ values, we'd need to think about the relationship between our multicollinear features, like we did in [Lecture 17](https://practicaldsc.org/resources/lectures/lec17/lec17-filled.html#Redundant-features).

---

## Solving the normal equations under multicollinearity

It turns out that there are several different ways we can _try_ and solve the normal equations in Python – and many of them give different results! Let's enumerate some possibilities.


**1. Using `np.linalg.inv`**

First, we can try and use `np.linalg.inv` and try and evaluate $$\vec{w}_\text{OLS}^* = (X^TX)^{-1} X^T \vec{y}$$ directly. It's not clear why this should work, since $$X^TX$$ is **not** invertible. Nevertheless, Python gives us _some_ result!

```python
w_inv = np.linalg.inv(X_train_design.T @ X_train_design) @ X_train_design.T @ y_train
w_inv = w_inv.to_numpy()
w_inv
```

```
array([-59.93693329,   2.43212549,  10.06693352])
```

<br>

**2. Using `np.linalg.pinv`**

We can use the same approach as above, but instead use `np.linalg.pinv`, which computes the **pseudoinverse** of its argument. The pseudoinverse is the generalization of the matrix inverse to non-invertible matrices; read more [here](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse).

```python
w_pinv = np.linalg.pinv(X_train_design.T @ X_train_design) @ X_train_design.T @ y_train
w_pinv = w_pinv.to_numpy()
w_pinv
```

```
array([-82.77005461,   3.06489359,   0.25540779])
```

<br>

**3. Using `np.linalg.solve`**

We can use `np.linalg.solve` to "solve" the normal equations, $$X^TX \vec{w}_\text{OLS}^* = X^T \vec{y}$$, without needing to invert. Remember, the normal equations are a system of $$d+1$$ equations with $$d+1$$ unknowns ($$w_0^*, w_1^*, ..., w_d^*$$); here, we have $$d = 2$$ features.

```python
w_solve = np.linalg.solve(X_train_design.T @ X_train_design, X_train_design.T @ y_train)
w_solve
```

```
array([-82.77005461,   7.47197413, -52.62955865])
```

<br>

**4. Using `np.linalg.lstsq`**

We can also use `np.linalg.lstsq`. `np.linalg.lstsq(A, B)` returns the vector $$\vec{w}$$ that minimizes $$\frac{1}{n} \lVert B - A \vec{w} \rVert_2^2$$. For us, `A = X_train_design` and `B = y_train`.

```python
w_lstsq = np.linalg.lstsq(X_train_design, y_train)[0]
w_lstsq
```

```python
array([-8.27700546e+01, -3.59298640e+11,  4.31158369e+12])
```

<br>

**5. Using `sklearn`**

Finally, we can just use `sklearn`, as we've done in class and homeworks already.

```python
from sklearn.linear_model import LinearRegression

# Our design matrix already has a column of 1s, so we don't need to tell sklearn to fit an intercept.
model = LinearRegression(fit_intercept=False) 
model.fit(X_train_design, y_train)

w_sklearn = model.coef_
w_sklearn
```

```python
array([-82.77005461,   3.06489359,   0.2554078 ])
```

<br>

Hmm... all five methods were in theory solving the same problem, and so should have given us the same optimal parameter vector, $$\vec{w}_\text{OLS}^*$$, but the first four were slightly different. The last two were identical; upon further investigation, [`sklearn`'s documentation](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LinearRegression.html) shows us that LinearRegression's `fit` method just calls `np.linalg.lstsq` under the hood!

While many of the $$\vec{w}_\text{OLS}^*$$ vectors look different, many (but not all!) end up making the same predictions and have the same mean squared error. Let's take a look:

| Method | Coefficients | First 3 Rows of Hypothesis Vector | Mean Squared Error |
|--------|--------------|-----------------------------------|-------------------|
| **`np.linalg.inv`** | [-59.94, 2.43, 10.07] | 165.512<br>153.298<br>170.646 | 1354.712 |
| **`np.linalg.pinv`** | [-82.77, 3.06, 0.26] | 129.938<br>118.414<br>134.782 | 101.310 |
| **`np.linalg.solve`** | [-82.77, 7.47, -52.63] | 129.938<br>118.414<br>134.782 | 101.310 |
| **`np.linalg.lstsq`** | [-82.77, -3.59e+11, 4.31e+12] | 129.983<br>118.453<br>134.828 | 101.311 |
| **`sklearn`** | [-82.77, 3.06, 0.26] | 129.938<br>118.414<br>134.782 | 101.310 |

It seems that the last four $$\vec{w}_\text{OLS}^*$$ vectors made the same predictions and had the same minimal mean squared error of $$\approx 101.31$$, while the optimal $$\vec{w}_\text{OLS}^*$$ found using `np.linalg.inv` **wasn't** actually optimal, since it didn't have the minimal mean squared error! (There were minor differences between the last four, but these differences are attributed to the fact that the techniques use different numerical methods to solve for the necessary vectors with different stopping criteria, and due to the general imprecision of floating-point arithmetic.)

This tells us that `np.linalg.inv` does _something_ when the input matrix is not invertible, and the result isn't reliable, at least not in the context of solving the normal equations.

But generally, it seems that when the design matrix isn't full rank, we still can minimize mean squared error, it's just unclear which "optimal" parameter vector $$\vec{w}_\text{OLS}^*$$ we'll end up with, since there are infinitely many choices that minimize MSE. This is an issue if we care about interpreting the coefficients of our model.

---

## Loss surfaces

**So, how does ridge regression help with this problem?**

To illustrate, let's look at a graph of $$R_\text{ridge}(\vec{w}) = \frac{1}{n} \lVert \vec y - X \vec w \rVert_2^2 + \lambda \sum_{j = 1}^d w_j^2$$, for different values of $$\lambda$$. The graph you're about to see is also known as a _loss surface_.

Remember, our model is of the form:

$$\text{predicted Weight (Pounds)}_i = w_0 + w_1 \cdot \text{Height (Inches)}_i + w_2 \cdot \text{Height (Feet)}_i$$

There are three axes in the graph that appears:

- One for different values of $$w_1$$.
- One for different values of $$w_2$$.
- One for the value of $$R_\text{ridge}(-82.77, w_1, w_2)$$, which is the mean squared error of the model that uses an intercept of -82.77 and the provided $$w_1$$ and $$w_2$$ values as coefficients for $$\text{Height (Inches)}_i$$ and $$\text{Height (Feet)}_i$$, respectively. Since we have three parameters, we'd need four axes to truly visualize $$R_\text{ridge}(\vec{w})$$, so we've fixed a particular value of $$w_0$$. (The interesting part of the graph doesn't involve the intercept, anyways, since the multicollinearity is between the two height-related features.)

Run the cell below and interact with the slider that appears!

<center>
<iframe src="../assets/ridge-3.html" width="700" height="700" frameborder="0"></iframe>
</center>


Some things to note:
- When you drag the `reg_lambda` slider to 0, you should notice a long "ridge" at the bottom of the loss surface! All values of $$w_1$$ and $$w_2$$ that fall on that ridge minimize mean squared error. **This ridge is problematic!**
- As you increase `reg_lambda`, the surface looks more and more like a bowl curved upwards, and less "ridgy". **Ridge regression removes the ridge!**
- As you increase `reg_lambda`, look at the $$z$$-axis of the resulting plot.

So, there, we have our answer! Ridge regression removes the "ridge" of infinitely many solutions when multicollinearity is present.

What we _haven't_ really answered is **why?** Why does the ridge regression objective function always have a unique minimizer, $$\vec{w}_\text{ridge}^*$$? That's what we'll work through now.

---

## Guaranteeing a unique solution

Throughout the remainder of this guide, we'll call the regularization penalty $$\lambda_\text{ridge}$$, not just $$\lambda$$, to avoid confusion with other notation we're about to introduce.

We've just taken for granted the fact that the minimizer of the ridge regression objective function,

$$R_\text{ridge}(\vec{w}) = \frac{1}{n} \lVert \vec{y} - X \vec{w} \rVert_2^2 + \lambda_\text{ridge} \sum_{j = 1}^d w_j^2$$

is:

$$\vec{w}_\text{ridge}^* = (X^TX + n \lambda_\text{ridge} I)^{-1} X^T \vec{y}$$

In Homework 9, we'll have you prove that this indeed is the minimizer. But for now, we'll answer the question, **why is $$\vec{w}_\text{ridge}^*$$ always uniquely defined?** This problem boils down to determining why $$X^TX + n \lambda_\text{ridge} I$$ is always invertible, since the inverse of a matrix – **if it exists** – is always unique.

To prove that $$X^TX + n \lambda_\text{ridge} I$$ is always invertible, we'll need to remember how eigenvalues and eigenvectors work from linear algebra. If you don't remember (or never learned), don't worry – we'll explain everything that's relevant. (And yes, this is all relevant to understanding how ridge regression works!) Much of this content is the same as in the linear algebra guide called [Eigenvalues](../../linear-algebra/eigenvalues), though we've included all relevant pieces here.

$$\lambda_i$$ is an **eigenvalue** of square matrix $$A$$, corresponding to the **eigenvector** $$\vec{v}_i$$, if:

$$A \vec{v}_i = \lambda_i \vec{v}_i$$

In other words, $$\vec{v}_i$$ is an eigenvalue of $$A$$ if, when left-multiplied by $$A$$, its direction doesn't change, only its length. The amount $$\vec{v}_i$$'s length is scaled by is $$\lambda_i$$. We also say that $$\lambda_i$$ and $$\vec{v}_i$$ form an **eigenvalue-eigenvector pair of $$A$$**. (Note that $$\vec{0}$$ is never considered to be an eigenvector, since any matrix times $$\vec{0}$$ is always just $$\vec{0}$$.)

For example, if $$A = \begin{bmatrix} -5 & 2 \\ -7 & 4 \end{bmatrix}$$, then $$\vec{v}_1 = \begin{bmatrix} 2 \\ 7 \end{bmatrix}$$ is an eigenvector of $$A$$ corresponding to the eigenvalue $$\lambda_1 = 2$$, because:

$$A\vec{v}_1 = \begin{bmatrix} -5 & 2 \\ -7 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ 7 \end{bmatrix} = \begin{bmatrix} -5(2) + 2(7) \\ -7(2) + 4(7) \end{bmatrix} = \begin{bmatrix} 4 \\ 14 \end{bmatrix} = 2 \begin{bmatrix} 2 \\ 7 \end{bmatrix} = 2 \vec{v}_1$$

So, when $$\vec{v}_1$$ is multiplied by $$A$$, it still points in the same direction, it's just doubled in length.

**Verify yourself that $$\lambda_2 = -3$$ is also an eigenvalue of $$A$$, corresponding to the eigenvector $$\vec{v}_2 = \begin{bmatrix} 1 \\ 1\end{bmatrix}$$.** Read more about eigenvalues and eigenvectors [**here**](https://math.libretexts.org/Bookshelves/Linear_Algebra/A_First_Course_in_Linear_Algebra_(Kuttler)/07%3A_Spectral_Theory/7.01%3A_Eigenvalues_and_Eigenvectors_of_a_Matrix), though we will cover everything you need to know directly in this homework.

One more thing: an $$n \times n$$ matrix can have at most $$n$$ non-zero eigenvalues. The **rank** of a square matrix is equal to the number of non-zero eigenvalues it has. As we've discussed in class, the rank of a matrix is also equal to the number of linearly independent columns it has.

<br>

Okay, so what did we need all of that for? It's to use this fact:

<center><b>A square matrix is invertible <i>if and only if</i> none of its eigenvalues are 0.</b></center>

We will use this particular fact without proof, mostly because its proof is similar to the proof you'll do in Homework 9. If we can prove that none of $$X^TX + n \lambda_\text{ridge} I$$'s eigenvalues are 0, then we know it must be invertible, and so $$\vec{w}_\text{ridge}^*$$ is uniquely defined. This is especially useful if some of $$X^TX$$'s eigenvalues are 0, which is the case when $$X$$ (and $$X^TX$$) isn't full rank, and hence $$X^TX$$ isn't invertible.

{: .green }
**At this stage, you're ready to compute Questions 1.1-1.3 in Homework 9.**

---

## Minimizing the ridge regression objective function

After reading the section above, and completing Questions 1.1-1.3 in Homework 9, we can say with confidence that the ridge regression objective function always has a unique minimizer, even when $$X^TX$$ itself isn't invertible.

But why is the minimizer of $$R_\text{ridge}(\vec{w}) = \frac{1}{n} \lVert \vec{y} - X \vec{w} \rVert_2^2 + \lambda_\text{ridge} \sum_{j = 1}^d w_j^2$$ the vector that we're claiming it is, $$\vec{w}_\text{ridge}^* = (X^TX + n \lambda_\text{ridge} I)^{-1}X^T \vec{y}$$? 

Let's address this now. We _could_ do it using vector calculus, a tool we'll learn about in coming weeks. But, we'll approach it from a linear algebra perspective. But first, a bit more setup.

Recall, our design matrix $$X$$ and observation vector $$\vec{y}$$ are defined as follows:

$$X = \begin{bmatrix}1 & x_1^{(1)} & x_1^{(2)} & ... & x_1^{(d)} \\ 1 & x_2^{(1)} & x_2^{(2)} & ... & x_2^{(d)} \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & x_n^{(1)} & x_n^{(2)} & ... & x_n^{(d)} \end{bmatrix}_{\: n \times (d + 1)} \qquad \vec{y} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}_{\:n \times 1}$$

Recall from [Lecture 14](https://practicaldsc.org/resources/lectures/lec14/lec14-filled.pdf#page=20) that the role of the intercept term in a linear model is to shift our hypothesis surface up, ensuring that an average $$\vec{x}_i$$ predicts an average $$y_i$$. If we **mean-center** each column in our design matrix, $$X$$, and our observation vector, $$\vec{y}$$, then there's no need for an intercept term in our model, since the mean of each feature will be $$0$$ and the mean $$y$$ will also be $$0$$.

Let $$\mu_j$$ be the mean of feature/column $$j$$, and let $$\bar{y}$$ be the mean of $$\vec{y}$$. Then, **mean-centered** design matrix, $$X_c$$, and observation vector, $$\vec{y}_c$$, are defined as follows:

$$X_c = \begin{bmatrix}x_1^{(1)} - \mu_1 && x_1^{(2)} - \mu_2 && ... && x_1^{(d)} - \mu_d \\ x_2^{(1)} - \mu_1 && x_2^{(2)} - \mu_2 && ... && x_2^{(d)} - \mu_d \\ \vdots && \vdots && \vdots && \vdots \\ x_n^{(1)} - \mu_1 && x_n^{(2)} - \mu_2 && ... && x_n^{(d)} - \mu_d \end{bmatrix}_{\:n \times d} \qquad \vec{y}_c = \begin{bmatrix} y_1 - \bar{y} \\ y_2 - \bar{y} \\ \vdots \\ y_n - \bar{y} \end{bmatrix}_{\:n \times 1}$$


{: .blue }    
> **Fact**: The vector $$\vec{w}_c^*$$ that minimizes mean squared error using the centered design matrix and observation vector, $$R_\text{sq-c}(\vec{w}) = \frac{1}{n} \lVert \vec{y}_c - X_c \vec{w} \rVert_2^2$$, ends up being the same as the vector $$\vec{w}^*$$ that minimizes mean squared error for the original, uncentered $$X$$ and $$\vec{y}$$, just without the intercept term $$w_0^*$$.
>
> In other words:
>
> $$\text{components $1$ to $d$ of } \left[ (X^TX)^{-1} X^T \vec{y} \right] = (X_c^T X_c)^{-1}X^T \vec{y}_c$$
>
> **We won't prove this fact here, but you're welcome to on your own. For now, take it for granted that centering the data doesn't change any of the coefficients, just the intercept.**

```python
X = np.array([[1, 5, 3],
              [1, -1, 2.5],
              [1, 14, -3.14],
              [1, 1998, 15]])

y = np.array([1, 0, 3, 9])

np.linalg.solve(X.T @ X, X.T @ y)
```




    array([ 1.60673208,  0.00670059, -0.39950019])




```python
X_c = X - X.mean(axis=0)
X_c
```




    array([[ 0.000e+00, -4.990e+02, -1.340e+00],
           [ 0.000e+00, -5.050e+02, -1.840e+00],
           [ 0.000e+00, -4.900e+02, -7.480e+00],
           [ 0.000e+00,  1.494e+03,  1.066e+01]])




```python
X_c = X_c[:, 1:]
X_c
```




    array([[-4.990e+02, -1.340e+00],
           [-5.050e+02, -1.840e+00],
           [-4.900e+02, -7.480e+00],
           [ 1.494e+03,  1.066e+01]])




```python
y_c = y - y.mean()
y_c
```




    array([-2.25, -3.25, -0.25,  5.75])




```python
np.linalg.solve(X_c.T @ X_c, X_c.T @ y)
```




    array([ 0.00670059, -0.39950019])


You should notice that the coefficients of 0.00670059 and -0.39950019 are the same as we saw in the call to `np.linalg.solve(X.T @ X, X.T @ y)`.

<br>

Okay – one last set of definitions. Again, this all has a purpose! We define the **adjusted** design matrix and observation vector – $$X_\text{adj}$$ and $$\vec{y}_\text{adj}$$, respectively – as follows:

$$X_\text{adj} = \begin{bmatrix} X_c \\ \sqrt{n \lambda_\text{ridge}}\cdot I_{d \times d} \end{bmatrix} = \begin{bmatrix}x_1^{(1)} - \mu_1 && x_1^{(2)} - \mu_2 && ... && x_1^{(d)} - \mu_d \\ x_2^{(1)} - \mu_1 && x_2^{(2)} - \mu_2 && ... && x_2^{(d)} - \mu_d \\ \vdots && \vdots && \vdots && \vdots \\ x_n^{(1)} - \mu_1 && x_n^{(2)} - \mu_2 && ... && x_n^{(d)} - \mu_d \\ \sqrt{n \lambda_\text{ridge}} && 0 && ... && 0 \\ 0 && \sqrt{n \lambda_\text{ridge}} && ... && 0 \\ \vdots && \vdots && ... && \vdots \\ 0 && 0 && ... && \sqrt{n \lambda_\text{ridge}} \end{bmatrix}_{\:(n + d) \times d} \qquad \vec{y}_\text{adj} = \begin{bmatrix}y_c \\ \vec 0_{d \times 1} \end{bmatrix} = \begin{bmatrix} y_1 - \bar{y} \\ y_2 - \bar{y} \\ \vdots \\ y_n - \bar{y} \\ 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix}_{\:(n + d) \times 1}$$

In short:
- To create $$X_\text{adj}$$, we take $$X_c$$ and "append" to the bottom a $$d \times d$$ diagonal matrix, with 0s everywhere except the diagonal, which contains $$\sqrt{n \lambda_\text{ridge}}$$.
- To create $$\vec{y}_\text{adj}$$, we take $$\vec{y}_c$$ and add $$d$$ new values to the bottom, all of which are 0.

**It turns out that we can use $$X_\text{adj}$$ and $$\vec{y}_\text{adj}$$ to show why the ridge regression objective function is minimized by $$\left(X_c^TX_c + n\lambda_\text{ridge} I \right)^{-1}X_c^T \vec{y_c}$$, which (ignoring the intercept term, which isn't regularized) is the same as $$\left(X^TX + n \lambda_\text{ridge} I \right)^{-1} X^T \vec{y}$$.**

The high-level gist is that:

$$\text{the $\vec{w}^*$ that minimizes} \frac{1}{n} \lVert \vec{y}_c - X_c \vec{w} \rVert_2^2 + \lambda_\text{ridge} \sum_{j = 1}^d w_j^2$$

$$\text{is equal to}$$

$$\text{the $\vec{w}^*$ that minimizes} \frac{1}{n} \lVert \vec{y}_\text{adj} - X_\text{adj} \vec{w} \rVert_2^2$$

$$\text{both of which are } \left(X_c^TX_c + n\lambda_\text{ridge} I \right)^{-1}X_c^T \vec{y_c}$$

Or, in simpler terms: suppose we have two functions, $$f(w)$$ and $$g(w)$$. If we can show that $$f(w) = g(w)$$, for all $$w$$, then the $$w$$ that minimizes $$f(w)$$ is also the $$w$$ that minimizes $$g(w)$$.

<br>

---

## The final derivation

{: .blue }
> We'll break the derivation down into four steps:
> 1. Show that $$X_\text{adj}^TX_\text{adj} = X_c^TX_c + n \lambda_\text{ridge} I$$.
> 1. Show that $$X_\text{adj}^T \vec{y}_\text{adj} = X_c^T \vec{y}_c$$.
> 1. Show that $$\frac{1}{n} \lVert \vec{y}_{\text{adj}} - X_{\text{adj}} \vec{w} \rVert_2^2 = \frac{1}{n} \lVert \vec{y}_c - X_c \vec{w} \rVert_2^2 + \lambda_\text{ridge} \sum_{j = 1}^d w_j^2$$.
> 1. Put everything together to demonstrate why $$\left(X_c^TX_c + n\lambda_\text{ridge} I \right)^{-1}X_c^T \vec{y_c}$$ minimizes the ridge regression objective function.

We'll work through Step 1 below, but you'll do Steps 2-4 in Questions 1.4-1.6 of Homework 9.

Step 1 is to show that:

$$X_\text{adj}^TX_\text{adj} = X_c^TX_c + n \lambda_\text{ridge} I$$

Note that both of these look like the sort of terms we invert, when doing non-regularized linear regression ($$X_\text{adj}^TX_\text{adj}$$) and ridge regression ($$X_c^TX_c + n \lambda_\text{ridge} I$$) respectively.

Let's examine what the product and shapes are. **Here, suppose $$\vec{x^{(i)}}$$ represents column $$i$$ of $$X_c$$, i.e. $$\vec{x^{(i)}}$$ is already centered.**

$$
X^T_\text{adj} X_\text{adj} = \begin{bmatrix} \rule[.5ex]{1.5em}{0.4pt} \ \vec{x^{(1)}} \ \rule[.5ex]{1.5em}{0.4pt} & \sqrt{n\lambda_\text{ridge}}  & 0 & \dots & \dots\\ 
\rule[.5ex]{1.5em}{0.4pt} \ \vec{x^{(2)}} \ \rule[.5ex]{1.5em}{0.4pt} & 0 & \sqrt{n\lambda_\text{ridge}}  & \dots  & \dots\\ 
\dots & \dots & \dots & \dots & \dots \\
\rule[.5ex]{1.5em}{0.4pt} \ \vec{x^{(d)}} \ \rule[.5ex]{1.5em}{0.4pt} & 0 & 0 &  \dots & \sqrt{n\lambda_\text{ridge}}
\end{bmatrix}_{\:d \times (n+d)} 
\begin{bmatrix}  | & | & \dots & | \\ \vec{x^{(1)}} & \vec{x^{(2)}} & \dots & \vec{x^{(d)}} \\ | & | & \dots & | \\
\sqrt{n\lambda_\text{ridge}} & 0 & \dots & \dots \\ 
0 & \sqrt{n\lambda_\text{ridge}} & \dots & \dots \\ 
\dots & \dots & \dots & \sqrt{n\lambda_\text{ridge}} \\
\end{bmatrix}_{\:(n+d) \times d}
$$

What do we know about the product, $$X_\text{adj}^T X_\text{adj}$$?

- It has shape $$d \times d$$, just like $$X_c^T X_c$$.
- Each element in $$X_\text{adj}^T X_\text{adj}$$ is a **dot product** between a row in $$X_\text{adj}^T$$ and a column in $$X_\text{adj}$$. But since the rows of $$X_\text{adj}^T$$ are just the columns of $$X_\text{adj}$$, each element in $$X_\text{adj}^T X_\text{adj}$$ is a **dot product between two columns of $$X_\text{adj}$$**.
- In general, the number at position $$(i, j)$$ in $$X_\text{adj}^T X_\text{adj}$$ is the dot product between column $$i$$ of $$X_\text{adj}$$ and column $$j$$ of $$X_\text{adj}$$. 

There are two cases to consider:

**Case 1**: $$i = j$$. Here, we're taking a dot product between two identical vectors of shape $$(n + d) \times 1$$:

$$\begin{bmatrix}  | \\  \vec{x^{(i)}} \\ | \\ 0 \\ \vdots \\ \sqrt{n \lambda_\text{ridge}} \\ 0 \\ \vdots \\ 0 \end{bmatrix} \cdot \begin{bmatrix}  | \\  \vec{x^{(i)}} \\ | \\ 0 \\ \vdots \\ \sqrt{n \lambda_\text{ridge}} \\ 0 \\ \vdots \\ 0 \end{bmatrix}$$

Here, the dot product in the first $$n$$ components, $$\sum_{p = 1}^n x_p^{(i)} \times x_p^{(i)}$$, is just the dot product of $$\vec{x^{(i)}}$$ with $$\vec{x^{(i)}}$$. Looking at the latter $$d$$ components, both vectors have the value 0 in $$d - 1$$ of those components, with a non-zero value of $$\sqrt{n \lambda_\text{ridge}}$$ **in the same position**. So, the dot product of column $$i$$ with column $$i$$ in $$X_\text{adj}^T X_\text{adj}$$ ends up being:

$$\vec{x^{(i)}} \cdot \vec{x^{(i)}} + n \lambda_\text{ridge}$$

Note that this is equal to the dot product of column $$i$$ with column $$i$$ as computed in $$X_c^T X_c$$, just with the term $$\sqrt{n \lambda_\text{ridge}}$$ added.

**Case 2**: $$i \neq j$$. The difference here is that the $$\sqrt{n \lambda_\text{ridge}}$$ in the two vectors won't be in the same position. Rather, their dot product will look something like:

$$\begin{bmatrix}  | \\  \vec{x^{(i)}} \\ | \\ 0 \\ \vdots \\ \sqrt{n \lambda_\text{ridge}} \\ 0 \\ \vdots \\ 0 \end{bmatrix} \cdot \begin{bmatrix}  | \\  \vec{x^{(j)}} \\ | \\ 0 \\ \vdots \\ 0 \\ \sqrt{n \lambda_\text{ridge}} \\ \vdots \\ 0 \end{bmatrix}$$

The dot product of column $$i$$ with column $$j$$ in $$X_\text{adj}^T X_\text{adj}$$ ends up being just $$\vec{x^{(i)}} \cdot \vec{x^{(j)}}$$, i.e, **no different** than in $$X_c^T X_c$$, since the $$\sqrt{n \lambda_\text{ridge}}$$ in each column ends up being multiplied by a 0 in the other column.

So, putting this together, the terms of $$X_\text{adj}^T X_\text{adj}$$ are the same as the terms of $$X_c^T X_c$$, **the only difference being that** the diagonal terms (where $$i = j$$, i.e. row number = column number) have $$n \lambda_\text{ridge}$$ added to them. To represent this, we can take $$X_c^T X_c$$ and add the identity matrix, $$I_{d \times d} = \begin{bmatrix} 1 & 0 & ... & 0 \\ 0 & 1 & ... & 0 \\ \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & ... & 1 \end{bmatrix}$$, which is already diagonal with the same constant in every position, multiplied by $$n \lambda_\text{ridge}$$. 

This means that: $$X_\text{adj}^T X_\text{adj} = X_c^T X_c + n \lambda_\text{ridge} I$$

As needed!

{: .green }
**At this stage, you're ready to compute Questions 1.4-1.6 in Homework 9. But, before proceeding, revisit our outline of what Steps 1-4 of this derivation are so you're clear on what the purpose of this step was, and what comes next.**