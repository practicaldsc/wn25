---
layout: page
title: Visualization Tips and Examples
description: >-
  More on the theory and practice of data visualization.
parent: 🐼 Data Wrangling
grand_parent: 🧑‍🤝‍🧑 Guides
---


# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>


## Overview

In [Lecture 7](https://practicaldsc.org/resources/lectures/lec07/lec07-filled.html), we provided an overview of `plotly` syntax, and discussed how to decide which type of chart to create, be it a bar chart, histogram, line chart, box plot, scatter plot.

The purpose of this guide is twofold:
1. First, we'll discuss visualization "best practices", and how to avoid common mistakes.
1. Then, we'll show you several examples of other plots you can create in `plotly`, drawing from rich historical examples.


As a reminder, the [`plotly` examples library](https://plotly.com/python/) is excellent; you should use it as a reference and as inspiration when developing plots on your own (say, for the Final Project).

The plots in this website are not interactive, only due to a rendering limitation with the course website. If you run the code below on your own, you'll be able to interact with the resulting plots.

---

## Best practices

### Perception

As we discussed in Lecture 7, one reason to create visualizations is for **us** to better understand our data. But another reason is to **_accurately communicate_ a message to other people**. And, as it turns out, the world around us is filled with examples of visualizations that are difficult to accurately interpret, or **perceive**.

We'll start with a few examples from the internet.

<center><img src="../assets/bad-india.jpg" width="500">

</center>

<center>What's wrong with <a href="https://x.com/JeffDean/status/1291613522942504962">this visualization</a>?</center>

<center><img src="../assets/bad-bar.png" width="500">

</center>

<center>What's wrong with <a href="https://www.researchgate.net/publication/2564098_User_Adaptive_Information_Visualization#pf2">this visualization</a>?</center>

Something seems "wrong" about the two visualizations above, but describing specifically what is wrong can be challenging without the right vocabulary. To illustrate, let's pivot to a dataset of our own. Below, we load in a dataset with information about various countries over time, maintained by [Gapminder](https://www.gapminder.org/).


```python
world = px.data.gapminder() # The dataset is built into plotly.express.
world
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
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>lifeExp</th>
      <th>pop</th>
      <th>gdpPercap</th>
      <th>iso_alpha</th>
      <th>iso_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1952</td>
      <td>28.80</td>
      <td>8425333</td>
      <td>779.45</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1957</td>
      <td>30.33</td>
      <td>9240934</td>
      <td>820.85</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1962</td>
      <td>32.00</td>
      <td>10267083</td>
      <td>853.10</td>
      <td>AFG</td>
      <td>4</td>
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
    </tr>
    <tr>
      <th>1701</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1997</td>
      <td>46.81</td>
      <td>11404948</td>
      <td>792.45</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1702</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2002</td>
      <td>39.99</td>
      <td>11926563</td>
      <td>672.04</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1703</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2007</td>
      <td>43.49</td>
      <td>12311143</td>
      <td>469.71</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
  </tbody>
</table>
<p>1704 rows × 8 columns</p>
</div>



Let's suppose we're interested in understanding the distribution of Earth's population by continent, in the most recent year we have data for (which, in this dataset, happens to be 2007).


```python
pop_by_cont = (
    world[world['year'] == world['year'].max()]
    .groupby('continent')
    ['pop']
    .sum()
)
pop_by_cont
```




    continent
    Africa       929539692
    Americas     898871184
    Asia        3811953827
    Europe       586098529
    Oceania       24549947
    Name: pop, dtype: int64



In Lecture 7, we've seen that the "default" way to visualize such a distribution is to draw a bar chart:


```python
(
    pop_by_cont
    .sort_values()
    .plot(kind='barh', title='Distribution of Population by Continent')
)
```


    
<center><img src="../assets/output_11_0.png" width="85%"></center>
    


But, we _could_ also draw a pie chart:


```python
px.pie(
    pop_by_cont.reset_index(), 
    values='pop',
    names='continent',
    title='Distribution of Population by Continent'
).update_traces(textinfo='label')
```


    
<center><img src="../assets/output_13_0.png" width="85%"></center>
    


Note that Africa's population is larger than that of the Americas. But, that trend is only _visually_ obvious in the bar chart. It's easy to distinguish the lengths of bars that start at the same baseline; visualizing differences in angles or areas – as we're being asked to in the pie chart – is more difficult.

There is science to back up this phenomenon. In the mid-1980s, statisticians ran experiments comparing how easily human subjects were able to tell apart changes in length, angle, area, volume, color, and other **visual encodings**. Read [this article](https://peteraldhous.com/ucb/2016/dataviz/week2.html) for more details.

<center><img src="../assets/perception.png" width=500></center>

As a data scientist, **your job is to make comparisons easy!** Avoid pie charts and other visual representations that make it difficult to understand the data. Going back to the women's heights example, the area of the India figure is tiny compared to the area of the Latvia figure, despite only representing a value 5 inches smaller.

### Aside: What is a distribution?

The term "distribution" is often misused. For example, the following bar chart does **not** show a distribution. Why not?

<center><img src="../assets/not-dist.png" width=500></center>

The answer is because individuals can be in multiple categories – as told to us in the fine print – and the frequencies don't add to 100%.

By definition, the distribution of a column tells us the unique values in that column, and how often they occur. If using counts, the counts should add up to the number of data points; if using percentages, they should add up to 100%.


```python
# Actually a distribution!
(
    pop_by_cont
    .sort_values()
    .plot(kind='barh', title='Distribution of Population by Continent')
)
```


    
<center><img src="../assets/output_21_0.png" width="85%"></center>
    


### Color scales

Let's switch gears and investigate the role of color in our graphs. We'll start by loading in a dataset describing each Walmart location in the US as of 2006. Download it from [**here**](https://github.com/practicaldsc/fa24/blob/main/lectures/lec08/data/walmart.csv).


```python
wm = pd.read_csv('data/walmart.csv')
wm
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
      <th>storenum</th>
      <th>OPENDATE</th>
      <th>date_super</th>
      <th>conversion</th>
      <th>...</th>
      <th>LON</th>
      <th>MONTH</th>
      <th>DAY</th>
      <th>YEAR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7/1/62</td>
      <td>3/1/97</td>
      <td>1.0</td>
      <td>...</td>
      <td>-94.07</td>
      <td>7</td>
      <td>1</td>
      <td>1962</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>8/1/64</td>
      <td>3/1/96</td>
      <td>1.0</td>
      <td>...</td>
      <td>-93.09</td>
      <td>8</td>
      <td>1</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>8/1/65</td>
      <td>3/1/02</td>
      <td>1.0</td>
      <td>...</td>
      <td>-94.50</td>
      <td>8</td>
      <td>1</td>
      <td>1965</td>
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
      <th>2989</th>
      <td>5485</td>
      <td>1/27/06</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>-87.70</td>
      <td>1</td>
      <td>27</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>2990</th>
      <td>3425</td>
      <td>1/27/06</td>
      <td>1/27/06</td>
      <td>0.0</td>
      <td>...</td>
      <td>-95.22</td>
      <td>1</td>
      <td>27</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>2991</th>
      <td>5193</td>
      <td>1/31/06</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>-117.17</td>
      <td>1</td>
      <td>31</td>
      <td>2006</td>
    </tr>
  </tbody>
</table>
<p>2992 rows × 16 columns</p>
</div>



To visualize the number of Walmarts per state, we could use a bar chart, as in the continents example.


```python
wm_per_state = wm['STRSTATE'].value_counts()
wm_per_state
```




    STRSTATE
    TX    315
    FL    175
    CA    159
         ... 
    WY      9
    ND      8
    DE      8
    Name: count, Length: 41, dtype: int64




```python
wm_per_state.head(10).sort_values().plot(kind='barh', title='Number of Walmarts Per State')
```


    
<center><img src="../assets/output_27_0.png" width="85%"></center>
    


But, perhaps a more interesting visualization is a **choropleth** – the kind you created in Homework 3, when visualizing the party with the most votes per state in 2024.


```python
choro = px.choropleth(wm_per_state.reset_index(),
             locations='STRSTATE',
             color='count',
             locationmode='USA-states',
             scope='usa',
             title='Number of Walmarts Per State')
choro
```


    
<center><img src="../assets/output_29_0.png" width="85%"></center>
    


Now, you may notice the choropleth above is colored differently than the one you had to create in Homework 3:

<center><img src="../assets/repl.png" width=800></center>

Why? In the bottom, political choropleth, the feature being compared across states is **categorical** (political party). In the top, Walmart choropleth, the feature being compared across states is **numerical** (number of Walmarts).

So:
- When comparing **categories**, use very different colors for each category, ideally choosing from a known [color-blind friendly color palette](https://davidmathlogic.com/colorblind/#%23D81B60-%231E88E5-%23FFC107-%23004D40).
- When comparing **numbers**, choose an appropriate _continuous_ color scheme. There are two types: sequential, where larger values are more intense and smaller values are less intensive; or diverging, where both large and small values are equally intense, but in different colors.

Here's another example of a **sequential** continuous color scale in action:


```python
px.choropleth(wm_per_state.reset_index(),
             locations='STRSTATE',
             color='count',
             locationmode='USA-states',
             scope='usa',
             title='Number of Walmarts Per State',
             color_continuous_scale='greens')
```


    
<center><img src="../assets/output_34_0.png" width="85%"></center>
    


Here's a **diverging** color scale, where dark blue means "large" and dark red means "small." Here, it feels unnatural that states with very few Walmarts and very many Walmarts are similarly "intense."


```python
px.choropleth(wm_per_state.reset_index(),
             locations='STRSTATE',
             color='count',
             locationmode='USA-states',
             scope='usa',
             title='Number of Walmarts Per State',
             color_continuous_scale='rdbu')
```


    
<center><img src="../assets/output_36_0.png" width="85%"></center>
    


But, diverging color schemes like the one above make sense in other cases, e.g. in [political choropleths that show voting margins](https://www.270towin.com/maps/consensus-2024-presidential-election-forecast).

### Key takeaways

The Gapminder and Walmart examples should have made two points clear. In your visualizations:

- Make comparisons easy.
- Choose an appropriate color scheme.

---

## More examples

Next, we'll look at several example visualizations, to serve as further inspiration. Some of these use chart types we saw in Lecture 7; others are new.

### Historical examples

William Playfair is known as the "father of data visualization", and is the creator of line charts, bar charts, and pie charts, among other things. We'll start by recreating some of his historical charts using `plotly`!

First, we'll recreate the **very first known example of a bar chart**, which depicts the
imports and exports of Scotland to various countries in 1781.

<center><img src='../assets/scotland.png' width=500></center>


```python
scotland = pd.read_csv('data/playfair-scotland.csv')
scotland
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
      <th>country</th>
      <th>imports</th>
      <th>exports</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ireland</td>
      <td>195685</td>
      <td>305167</td>
    </tr>
    <tr>
      <th>1</th>
      <td>America</td>
      <td>49826</td>
      <td>183620</td>
    </tr>
    <tr>
      <th>2</th>
      <td>West Indies</td>
      <td>169375</td>
      <td>141220</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Greenland</td>
      <td>8291</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Isle of Man &amp; Jersey</td>
      <td>802</td>
      <td>1818</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Denmark and Norway</td>
      <td>28118</td>
      <td>35011</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 3 columns</p>
</div>


The reproduction code is quite long, so we've hidden it behind a button.

<details markdown="1">

<summary>Click <b>here</b> to see the code for this example.</summary>

```python
fig = px.bar(scotland.sort_values('imports', ascending=False), 
             x=['exports', 'imports'], 
             y='country', 
             barmode='group', 
             orientation='h',
             color_discrete_map={
                 'exports': '#151EA6',
                 'imports': '#FCB305',
              },      
             title='Exports and Imports of <b>Scotland</b> to and from different parts for one Year'
            )

fig.update_layout(
    font_family="Arial",
    title_font_family="Arial",
    paper_bgcolor='#FFFFFF',
    plot_bgcolor='#FFFFFF',
    legend = {
        'title': '',
        'orientation': 'h'
    }
)

fig.add_annotation( # add a text callout with arrow
    text="no exports to Greenland!", x=10000, y="Greenland", ax=125,
    arrowhead=2, showarrow=True
)

fig.update_xaxes(title_text='',
                 side='top',
                 showline=True, 
                 linewidth=2, 
                 linecolor='black',
                 mirror=True,
                 showgrid=True, 
                 gridwidth=1, 
                 gridcolor='#EEEEEE',
                 tick0=0, 
                 dtick=25000,
                 tickangle=0)

fig.update_yaxes(title_text='',
                 side='right',
                 showline=True, 
                 linewidth=2, 
                 linecolor='black',
                 mirror=True,
                 showgrid=True, 
                 gridwidth=1, 
                 gridcolor='#EEEEEE',
                 tickson='boundaries')
```

</details>

<br>
    
<center><img src="../assets/output_42_0.png" width="85%"></center>
    


As an aside – what if we want to export this chart to HTML, to put on a website? (Say, for the Final Project?)

The `.to_html()` method will come in handy. Assuming `fig` is a `plotly` Figure, then we could use:


```python
with open('scotland.html', 'w') as f:
    f.write(fig.to_html())
    f.close()
```

This next plot shows the relationship between weekly labor wages and
the cost of a “quarter” of wheat, along with a timeline of English monarchs, from 1565 to 1821.

<img src='../assets/wheat-wages.png' width=800>


```python
wheat = pd.read_csv('data/Wheat.csv').drop(columns=['Unnamed: 0']).iloc[:-1]
wheat.head()
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
      <th>Year</th>
      <th>Wheat</th>
      <th>Wages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1565</td>
      <td>41.0</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1570</td>
      <td>45.0</td>
      <td>5.05</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1575</td>
      <td>42.0</td>
      <td>5.08</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1580</td>
      <td>49.0</td>
      <td>5.12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1585</td>
      <td>41.5</td>
      <td>5.15</td>
    </tr>
  </tbody>
</table>
</div>



This task is a bit different, since it involves two different types of visualizations – a line chart and a bar chart.


```python
px.line(wheat, x='Year', y='Wages')
```


    
<center><img src="../assets/output_48_0.png" width="85%"></center>
    



```python
px.bar(wheat, x='Year', y='Wages')
```


    
<center><img src="../assets/output_49_0.png" width="85%"></center>
    


Instead of using `plotly.express`, which is a "lite" version of `plotly`, we will use `plotly`'s `graph_objects` module.


```python
import plotly.graph_objects as go
```

<details markdown="1">

<summary>Click <b>here</b> to see the code for this example.</summary>

```python
wheat_fig = go.Figure()

# Add bar chart
wheat_fig.add_trace(
    go.Bar(
        x=wheat['Year'],
        y=wheat['Wheat'],
        name='Wheat',
        marker={'color': '#AAAAAA'},
        width=5
    )
)

# Add line chart
wheat_fig.add_trace(
    go.Scatter(
        x=wheat['Year'],
        y=wheat['Wages'],
        name='Wages',
        marker={'color': 'red'},
        fill='tozeroy',
        fillcolor='rgba(135,206,235,0.65)'
    )
)

# Adjust overall attributes
wheat_fig.update_layout(
    font_family="Arial",
    title_font_family="Arial",
    paper_bgcolor='#FFFFFF',
    plot_bgcolor='#FFFFFF',
    showlegend=False
)

# Adjust x-axis
wheat_fig.update_xaxes(title_text='<i>5 Years each division</i>', 
                       tickmode='array',
                       tickvals=[1565, 1600, 1650, 1700, 1750, 1800, 1820], 
                       tickangle=0,
                       showgrid=False,
                       showline=True, 
                       linewidth=2, 
                       linecolor='black',
                       mirror=True)

# Adjust y-axis
wheat_fig.update_yaxes(title_text='<i>Price of the Quarter of Wheat in Shillings</i>',
                       side='right',
                       tick0=0, 
                       dtick=5, 
                       gridcolor='#EEEEEE',
                       gridwidth=1,
                       showline=True, 
                       linewidth=2, 
                       linecolor='black',
                       mirror=True)

# Add annotations
wheat_fig.add_annotation( # add a text callout with arrow
    text="<i>Weekly Wages of a Good Mechanic</i>", 
    x=1640, 
    y=9, 
    showarrow=False, 
    font = {
        'size': 10,
        'color': 'white'
    }
    
)

# Add annotations
title_text = 'CHART,<br><i>Showing at One View</i><br><i>The Price of The Quarter of Wheat</i><br>& Wages of Labour by the Week,<br>-- from --<br><i>The Year 1565 to 1821</i><br>-- by --<br><i>William Playfair</i>'

wheat_fig.add_annotation(
    text=title_text, 
    x=1640, 
    y=70, 
    font = {
        'size': 10,
        'color': 'black'
    },
    bordercolor="black",
    borderwidth=2,
    borderpad=4,
    bgcolor="#FFFFFF",
    opacity=1
    
)

wheat_fig.add_annotation(
    text="<i>Weekly Wages of a Good Mechanic</i>", 
    x=1640, 
    y=9, 
    showarrow=False, 
    font = {
        'size': 10,
        'color': 'black'
    }
    
)
```

</details>

<br>

    
<center><img src="../assets/output_52_0.png" width="85%"></center>
    


Finally, we'll look at Playfair's first pie chart, describing the land distribution of the Turkish Empire.

<center><img src="../assets/pie.png" width=400></center>


```python
dist = pd.DataFrame().assign(
    continent=['African', 'European', 'Asiatic'],
    proportion=[0.2, 0.25, 0.55]
)

dist
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
      <th>continent</th>
      <th>proportion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>African</td>
      <td>0.20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>European</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Asiatic</td>
      <td>0.55</td>
    </tr>
  </tbody>
</table>
</div>


The code here is effectively the same as the code we used to create our earlier pie chart.


```python
px.pie(dist,
       values='proportion',
       names='continent',
       width=400,
       height=300,
       title='Land Distribution of the Turkish Empire')
```
    
<center><img src="../assets/output_55_0.png" width="85%"></center>
    


### Other plot types

Let's wrap up by looking at other plot types.

**Gantt charts (i.e. timelines)**


```python
phases = [
 ['Newborn', '1998-11-26', '1999-11-26', 'Canada'],
 ['Toddler, Preschooler', '1999-11-26', '2005-09-03', 'US'],
 ['Elementary School Student', '2005-09-03', '2009-06-30', 'Canada'],
 ['Middle School Student', '2009-09-15', '2012-06-15', 'Canada'],
 ['High School Student', '2012-09-05', '2016-05-30', 'Canada'],
 ['Undergrad @ UC Berkeley', '2016-08-22','2020-05-15', 'US'],
 ['Masters @ UC Berkeley', '2020-08-25', '2021-05-14', 'Canada'],
 ['Lecturer @ UCSD', '2021-09-01', '2024-06-30', 'US'],
 ['Lecturer @ UMich', '2024-08-26', '2025-04-28', 'US']]

phases_df = pd.DataFrame(phases, columns=['Phase', 'Start', 'End', 'Location'])
phases_df
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
      <th>Phase</th>
      <th>Start</th>
      <th>End</th>
      <th>Location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Newborn</td>
      <td>1998-11-26</td>
      <td>1999-11-26</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Toddler, Preschooler</td>
      <td>1999-11-26</td>
      <td>2005-09-03</td>
      <td>US</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Elementary School Student</td>
      <td>2005-09-03</td>
      <td>2009-06-30</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Masters @ UC Berkeley</td>
      <td>2020-08-25</td>
      <td>2021-05-14</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Lecturer @ UCSD</td>
      <td>2021-09-01</td>
      <td>2024-06-30</td>
      <td>US</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Lecturer @ UMich</td>
      <td>2024-08-26</td>
      <td>2025-04-28</td>
      <td>US</td>
    </tr>
  </tbody>
</table>
<p>9 rows × 4 columns</p>
</div>




```python
tim = px.timeline(phases_df,
                  x_start = 'Start',
                  x_end = 'End',
                  y = 'Phase',
                  text = 'Location',
                  title = 'My Life Trajectory',
                  width=700,
                  height=400)

tim.update_yaxes(autorange='reversed')
```


    
<center><img src="../assets/output_59_0.png" width="85%"></center>
    


**Animated scatter plots**


```python
world = px.data.gapminder()
world
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
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>lifeExp</th>
      <th>pop</th>
      <th>gdpPercap</th>
      <th>iso_alpha</th>
      <th>iso_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1952</td>
      <td>28.80</td>
      <td>8425333</td>
      <td>779.45</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1957</td>
      <td>30.33</td>
      <td>9240934</td>
      <td>820.85</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1962</td>
      <td>32.00</td>
      <td>10267083</td>
      <td>853.10</td>
      <td>AFG</td>
      <td>4</td>
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
    </tr>
    <tr>
      <th>1701</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1997</td>
      <td>46.81</td>
      <td>11404948</td>
      <td>792.45</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1702</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2002</td>
      <td>39.99</td>
      <td>11926563</td>
      <td>672.04</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1703</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2007</td>
      <td>43.49</td>
      <td>12311143</td>
      <td>469.71</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
  </tbody>
</table>
<p>1704 rows × 8 columns</p>
</div>



```python
px.scatter(world,
           x = 'gdpPercap',
           y = 'lifeExp', 
           hover_name = 'country',
           color = 'continent',
           size = 'pop',
           size_max = 60,
           log_x = True,
           range_y = [30, 90],
           animation_frame = 'year',
           title = 'Life Expectancy, GDP Per Capita, and Population over Time'
          )
```


    
<center><img src="../assets/output_62_0.png" width="85%"></center>

Again, our website doesn't have interactive versions of these plots, but if you run this code yourself you'll be able to click the "▶️ Play" button to see the points move over time, in the style of [**this classic video**](https://youtu.be/jbkSRLYSojo?si=LGPAWlvzN7kBdTMB).
    


**Animated histograms**


```python
px.histogram(world,
            x = 'lifeExp',
            animation_frame = 'year',
            range_x = [20, 90],
            range_y = [0, 50],
            title = 'Distribution of Life Expectancy over Time')
```


    
<center><img src="../assets/output_64_0.png" width="85%"></center>
    


**3D scatter plots**


```python
import seaborn as sns
penguins = sns.load_dataset('penguins')
penguins
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
      <th>species</th>
      <th>island</th>
      <th>bill_length_mm</th>
      <th>bill_depth_mm</th>
      <th>flipper_length_mm</th>
      <th>body_mass_g</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adelie</td>
      <td>Torgersen</td>
      <td>39.1</td>
      <td>18.7</td>
      <td>181.0</td>
      <td>3750.0</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Adelie</td>
      <td>Torgersen</td>
      <td>39.5</td>
      <td>17.4</td>
      <td>186.0</td>
      <td>3800.0</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Adelie</td>
      <td>Torgersen</td>
      <td>40.3</td>
      <td>18.0</td>
      <td>195.0</td>
      <td>3250.0</td>
      <td>Female</td>
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
    </tr>
    <tr>
      <th>341</th>
      <td>Gentoo</td>
      <td>Biscoe</td>
      <td>50.4</td>
      <td>15.7</td>
      <td>222.0</td>
      <td>5750.0</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Gentoo</td>
      <td>Biscoe</td>
      <td>45.2</td>
      <td>14.8</td>
      <td>212.0</td>
      <td>5200.0</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Gentoo</td>
      <td>Biscoe</td>
      <td>49.9</td>
      <td>16.1</td>
      <td>213.0</td>
      <td>5400.0</td>
      <td>Male</td>
    </tr>
  </tbody>
</table>
<p>344 rows × 7 columns</p>
</div>




```python
px.scatter_3d(penguins,
             x = 'bill_length_mm',
             y = 'bill_depth_mm',
             z = 'flipper_length_mm',
             color = 'species',
             hover_name = 'island',
             title = 'Flipper Length vs. Bill Depth vs. Bill Length')
```


    
<center><img src="../assets/output_67_0.png" width="85%"></center>

Again, the last few plots would be interactive if you produced them in your notebook.

---

## More resources

Entire courses are dedicated to data visualization. Unfortunately, we don't have an entire semester to dedicate to it ourselves! 

We've just provided you with a few high-level considerations to be aware of when making plots. For more resources, look at:

    - [This lecture](https://ds100.org/su20/lecture/lec10) I taught at another university that discusses some of these ideas in more depth.
    - [This visualization course at UC San Diego](https://dsc-courses.github.io/dsc106-wi24).
    - [This visualization course at the University of Washington](https://courses.cs.washington.edu/courses/cse442/23au/).
    - [This visualization course at UC Berkeley](https://peteraldhous.com/ucb/2016/dataviz/).
