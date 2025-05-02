---
layout: page
title: DataFrame Internals
description: >-
  Mutability and data types, as they pertain to DataFrames.
parent: 🐼 Data Wrangling
grand_parent: 🧑‍🤝‍🧑 Guides
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

In [Lecture 4](../../../resources/lectures/lec04/lec04-filled.html), we discussed the three main data structures in `pandas`:

<center><img src="../assets/df-anatomy.png" width="80%"></center>

- **DataFrame**: 2 dimensional tables. These have rows and columns.
- **Series**: 1 dimensional array-like object, representing a row or column.
<!-- <br><small>Like arrays, Series contain data of the same type. The plural of Series is also Series.</small> -->
- **Index**: Sequence of row or column labels. When we say "the index", we're referring to the sequence of row labels.
<!-- <br><small>The index – 'lebronja', 'obammich', 'carpents', and 'timapplec' in the example above – is not a column!<br>
Column names – 'name', 'program', and 'year' in the example above – are stored as strings, and the sequence of column names is also an index.</small> -->

We were exposed to several DataFrame methods, like  `head`, `tail`, `sort_values`, and `set_index`, and Series methods, like `mean`, `value_counts`, and `argmax` (to name a few; see the [`pandas` documentation](https://pandas.pydata.org/docs/reference/frame.html) for more).

We also learned about a few key techniques for accessing data in DataFrames; in particular, we learned that:
- `loc` is used to extract a subset of rows and columns from a DataFrame, given their **index** values.
- `iloc` is used to extract a subset of rows and columns from a DataFrame, given their **integer positions**.
- The square brackets operator, used **without** `loc` or `iloc`, can either be used to select an individual column **or** to perform a **query**, where we select a subset of rows that satisfy particular conditions.

In this guide, we'll discuss some of the details of _how_ DataFrames are stored in memory, and how that might influence the way you interact with them in homeworks. In previous semesters, we'd show this material in lecture, but we felt that it's better served as reference notes, and that lecture time is better spent on activities that involve conceptual problem solving.

---

## Consequences of mutability

DataFrames, like lists, arrays, dictionaries, Series, and indexes, are **mutable**, meaning that they can be modified in-place after instantiation. A consequence of this is that DataFrames can be inadvertently modified in unexpected ways. To illustrate, we'll look at a common operation: adding a new column. We'll continue using the `dogs` DataFrame from Lecture 4.

```python
dogs.head()
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
      <th>kind</th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>size</th>
      <th>weight</th>
      <th>height</th>
    </tr>
    <tr>
      <th>breed</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brittany</th>
      <td>sporting</td>
      <td>22589.0</td>
      <td>12.92</td>
      <td>medium</td>
      <td>35.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>Cairn Terrier</th>
      <td>terrier</td>
      <td>21992.0</td>
      <td>13.84</td>
      <td>small</td>
      <td>14.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>English Cocker Spaniel</th>
      <td>sporting</td>
      <td>18993.0</td>
      <td>11.66</td>
      <td>medium</td>
      <td>30.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>Cocker Spaniel</th>
      <td>sporting</td>
      <td>24330.0</td>
      <td>12.50</td>
      <td>small</td>
      <td>25.0</td>
      <td>14.5</td>
    </tr>
    <tr>
      <th>Shetland Sheepdog</th>
      <td>herding</td>
      <td>21006.0</td>
      <td>12.53</td>
      <td>small</td>
      <td>22.0</td>
      <td>14.5</td>
    </tr>
  </tbody>
</table>
</div>

Note that the DataFrame above only has 6 columns – `'kind'`, `'lifetime_cost'`, `'longevity'`, `'size'`, `'weight'`, and `'height'`. `'breed'` is **not** a column; rather, it's stored in the `'index'`. The string `'breed'` appears above the index because it was carried over from when `'breed'` initially was a column; recall, in lecture, we manually set the index of `dogs` to `'breed'`. The fact that it says `'breed'` above the index does not change the fact that `'breed'` is not one of the columns.

<br>

### Adding columns using `[]`

The most common way to add or modify columns to a DataFrame is using the `[]` operator, which we also use to access columns. This works like dictionary assignment. (By "modify" a column, we mean replace an existing column with a new column of the same name.)

Using `[]` to add or modify columns is **destructive**, meaning it changes the underlying DataFrame in memory. Let's demonstrate. Suppose we add a `'cost_per_year'` column to `dogs` using the `[]` operator.

```python
dogs['cost_per_year'] = dogs['lifetime_cost'] / dogs['longevity']
```

Note that we never explicitly re-assigned `dogs` in the cell above, i.e. we never wrote `dogs = ...`. **But, `dogs` was still modified**! Scroll to the right below and you'll see that `dogs` now has a `'cost_per_year'` column.

```python
dogs.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kind</th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>size</th>
      <th>weight</th>
      <th>height</th>
      <th>cost_per_year</th>
    </tr>
    <tr>
      <th>breed</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brittany</th>
      <td>sporting</td>
      <td>22589.0</td>
      <td>12.92</td>
      <td>medium</td>
      <td>35.0</td>
      <td>19.0</td>
      <td>1748.37</td>
    </tr>
    <tr>
      <th>Cairn Terrier</th>
      <td>terrier</td>
      <td>21992.0</td>
      <td>13.84</td>
      <td>small</td>
      <td>14.0</td>
      <td>10.0</td>
      <td>1589.02</td>
    </tr>
    <tr>
      <th>English Cocker Spaniel</th>
      <td>sporting</td>
      <td>18993.0</td>
      <td>11.66</td>
      <td>medium</td>
      <td>30.0</td>
      <td>16.0</td>
      <td>1628.90</td>
    </tr>
    <tr>
      <th>Cocker Spaniel</th>
      <td>sporting</td>
      <td>24330.0</td>
      <td>12.50</td>
      <td>small</td>
      <td>25.0</td>
      <td>14.5</td>
      <td>1946.40</td>
    </tr>
    <tr>
      <th>Shetland Sheepdog</th>
      <td>herding</td>
      <td>21006.0</td>
      <td>12.53</td>
      <td>small</td>
      <td>22.0</td>
      <td>14.5</td>
      <td>1676.46</td>
    </tr>
  </tbody>
</table>

<br>

In and of itself, this doesn't seem like the _worst_ thing in the world. But, the fact that DataFrames are mutable can have even more unintended consequences. For instance, consider the function `cost_in_thousands`, defined below.

```python
# Note that cost_in_thousands doesn't return anything.
def cost_in_thousands(df):
    df['lifetime_cost'] = df['lifetime_cost'] / 1000
```

Suppose `dogs` is now a fresh copy of the `dogs` DataFrame, i.e. one without a `'cost_per_year'` column. And suppose we run the following cell **twice**:

```python
cost_in_thousands(dogs)
```

Even though we never explicitly re-assigned `dogs`, it was modified – twice.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kind</th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>size</th>
      <th>weight</th>
      <th>height</th>
    </tr>
    <tr>
      <th>breed</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brittany</th>
      <td>sporting</td>
      <td>0.02</td>
      <td>12.92</td>
      <td>medium</td>
      <td>35.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>Cairn Terrier</th>
      <td>terrier</td>
      <td>0.02</td>
      <td>13.84</td>
      <td>small</td>
      <td>14.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>English Cocker Spaniel</th>
      <td>sporting</td>
      <td>0.02</td>
      <td>11.66</td>
      <td>medium</td>
      <td>30.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>Cocker Spaniel</th>
      <td>sporting</td>
      <td>0.02</td>
      <td>12.50</td>
      <td>small</td>
      <td>25.0</td>
      <td>14.5</td>
    </tr>
    <tr>
      <th>Shetland Sheepdog</th>
      <td>herding</td>
      <td>0.02</td>
      <td>12.53</td>
      <td>small</td>
      <td>22.0</td>
      <td>14.5</td>
    </tr>
  </tbody>
</table>

The values in the `'lifetime_cost'` above aren't just their original values divided by $$1000$$, but they are their original values divided by $$1000 \cdot 1000 = 1000000$$! You may ask, why would we ever run the cell `cost_in_thousands(dogs)` twice? On purpose, we probably wouldn't, but when you have hundreds of cells in front of you, it's common to inadvertently run a cell multiple times, and it's best practice to structure your code such that **no matter how many times it's run, the results and consequences are the same**.

{: .red }
Moral of the story: avoid mutation when possible!

<br>

We're about to show you another non-destructive technique for adding or modifying columns. But, since the `[]` technique is so common, we'll leave you with a word of advice: when implementing functions that take in DataFrames, it's a good idea to include `df = df.copy()` as the first line. `df.copy()` returns a **deep copy** of `df`, which is a new DataFrame with the same content as `df`, but a different memory address. This way, the changes you make to `df` within the body of the function won't impact any input DataFrames in your global scope.

```python
# Better than before!
# Now, when cost_in_thousands is called,
# it won't make destructive modifications to the DataFrame it is called on.
# Since it doesn't return anything, it won't actually do anything, then.
def cost_in_thousands(df):
    df = df.copy()
    df['lifetime_cost'] = df['lifetime_cost'] / 1000
```

### Adding columns using `assign`

A non-destructive way to add a new column to a DataFrame is to use the `assign` DataFrame method. Like most other DataFrame methods we saw in Lecture 4 (and will see in the subsequent lectures), `assign` returns a new DataFrame, and leaves the original DataFrame untouched. The downside to this is that it is not very space efficient, as it creates a new copy in memory each time it's called.

The `assign` method creates new columns using Python's named keyword argument syntax. If the column name we're trying to add already exists, `assign` will replace the old column with the new one. In general, we say:

```python
df.assign(name_of_new_column=values_in_new_column)
```

To illustrate, suppose `dogs` is now a fresh copy of the original DataFrame loaded in at the start of this guide. The following expression returns a new DataFrame with all of the columns in `dogs`, plus a new `'cost_per_year'` column.

```python
dogs.assign(cost_per_year=dogs['lifetime_cost'] / dogs['longevity'])
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kind</th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>size</th>
      <th>weight</th>
      <th>height</th>
      <th>cost_per_year</th>
    </tr>
    <tr>
      <th>breed</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brittany</th>
      <td>sporting</td>
      <td>22589.0</td>
      <td>12.92</td>
      <td>medium</td>
      <td>35.0</td>
      <td>19.0</td>
      <td>1748.37</td>
    </tr>
    <tr>
      <th>Cairn Terrier</th>
      <td>terrier</td>
      <td>21992.0</td>
      <td>13.84</td>
      <td>small</td>
      <td>14.0</td>
      <td>10.0</td>
      <td>1589.02</td>
    </tr>
    <tr>
      <th>English Cocker Spaniel</th>
      <td>sporting</td>
      <td>18993.0</td>
      <td>11.66</td>
      <td>medium</td>
      <td>30.0</td>
      <td>16.0</td>
      <td>1628.90</td>
    </tr>
    <tr>
      <th>Cocker Spaniel</th>
      <td>sporting</td>
      <td>24330.0</td>
      <td>12.50</td>
      <td>small</td>
      <td>25.0</td>
      <td>14.5</td>
      <td>1946.40</td>
    </tr>
    <tr>
      <th>Shetland Sheepdog</th>
      <td>herding</td>
      <td>21006.0</td>
      <td>12.53</td>
      <td>small</td>
      <td>22.0</td>
      <td>14.5</td>
      <td>1676.46</td>
    </tr>
  </tbody>
</table>

But, `dogs` itself is still unchanged:

```python
dogs
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
      <th>kind</th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>size</th>
      <th>weight</th>
      <th>height</th>
    </tr>
    <tr>
      <th>breed</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brittany</th>
      <td>sporting</td>
      <td>22589.0</td>
      <td>12.92</td>
      <td>medium</td>
      <td>35.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>Cairn Terrier</th>
      <td>terrier</td>
      <td>21992.0</td>
      <td>13.84</td>
      <td>small</td>
      <td>14.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>English Cocker Spaniel</th>
      <td>sporting</td>
      <td>18993.0</td>
      <td>11.66</td>
      <td>medium</td>
      <td>30.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>Cocker Spaniel</th>
      <td>sporting</td>
      <td>24330.0</td>
      <td>12.50</td>
      <td>small</td>
      <td>25.0</td>
      <td>14.5</td>
    </tr>
    <tr>
      <th>Shetland Sheepdog</th>
      <td>herding</td>
      <td>21006.0</td>
      <td>12.53</td>
      <td>small</td>
      <td>22.0</td>
      <td>14.5</td>
    </tr>
  </tbody>
</table>
</div>

You can also use `assign` when the desired column name has spaces (and other special characters) by unpacking a dictionary:

```python
dogs.assign(**{'cost per year 💵': dogs['lifetime_cost'] / dogs['longevity']})
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kind</th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>size</th>
      <th>weight</th>
      <th>height</th>
      <th>cost per year 💵</th>
    </tr>
    <tr>
      <th>breed</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brittany</th>
      <td>sporting</td>
      <td>22589.0</td>
      <td>12.92</td>
      <td>medium</td>
      <td>35.0</td>
      <td>19.0</td>
      <td>1748.37</td>
    </tr>
    <tr>
      <th>Cairn Terrier</th>
      <td>terrier</td>
      <td>21992.0</td>
      <td>13.84</td>
      <td>small</td>
      <td>14.0</td>
      <td>10.0</td>
      <td>1589.02</td>
    </tr>
    <tr>
      <th>English Cocker Spaniel</th>
      <td>sporting</td>
      <td>18993.0</td>
      <td>11.66</td>
      <td>medium</td>
      <td>30.0</td>
      <td>16.0</td>
      <td>1628.90</td>
    </tr>
    <tr>
      <th>Cocker Spaniel</th>
      <td>sporting</td>
      <td>24330.0</td>
      <td>12.50</td>
      <td>small</td>
      <td>25.0</td>
      <td>14.5</td>
      <td>1946.40</td>
    </tr>
    <tr>
      <th>Shetland Sheepdog</th>
      <td>herding</td>
      <td>21006.0</td>
      <td>12.53</td>
      <td>small</td>
      <td>22.0</td>
      <td>14.5</td>
      <td>1676.46</td>
    </tr>
  </tbody>
</table>

To have any of these changes persist, we'd need to explicitly re-assign `dogs` to this DataFrame.

```python
dogs = dogs.assign(cost_per_year=dogs['lifetime_cost'] / dogs['longevity'])
```

Admittedly, this syntax is a bit convoluted – especially when adding columns whose names have spaces – and the `[]` operator is more convenient. It just comes with side effects that you should be aware of.

<br>

### Chained indexing

Consider the following example DataFrame, `A`.

```python
A = pd.DataFrame().assign(
    x=[1, 2, 3],
    y=[4, 4, 5]
)
A
```

<table border="1" class="dataframe" style="width: 100px !important;">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

Suppose we need to set the values of `'y'` when `'x'` is greater than 1 to 3. There are a few ways to attempt this:

1. `A[A['x'] > 1]['y'] = 3`
1. `A.loc[A['x'] > 1, 'y'] = 3`

It turns out that only the second line would work, **not** the first. In short, the reason is that because in the first method, `A[A['x'] > 1]` returns a **new** DataFrame, detached from `A`, and the `['y'] = 3` piece sets the corresponding `'y'` values of that new DataFrame to 3. It doesn't change `A`, like the second line does.

The first line uses what is called "chained indexing", which generally should be avoided. If all we were trying to do was access the `'y'` values for which `'x'` is greater than 1, then both `A[A['x'] > 1]['y']` and `A.loc[A['x'] > 1, 'y']` would give us equivalent results, but because the former technique _can_ lead to problems when used for assignment, it's best to avoid it in general.

To read more about this nuance, and the famed `SettingWithCopyWarning` in `pandas`, read:
- The [`pandas` documentation section called "Returning a view versus a copy"](https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy).
- This [StackOverflow post](https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas).

---

## Pandas and NumPy

`pandas` is built upon `numpy`, and both `pandas` and `numpy` are part of a larger Python scientific computing ecosystem of packages. This rich ecosystem is part of why Python is so popular in different domains.

<center><img src="../assets/python-stack.png" width="60%"></center>


In particular, a Series is a (`numpy`) array with an index, and a DataFrame can be thought of as a dictionary of columns, each of which is an array.

Many operations in `pandas` are fast because they use `numpy`'s implementations, which are written in fast, compiled languages like C and Fortran. If you need to access the array underlying a DataFrame or Series, use the `to_numpy` method.

```python
dogs['lifetime_cost']
```

```
breed
Brittany                  22589.0
Cairn Terrier             21992.0
English Cocker Spaniel    18993.0
                           ...   
Bullmastiff               13936.0
Mastiff                   13581.0
Saint Bernard             20022.0
Name: lifetime_cost, Length: 43, dtype: float64
```

<br>

```python
dogs['lifetime_cost'].to_numpy()
```

```
array([22589., 21992., 18993., ..., 13936., 13581., 20022.])
```

<br>

### `pandas` data types

Each Series has a `numpy` data type, which refers to the type of the values stored within. Remember that each column (and row) in a DataFrame is stored as a Series.

The data type of `dogs['lifetime_cost']` is `float64`, as you can see in the last line of the Series' preview above. This is the `pandas`/`numpy` version of the vanilla Python `float` data type, and you'll run into it frequently in your autograder tests. 

You can programmatically access the data type of a Series using the `dtype` attribute:

```python
dogs['lifetime_cost'].dtype
```

```
dtype('float64')
```

The DataFrame `dtypes` attribute shows you the data types of all columns in the DataFrame:

```python
dogs.dtypes
```

```
kind              object
lifetime_cost    float64
longevity        float64
size              object
weight           float64
height           float64
dtype: object
```

The `object` data type usually refers to strings, but can be thought of as a catch-all data type that refers to anything that's non-numeric.

<br>

A Series' data type determines which operations can be applied to it. When creating a DataFrame using `pd.read_csv`, `pandas` tries to guess the correct data types for a given DataFrame, and is often wrong. This can lead to incorrect calculations and poor memory/time performance. As a result, you may need to explicitly convert between data types.

To change the data type of a Series, use the `astype` method. For instance, if `s` was a Series of strings that you wanted to convert to integers, use `s.astype(int)`.

Sometimes, changing the data type of a Series can lead to performance benefits. The DataFrame `info` method shows us all of the information that the `dtypes` attribute does, as well as the space taken up by the DataFrame.

```python
dogs.info()
```

```
<class 'pandas.core.frame.DataFrame'>
Index: 42 entries, Brittany to Saint Bernard
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   kind           42 non-null     object 
 1   lifetime_cost  42 non-null     float64
 2   longevity      42 non-null     float64
 3   size           42 non-null     object 
 4   weight         42 non-null     float64
 5   height         42 non-null     float64
dtypes: float64(4), object(2)
memory usage: 2.4+ KB
```

<br>

The `'lifetime_cost'` column currently has a data type of `float64`, but all of the values are integers between $$13581$$ and $$26686$$. We _could_ set the data type of `'lifetime_cost'` to `uint16`, which stands for unsigned 16-bit integers, which can represent values from 0 to $$2^{16} - 1 = 65535$$. In practice, we probably wouldn't do this, because any operations involving the new `'lifetime_cost'` are at risk of [numerical overflow](https://en.wikipedia.org/wiki/Integer_overflow), but we could still try, because doing so saves some space:

```python
dogs['lifetime_cost'] = dogs['lifetime_cost'].astype('uint16') # Notice the quotes!
dogs.info()
```

```
<class 'pandas.core.frame.DataFrame'>
Index: 42 entries, Brittany to Saint Bernard
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   kind           42 non-null     object 
 1   lifetime_cost  42 non-null     uint16 
 2   longevity      42 non-null     float64
 3   size           42 non-null     object 
 4   weight         42 non-null     float64
 5   height         42 non-null     float64
dtypes: float64(3), object(2), uint16(1)
memory usage: 2.1+ KB
```

Here, we saved 0.3 KB, or $$\left( 1 - \frac{2.1}{2.4} \right) \cdot 100\% = 12.5\%$$ of space. These memory savings are insignificant in our humble 42 row DataFrame, but such changes can have a serious impact when working with large-scale datasets.

You can also set the data type of a column when loading it in, to prevent ever instantiating the inefficient representation:

```python
pd.read_csv(file_path, dtype={'lifetime_cost': 'uint16'})
```

<br>

The table below summarizes key data types in Python, `numpy`, and `pandas` (the latter two have subtle differences). Most importantly, notice that Python `str` types are `object` types in `numpy` and `pandas`.

|Pandas data type|Python type|NumPy data type|SQL type|Usage|
|---|---|---|---|---|
|int64|int|int_, int8,...,int64, uint8,...,uint64|INT, BIGINT| Integer numbers|
|float64|float|float_, float16, float32, float64|FLOAT| Floating point numbers|
|bool|bool|bool_|BOOL|True/False values|
|datetime64 or Timestamp|datetime.datetime|datetime64|DATETIME|Date and time values|
|timedelta64 or Timedelta|datetime.timedelta|timedelta64|NA|Differences between two datetimes|
|category|NA|NA|ENUM|Finite list of text values|
|object|str|string, unicode|NA|Text|
|object|NA|object|NA|Mixed types|

For extra reading:
- [This article](https://www.dataquest.io/blog/pandas-big-data/) details how `pandas` stores different data types under the hood.
- [This article](https://mortada.net/can-integer-operations-overflow-in-python.html#Can-integers-overflow-in-python?) explains how `numpy`/`pandas` `int64` operations differ from vanilla `int` operations.

<br>

### Axes

As we've mentioned before, the rows and columns of a DataFrame are both stored as Series. In [Lecture 4](../../../resources/lectures/lec04/lec04-filled.html), we learned about several Series methods, like `mean`, `value_counts`, and `argmax`.

<center><img src="../assets/axis.png" width="30%"></center>

It turns out many of these methods also work on DataFrames, too, with one caveat – we need to be careful to describe whether we want the method to be used on:
- every column of the DataFrame, i.e. **across `axis=0`**, or 
- on every row of the DataFrame, i.e. **across `axis=1`**.

These axis definitions are the same ones that 2D `numpy` arrays have, that we first saw in [Lecture 3](../../../resources/lectures/lec03/lec03-filled.html).

<br>

The Series methods that also work with DataFrames **usually** use `axis=0` as a default. Let's illustrate with a few examples. To find the maximum element in each column, we can use:

```python
dogs.max()
```

```
kind             working
lifetime_cost      26686
longevity           16.5
size               small
weight             175.0
height              30.0
dtype: object
```

Adding `axis=0` in the above would not have changed the result.

<br>

On the other hand, if we want the maximum element in each row, we'd use `axis=1`. However, `dogs.max(axis=1)` won't work directly, since that'd require us to compare numbers (like `15.0`) to strings (like `'working'`). So, we'll first select the numeric columns out of `dogs`. Note that while this _works_, the results are a little nonsensical, since the values in each column are on different scales.

```python
dogs[['lifetime_cost', 'longevity', 'weight', 'height']].max(axis=1)
```

```
breed
Brittany                  22589.0
Cairn Terrier             21992.0
English Cocker Spaniel    18993.0
                           ...   
Bullmastiff               13936.0
Mastiff                   13581.0
Saint Bernard             20022.0
Length: 42, dtype: float64
```

A shortcut to `dogs[['lifetime_cost', 'longevity', 'weight', 'height']]` is `dogs.select_dtypes(include='number')`.

<br>

As another example, to find the number of _unique_ values in each column:
```python
dogs.nunique()
```

```
kind              7
lifetime_cost    42
longevity        40
size              3
weight           37
height           30
dtype: int64
```

or row:

```python
dogs.nunique(axis=1)
```

```
breed
Brittany                  6
Cairn Terrier             6
English Cocker Spaniel    6
                         ..
Bullmastiff               6
Mastiff                   6
Saint Bernard             6
Length: 42, dtype: int64
```

<br>

And, finally, to get summary statistics for each numeric column:
```python
dogs.describe()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lifetime_cost</th>
      <th>longevity</th>
      <th>weight</th>
      <th>height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>42.00</td>
      <td>42.00</td>
      <td>42.00</td>
      <td>42.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>20532.84</td>
      <td>11.34</td>
      <td>49.35</td>
      <td>18.34</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3290.78</td>
      <td>2.05</td>
      <td>39.42</td>
      <td>6.83</td>
    </tr>
    <tr>
      <th>min</th>
      <td>13581.00</td>
      <td>6.50</td>
      <td>5.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>18508.50</td>
      <td>10.05</td>
      <td>18.00</td>
      <td>11.75</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>21006.00</td>
      <td>11.81</td>
      <td>36.50</td>
      <td>18.50</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>22072.50</td>
      <td>12.52</td>
      <td>67.50</td>
      <td>25.00</td>
    </tr>
    <tr>
      <th>max</th>
      <td>26686.00</td>
      <td>16.50</td>
      <td>175.00</td>
      <td>30.00</td>
    </tr>
  </tbody>
</table>

Give this guide a read, and refer back to it if you run into behavior you weren't expecting while working a homework.