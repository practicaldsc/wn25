---
layout: page
title: SQL and Spreadsheets
description: >-
  Translating our pandas knowledge to other table manipulation paradigms.
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

### Representations of tabular data

In this class, we've worked with DataFrames in `pandas`.
- When we say `pandas` DataFrame, we're talking about the `pandas` API for its DataFrame objects.
- When we say "DataFrame", we're referring to a general way to represent data. Specifically, DataFrames organize data into rows and columns, with labels for both rows and columns.

There many other ways to work with data tables, each of which have their pros and cons.<br><small>Some examples include R data frames, SQL databases, spreadsheets in Google Sheets/Excel, or even matrices from linear algebra.</small>

Below, we discuss pros and cons of (some of) the ways we can work with tabular data.

| Platform               | **Pros ✅**                                          | **Cons ❌**                                            |
|------------------------|--------------------------------------------------|----------------------------------------------------|
| **`pandas` DataFrames**   | Works well with the Python ecosystem (for visualization, machien learning, domain-specifc purposes, etc.), extremely flexible, reproducible steps  | Steep learning curve (need to know Python too) and messy code, easy to make destructive in-place modifications, no persistence (everything starts from a `CSV` file)  |
| **R data frames**        | Designed specifically for data science so statistics and visualizations are easy; reproducible steps | R isn't as general-purpose as Python, no persistence  |
| **SQL**                | Scalable, good for maintaining many large, important datasets with many concurrent users | Requires lots of infrastructure, advanced operations can be challenging  |
| **Spreadsheets**        | Widespread use, very easy to get started, easy for sharing | Steps aren't reproducible, advanced operations can be challenging |

A common workflow is to load a subset of data in from a database system into `pandas`, then do further cleaning and visualization. Another is to load and clean data in `pandas`, then store it in a database system for others to use.

### Relational algebra

**Relational algebra** captures common data operations between many data table systems. For example, the following expression describes a calculation in relational algebra:

$$\pi_{\text{int_rate}}(\sigma_{\text{state} = \text{"MI"}}(\text{loans}))$$

$$\pi$$ stands for "**p**roject," i.e. selecting columns; $$\sigma$$ stands for "**s**elect," i.e. selecting rows. We won't test you on relational algebra syntax, but if you'd like to learn more, take EECS 484: Database Management Systems.

In `pandas`, we'd implement this expression as follows:

```python
loans.loc[loans['state'] == 'MI', 'int_rate']
```

**Question**: How would we implement it in SQL? Or a spreadsheet?

To show you how the tabular manipulation skills you've learned in `pandas` generalize to other systems, we will answer a few questions in all three of the above platforms. First, we'll work through our analysis in `pandas`, and then in SQL, and finally, in a Google Sheets document.

### Dataset: Top 200 Streams

Our dataset contains the number of streams for the top 200 songs on Spotify, for the week leading up to September 19th. We downloaded it from [**here**](https://charts.spotify.com/charts/view/regional-global-weekly/latest) in Fall 2024, and you can find a copy of it (to repeat the analysis) [**here**](https://github.com/practicaldsc/fa24/blob/main/lectures/lec10/data/regional-global-weekly-2024-09-19.csv).

```python
charts = pd.read_csv('data/regional-global-weekly-2024-09-19.csv')
charts
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
      <th>rank</th>
      <th>uri</th>
      <th>artist_names</th>
      <th>track_name</th>
      <th>...</th>
      <th>peak_rank</th>
      <th>previous_rank</th>
      <th>weeks_on_chart</th>
      <th>streams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>spotify:track:2plbrEY59IikOBgBGLjaoe</td>
      <td>Lady Gaga, Bruno Mars</td>
      <td>Die With A Smile</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>76502673</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>spotify:track:6dOtVTDdiauQNBQEDOtlAB</td>
      <td>Billie Eilish</td>
      <td>BIRDS OF A FEATHER</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>18</td>
      <td>54756808</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>spotify:track:5G2f63n7IPVPPjfNIGih7Q</td>
      <td>Sabrina Carpenter</td>
      <td>Taste</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>48790619</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>197</th>
      <td>198</td>
      <td>spotify:track:3EaJDYHA0KnX88JvDhL9oa</td>
      <td>Steve Lacy</td>
      <td>Dark Red</td>
      <td>...</td>
      <td>66</td>
      <td>200</td>
      <td>118</td>
      <td>8901006</td>
    </tr>
    <tr>
      <th>198</th>
      <td>199</td>
      <td>spotify:track:0gEyKnHvgkrkBM6fbeHdwK</td>
      <td>The Cranberries</td>
      <td>Linger</td>
      <td>...</td>
      <td>199</td>
      <td>-1</td>
      <td>2</td>
      <td>8867800</td>
    </tr>
    <tr>
      <th>199</th>
      <td>200</td>
      <td>spotify:track:7iUtQNMRB8ZkKC4AmEuCJC</td>
      <td>Myke Towers</td>
      <td>LA FALDA</td>
      <td>...</td>
      <td>24</td>
      <td>185</td>
      <td>36</td>
      <td>8848312</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 9 columns</p>
</div>


Scroll through the columns above. A song's `'uri'` is its uniform resource identifier. Given a song's `'uri'`, we can play it! 

```python
def show_spotify(uri):
    code = uri[uri.rfind(':')+1:]
    src = f"https://open.spotify.com/embed/track/{code}"
    width = 400
    height = 75
    display(IFrame(src, width, height))

my_uri = charts.loc[charts['track_name'] == 'Yellow', 'uri'].iloc[0] 
my_uri
```

    'spotify:track:3AJwUDP919kvQ9QcozQPxg'




```python
show_spotify(my_uri)
```



<iframe
    width="400"
    height="75"
    src="https://open.spotify.com/embed/track/3AJwUDP919kvQ9QcozQPxg"
    frameborder="0"
    allowfullscreen

></iframe>


---

## Round 1: `pandas`

Below, we present six tasks and their solutions. A good way to practice your `pandas` skills is to download the CSV linked above and attempt the six tasks on your own, without looking at the solutions.

**Task 1**: Find the total number of streams of songs by Sabrina Carpenter.


<details markdown="1">

<summary>Click <b>here</b> to see the solution.</summary>

```python
charts.loc[charts['artist_names'] == 'Sabrina Carpenter', 'streams'].sum()
```

```
212960137
```

</details>

<br>
**Task 2**: Find the total number of streams per artist, sorted by number of streams in descending order. Only show the top 5 artists.

<details markdown="1">

<summary>Click <b>here</b> to see the solution.</summary>

```python
(
    charts
    .groupby('artist_names')
    ['streams']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
```

    artist_names
    Sabrina Carpenter        212960137
    Billie Eilish            107797821
    Chappell Roan             92990557
    Linkin Park               89935206
    Lady Gaga, Bruno Mars     76502673
    Name: streams, dtype: int64

</details>

<br>
**Task 3**: Find the artist with the lowest average number of streams, among artists with at least 5 songs in the Top 200.

<details markdown="1">

<summary>Click <b>here</b> to see the solution.</summary>

```python
(
    charts
    .groupby('artist_names')
    .filter(lambda df: df.shape[0] >= 5)
    .groupby('artist_names')
    ['streams']
    .mean()
    .sort_values()
    .head(1)
)
```

    artist_names
    Bruno Mars    1.24e+07
    Name: streams, dtype: float64

</details>


<br>
**Task 4**: Find the number of songs with a higher ranking this week than last week.

<details markdown="1">

<summary>Click <b>here</b> to see the solution.</summary>

```python
charts[charts['rank'] > charts['previous_rank']].shape[0]
```


    119


</details>

<br>
**Task 5**: `charts_old` contains the Top 200 songs in the previous week. You can download it from [**here**](https://github.com/practicaldsc/fa24/blob/main/lectures/lec10/data/regional-global-weekly-2024-09-12.csv).


```python
charts_old = pd.read_csv('data/regional-global-weekly-2024-09-12.csv')
charts_old.head()
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
      <th>rank</th>
      <th>uri</th>
      <th>artist_names</th>
      <th>track_name</th>
      <th>...</th>
      <th>peak_rank</th>
      <th>previous_rank</th>
      <th>weeks_on_chart</th>
      <th>streams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>spotify:track:2plbrEY59IikOBgBGLjaoe</td>
      <td>Lady Gaga, Bruno Mars</td>
      <td>Die With A Smile</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>74988392</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>spotify:track:6dOtVTDdiauQNBQEDOtlAB</td>
      <td>Billie Eilish</td>
      <td>BIRDS OF A FEATHER</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>17</td>
      <td>56949755</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>spotify:track:5G2f63n7IPVPPjfNIGih7Q</td>
      <td>Sabrina Carpenter</td>
      <td>Taste</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>49847514</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>spotify:track:7tI8dRuH2Yc6RuoTjxo4dU</td>
      <td>Jimin</td>
      <td>Who</td>
      <td>...</td>
      <td>1</td>
      <td>4</td>
      <td>8</td>
      <td>45431448</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>spotify:track:2qSkIjg1o9h3YT9RAgYN75</td>
      <td>Sabrina Carpenter</td>
      <td>Espresso</td>
      <td>...</td>
      <td>1</td>
      <td>5</td>
      <td>22</td>
      <td>44982843</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 9 columns</p>
</div>

Find the song with the largest increase in streams between last week and this week, among songs that were in the Top 200 in both weeks.

<details markdown="1">

<summary>Click <b>here</b> to see the solution.</summary>

```python
with_old = (
    charts[['uri', 'track_name', 'artist_names', 'streams']]
    .merge(charts_old[['uri', 'streams',]], on='uri', suffixes=('_new', '_old'))
)

(
    with_old
    .assign(change=with_old['streams_new'] - with_old['streams_old'])
    .sort_values('change', ascending=False)
    [['track_name', 'artist_names', 'change']]
    .head(1)
)
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
      <th>track_name</th>
      <th>artist_names</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Good Luck, Babe!</td>
      <td>Chappell Roan</td>
      <td>3217539</td>
    </tr>
  </tbody>
</table>
</div>

</details>

<br>
**Task 6**: Find the 4 songs with the most artists.

<details markdown="1">

<summary>Click <b>here</b> to see the solution.</summary>

```python
(
    charts
    .assign(num_artists=charts['artist_names'].str.count(', '))
    .sort_values('num_artists', ascending=False)
    .head(4)
)
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
      <th>rank</th>
      <th>uri</th>
      <th>artist_names</th>
      <th>track_name</th>
      <th>...</th>
      <th>previous_rank</th>
      <th>weeks_on_chart</th>
      <th>streams</th>
      <th>num_artists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>spotify:track:1BJJbSX6muJVF2AK7uH1x4</td>
      <td>Adam Port, Stryv, Keinemusik, Orso, Malachiii</td>
      <td>Move</td>
      <td>...</td>
      <td>31</td>
      <td>14</td>
      <td>15987047</td>
      <td>4</td>
    </tr>
    <tr>
      <th>186</th>
      <td>187</td>
      <td>spotify:track:22skzmqfdWrjJylampe0kt</td>
      <td>Macklemore &amp; Ryan Lewis, Macklemore, Ryan Lewi...</td>
      <td>Can't Hold Us (feat. Ray Dalton)</td>
      <td>...</td>
      <td>163</td>
      <td>132</td>
      <td>9050984</td>
      <td>3</td>
    </tr>
    <tr>
      <th>194</th>
      <td>195</td>
      <td>spotify:track:28drn6tQo95MRvO0jQEo5C</td>
      <td>Future, Metro Boomin, Travis Scott, Playboi Carti</td>
      <td>Type Shit</td>
      <td>...</td>
      <td>-1</td>
      <td>25</td>
      <td>8942475</td>
      <td>3</td>
    </tr>
    <tr>
      <th>177</th>
      <td>178</td>
      <td>spotify:track:4QNpBfC0zvjKqPJcyqBy9W</td>
      <td>Pitbull, AFROJACK, Ne-Yo, Nayer</td>
      <td>Give Me Everything (feat. Nayer)</td>
      <td>...</td>
      <td>165</td>
      <td>19</td>
      <td>9265696</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 10 columns</p>
</div>

</details>

---

## Round 2: SQL

### Overview and setup

SQL stands for "Structured Query Language". It is **the** standard language for database manipulation. Each database system – for instance, MySQL, SQLite, DuckDB, or PostgreSQL – has its own slightly different dialect of SQL with unique features.

Of note, SQL is a **declarative** language. That is, in SQL, you just describe _what_ you want calculated, not _how_ you want it calculated. It's the database engine's job to figure out _how_ to process your **query**.

```sql
        SELECT artist_names, SUM(streams) AS total_streams FROM charts
        GROUP BY artist_names
        ORDER BY total_streams DESC
        LIMIT 5;
```

<center><small>One of the SQL queries we'll write shortly.</small></center>

We bolded the word "query" above because all code we write in SQL is referred to as a query. All SQL queries follow the same general template:

<center><img src="../assets/sql.png" width=900>

<br>
(<a href="https://learnsql.com/blog/sql-query-basic-elements/">source</a>)

</center>

[W3Schools](https://www.w3schools.com/sql/sql_examples.asp) has examples of SQL syntax, as does the example above.

In this guide, we'll demonstrate the usage of two SQL database platforms: SQLite and DuckDB. SQLite comes pre-installed on most systems, while DuckDB is open-source, and integrates with `pandas` really well. We'll answer our first few tasks by working with `sqlite3` in the command-line. To follow along:
1. Download `spotify.db` from [**here**](https://github.com/practicaldsc/fa24/blob/main/lectures/lec10/data/spotify.db).
1. Open your Terminal and `cd` to the directory where you downloaded `spotify.db`.
1. Run `sqlite3 spotify.db`.

These steps will open a `sqlite3` interpreter, connected to the `spotify.db` **database**. A database file can contain multiple tables; this one contains two: `charts` and `charts_old`. Note that tables are also known as **relations** in database terminology.

Now, on with the tasks. Here, we'll show the solutions directly. That said, this [**walkthrough video**](https://youtu.be/Jv14ceontLM) also covers the answers, and develops them step-by-step. (It's taken from a lecture recording in Fall 2024.)

<center>

<iframe width="800" height="350" src="https://www.youtube.com/embed/Jv14ceontLM?si=jhQym8G4QvmwdcVs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</center>

**Task 1**: Find the total number of streams of songs by Sabrina Carpenter.

<center><img src="../assets/task-1.png" width=700></center>

**Task 2**: Find the total number of streams per artist, sorted by number of streams in descending order. Only show the top 5 artists.

<center><img src="../assets/task-2.png" width=700></center>


Note that the values above match the outputs in the `pandas` implementations of the tasks!

### Aside: DuckDB

Instead of having to run all of our SQL queries in the Terminal using a `.db` file, we can use DuckDB, which allows us to execute queries in a notebook **using a `pandas` DataFrame**! 

To use DuckDB, `pip install` it in your Terminal using `pip install duckdb`. Then, in your notebook, run `import duckdb`. That will allow you to use the `run_sql` function, defined below, to execute SQL queries using the DataFrames in your notebook as SQL tables.


```python
def run_sql(query_str, as_df=False):
    out = duckdb.query(query_str)
    if as_df:
        return out.to_df()
    else:
        return out
```

Let's revisit Task 2:

```python
run_sql('''
SELECT artist_names, SUM(streams) AS total_streams FROM charts
GROUP BY artist_names
ORDER BY total_streams DESC
LIMIT 5;
''')
```


    ┌───────────────────────┬───────────────┐
    │     artist_names      │ total_streams │
    │        varchar        │    int128     │
    ├───────────────────────┼───────────────┤
    │ Sabrina Carpenter     │     212960137 │
    │ Billie Eilish         │     107797821 │
    │ Chappell Roan         │      92990557 │
    │ Linkin Park           │      89935206 │
    │ Lady Gaga, Bruno Mars │      76502673 │
    └───────────────────────┴───────────────┘


We can even ask for the output back as a DataFrame by setting `as_df` to `True`! This means that you can combine both SQL operations and `pandas` operations.

```python
run_sql('''
SELECT artist_names, SUM(streams) AS total_streams FROM charts
GROUP BY artist_names
ORDER BY total_streams DESC
LIMIT 5;
''', as_df=True)
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
      <th>artist_names</th>
      <th>total_streams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sabrina Carpenter</td>
      <td>2.13e+08</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Billie Eilish</td>
      <td>1.08e+08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chappell Roan</td>
      <td>9.30e+07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Linkin Park</td>
      <td>8.99e+07</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Lady Gaga, Bruno Mars</td>
      <td>7.65e+07</td>
    </tr>
  </tbody>
</table>
</div>

Back to the tasks.

**Task 3**: Find the artist with the lowest average number of streams, among artists with at least 5 songs in the Top 200.

```python
run_sql('''
SELECT artist_names, AVG(streams) as avg_streams FROM charts
GROUP BY artist_names
HAVING COUNT(*) >= 5
ORDER BY avg_streams
LIMIT 1;
''')
```

    ┌──────────────┬─────────────┐
    │ artist_names │ avg_streams │
    │   varchar    │   double    │
    ├──────────────┼─────────────┤
    │ Bruno Mars   │  12411488.8 │
    └──────────────┴─────────────┘

**Task 4**: Find the number of songs with a higher ranking this week than last week.


```python
run_sql('''
SELECT COUNT(*) as num_songs FROM (
    SELECT * FROM charts
    WHERE rank > previous_rank
)
''')
```

    ┌───────────┐
    │ num_songs │
    │   int64   │
    ├───────────┤
    │       119 │
    └───────────┘


**Task 5**: `charts_old` contains the Top 200 songs in the previous week.

Find the song with the largest increase in streams between last week and this week, among songs that were in the Top 200 in both weeks.

```python
run_sql('''
SELECT track_name, artist_names, (new_streams - old_streams) AS change
FROM (
    SELECT charts.uri, 
           charts.track_name, 
           charts.artist_names, 
           charts.streams AS new_streams, 
           charts_old.uri, 
           charts_old.streams AS old_streams
    FROM charts
    INNER JOIN charts_old ON charts.uri = charts_old.uri
) AS merged
ORDER BY change DESC
LIMIT 1;
''', as_df=True)
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
      <th>track_name</th>
      <th>artist_names</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Good Luck, Babe!</td>
      <td>Chappell Roan</td>
      <td>3217539</td>
    </tr>
  </tbody>
</table>
</div>


**Task 6**: Find the 4 songs with the most artists.<br>

Note that the syntax used in our solution doesn't exist in SQLite, but **does** exist in DuckDB.


```python
run_sql('''
SELECT track_name, artist_names, array_length(str_split(artist_names, ', ')) AS num_artists
FROM charts
ORDER BY num_artists DESC
LIMIT 4;
''', as_df=True)
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
      <th>track_name</th>
      <th>artist_names</th>
      <th>num_artists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Move</td>
      <td>Adam Port, Stryv, Keinemusik, Orso, Malachiii</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Give Me Everything (feat. Nayer)</td>
      <td>Pitbull, AFROJACK, Ne-Yo, Nayer</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Can't Hold Us (feat. Ray Dalton)</td>
      <td>Macklemore &amp; Ryan Lewis, Macklemore, Ryan Lewi...</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Type Shit</td>
      <td>Future, Metro Boomin, Travis Scott, Playboi Carti</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>

In all of the examples above, the results matched our `pandas` implementations, as we'd expect.


---

## Round 3: Spreadsheets

### Overview and setup

While we're big fans of writing code in this class, in the business world, spreadsheets are (still) the most common tool for tabular data manipulation. Spreadsheets are great for showing information directly to someone else, and are easy to share.

Here, we'll replicate our prior analyses using Google Sheets. Excel may be more industry-standard, but Google Sheets are widely popular as well, and are easy for sharing.

[**This Google Sheet**](https://docs.google.com/spreadsheets/d/1OFWqms0UN-9Lr5HxwPdZsgpPlLir8fy67dN0PD0beug/edit?usp=sharing) has both the `charts` and `charts_old` datasets that we've referred to above. You can try your hand at the analyses by creating a copy of it; do so by opening it and going to File > Make a copy.

### Walkthrough video

Since Google Sheets operations are slightly more complicated to share via text, we've produced a [**walkthrough video**](https://www.loom.com/share/eb06b185428542c391f21e55480a0d2d?sid=f2ed6617-a5a3-4c88-96b1-f78b396d7ac4). It covers the same six tasks that we've already completed in `pandas` and SQL.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/eb06b185428542c391f21e55480a0d2d?sid=88b42f11-1b0e-44d7-882a-6ba3e6935e60" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

If following along, at each stage, make sure you see the same results as in the `pandas` and SQL sections!

**Task 1**: Find the total number of streams of songs by Sabrina Carpenter.

Relevant functions: `FILTER`, `SUMIF`.

**Task 2**: Find the total number of streams per artist, sorted by number of streams in descending order. Only show the top 5 artists.

Relevant functions: `UNIQUE`, `SUMIF`.

**Task 3**: Find the artist with the lowest average number of streams, among artists with at least 5 songs in the Top 200.

Relevant functions: `AVERAGEIF`.

**Task 4**: Find the number of songs with a higher ranking this week than last week.

Relevant functions: `IF`.


**Task 5**: `charts_old` contains the Top 200 songs in the previous week.

Find the song with the largest increase in streams between last week and this week, among songs that were in the Top 200 in both weeks.

Relevant functions: `FILTER`.

**Task 6**: Find the 4 songs with the most artists.

Relevant functions: `SPLIT`, `LEN`, `SUBSTITUTE`.

<br>

As you've seen, the DataFrame manipulation techniques we've learned about over the past month generalize to other systems that you might be exposed to. This is important to realize, since in 20 years, `pandas` may not exist, but grouping, pivoting, querying, etc. are all **concepts** that still will be useful.