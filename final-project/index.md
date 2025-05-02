---
layout: page
title: 📊 Final Project
description: Description of the Final Project, the final assignment of the semester.
nav_order: 6
has_children: true
---

<script type="text/javascript" async="" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>

# {{ page.title }}
{: .no_toc }

{: .green }
> This project has two (optionally, three) deadlines:
> - (Optional) custom dataset proposal due **Wednesday, March 26th**
> - [Checkpoint](#checkpoint-submission) due **Friday, March 28th at 11:59PM** (slip days allowed!)
> - Final Submission due **Tuesday, April 22nd at 11:59PM** (<b><span style="color:red">no slip days allowed!</span>)

_last updated March 18 at 4:45PM_

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Welcome to the Final Project, the final assignment of the semester! 👋

This project aims to be a culmination of everything you've learned this semester. In the project, you will conduct an open-ended investigation into one of the three datasets (🍽 Recipes and Ratings, ⌨️ League of Legends, or 🔋 Power Outages), or – upon permission of the instructor – choose your own. Specifically, you'll draw several visualizations to help understand the distributions of key variables, build and improve a predictive model, and share your findings with everyone on the internet.

The Final Project is worth 100 points total; the breakdown is described in the [Rubric](#rubric) section at the bottom of this page. The Final Project is different from homeworks in a few crucial ways:

- You **can work with one partner** (but don't have to). If you choose to work with a partner, read the [Partner Guidelines](#partner-guidelines) section at the bottom.
- There is a **checkpoint**, due March 28, 2025, worth 15 points out of the 100 points the project is scored out of. It exists to make sure you've picked a dataset and started some preliminary work. See the [Checkpoint Submission](#checkpoint-submission) section for more details and for the Gradescope submission link.
- You can use slip days on the checkpoint; however, you **cannot use slip days** on the final submission, since it's due so close to the end of the semester that we need all the time we can get to grade them. All components of the project are manually graded.
- As your final deliverables, you'll submit two things to us:
  - a public-facing website. We'll eventually create a public "showcase" site that has links to everyone's submissions – **that is, your website will be available to the entire internet!**
  - a PDF of your Jupyter Notebook.

Before we get into the details of what's expected of you, note that this project in particular is meant to encourage you to build something you're proud of. This is a chance to put something concrete on your resume to show potential employers. Grading will likely be lenient, but your work will be publicly available forever!

As alluded to above, the project is broken into two parts:

- Part 1: An **analysis**, submitted as a Jupyter Notebook. This will contain the details of your work. Focus on completing your analysis before moving to Part 2, as the analysis is the bulk of the project.
- Part 2: A **report**, submitted as a website. This will contain a narrative "story" with visuals. Focus on this after finishing _most_ of your analysis.

The project is worth a total of 100 points. You can see the distribution of points in the [Rubric](#rubric) section at the very bottom.

---

## Choosing a Dataset

In this project, you will perform an open-ended investigation into a **single dataset**. Here are the four options available to you; click the relevant pages for more details. (These are also accessible from the sidebar of the course website, to your left.)

1. [🍽 Recipes and Ratings](datasets/recipes-and-ratings)
2. [⌨️ League of Legends](datasets/league-of-legends)
3. [🔋 Power Outages](datasets/power-outages)
4. [🎨 Custom Dataset](datasets/custom-dataset)

The first three dataset description pages linked above each have three sections:

- **Getting the Data**: Describes how to access the data and, in some cases, what various features mean. (In general, you're going to have to understand what your data means on your own!) You're welcome to download additional data to help with your analyses, in addition to using the data that's provided for you.
- **Example Questions and Prediction Problems**: Use these as inspiration, but feel free to come up with your own questions and prediction problems!
- **Special Considerations**: Things to be aware of when working with the given dataset, e.g. some additional requirements.

If you're interested in bringing your own dataset, the fourth page linked above will guide you through the process of proposing a custom dataset. Note that the deadline to propose a custom dataset is **Wednesday, March 26th**.

When selecting which dataset you'll use for your project, try choosing the one whose topic appeals to you the most as that will make finishing the project a lot more enjoyable.

{: .blue }
To help contextualize the kinds of analysis you can do in this project, it might help to browse through Fall 2024's [**Showcase Page**](https://practicaldsc.org/showcase/). Treat last semester's examples as a foundation for inspiration, but **don't** just repeat or copy their work - be original!

Before choosing a dataset, read the rest of this page to see what's required of you!

---

## Part 1: Analysis

Before beginning your analysis, you'll need to set up a few things.

1. Pull the latest version of the course GitHub repo, [github.com/practicaldsc/wn25](https://github.com/practicaldsc/wn25). Within the `final-project` folder, there is a `template.ipynb` notebook that you will use as a template for the project. If you delete the file or want another copy of the template, you can re-download it from [here](https://github.com/practicaldsc/wn25/blob/main/final-project/template.ipynb). This is where your analysis will live; you will submit this entire notebook to us.
1. Download the [dataset](#choosing-a-dataset) you chose and load it into your template notebook.

Once you have your dataset loaded in your notebook, it's time for you to find meaning in the real-world data you've collected! Follow the steps below.

{: .green }
For each step, we specify what must be done in your notebook and what must go on your website, which we expand on in [**Part 2**](#part-2-report). We recommend you write everything in your notebook first, and then move things over to your website once you've completed your analysis.

<br>

In Steps 1-2, you'll develop a deeper understanding of your dataset while trying to answer a single question.

### Step 1: Introduction

| Step                                         | Analysis in Notebook                                                                                                                                                                                                                                                                                                                  | Report on Website                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Introduction and Question Identification** | Understand the data you have access to. Brainstorm a few questions that interest you about the dataset. Pick **one** question you plan to investigate further. | Provide an introduction to your dataset, and clearly state the one question your project is centered around. Why should readers of your website care about the dataset and your question specifically? Report the number of rows in the dataset, the names of the columns that are relevant to your question, and descriptions of those relevant columns. |

### Step 2: Data Cleaning and Exploratory Data Analysis

| Step                       | Analysis in Notebook                                                                                                                                                                                                                                                 | Report on Website                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data Cleaning**          | Clean the data appropriately. For instance, you may need to replace data that should be missing with `NaN` or create new columns out of given ones (e.g. compute distances, apply numerical-to-numerical transformations, or get time information from time stamps). | Describe, in detail, the data cleaning steps you took and how they affected your analyses. The steps should be explained in reference to the data generating process. Show the `head` of your cleaned DataFrame (see [Part 2: Report](#part-2-report) for instructions).                                                                                                                                                                                                                                                                                                                       |
| **Univariate Analysis**    | Look at the distributions of relevant columns separately by using DataFrame operations and drawing at least two relevant plots.                                                                                                                                      | Embed **at least one** `plotly` plot you created in your notebook that displays the distribution of a single column (see [Part 2: Report](#part-2-report) for instructions). Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present, and how they answer your initial question. (Your notebook will likely have more visualizations than your website, and that's fine. Feel free to embed more than one univariate visualization in your website if you'd like, but make sure that each embedded plot is accompanied by a description.) |
| **Bivariate Analysis**     | Look at the statistics of pairs of columns to identify possible associations. For instance, you may create scatter plots and plot conditional distributions, or box plots. You must plot at least two such plots in your notebook. Be creative!                      | Embed **at least one** `plotly` plot that displays the relationship between two columns. Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present and how they answer your initial question. (Your notebook will likely have more visualizations than your website, and that's fine. Feel free to embed more than one bivariate visualization in your website if you'd like, but make sure that each embedded plot is accompanied by a description.)                                                                                       |
| **Interesting Aggregates** | Choose columns to group and pivot by and examine aggregate statistics.                                                                                                                                                                                               | Embed at least one grouped table or pivot table in your website and explain its significance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Imputation**             | If needed for further analyses, impute any missing values.                                                                                                                                                                                                           | If you imputed any missing values, visualize the distributions of the imputed columns before and after imputation. Describe which imputation technique you chose to use and why. If you didn't fill in any missing values, discuss why not.                                                                                                                                                                                                                                                                                                                                                    |

<br>

In Steps 3-5, you will build a predictive model, based on the knowledge of your dataset you developed in Steps 1-2.

A useful heuristic when designing your model is to decide whether your response variable (i.e. the variable you are predicting) should be treated as continuous or as categorical. Ask yourself:

- **Can you measure the difference between the maximum and minimum values quantitatively?** If you can, then a regression model is appropriate because it captures incremental differences and predicts precise numerical outcomes.

- **Or, is the distinction between high and low values more qualitative—where the maximum is simply "better" or "more" than the minimum?** In this case, a classification model might be more suitable, as it groups outcomes into distinct categories.

This approach helps ensure that your model reflects the true nature of your data. For a deeper discussion on this topic, see this [Stack Exchange discussion](https://stats.stackexchange.com/questions/68834/what-is-the-benefit-of-breaking-up-a-continuous-predictor-variable). **Framing your prediction problem appropriately is one of the most important parts of the project, so ask questions in office hours if you're unsure of your approach.**

### Step 3: Framing a Prediction Problem

| Step                       | Analysis in Notebook                                                                                                                                                                                                                                                                                                                                                                                       | Report on Website                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem Identification** | Identify a prediction problem. Feel free to use one of the example prediction problems stated in the "Example Questions and Prediction Problems" section of your dataset's description page or pose one of your own. The prediction problem you come up with doesn't have to be related to the question you were answering in Steps 1-2, but ideally, your entire project has some sort of coherent theme. | Clearly state your prediction problem and type (classification or regression). If you are building a classifier, make sure to state whether you are performing binary classification or multiclass classification. Report the response variable (i.e. the variable you are predicting) and why you chose it, the metric you are using to evaluate your model and why you chose it over other suitable metrics (e.g. accuracy vs. F1-score).<br><br>**_Note_**: Make sure to justify what information you would know at the "time of prediction" and to only train your model using those features. For instance, if we wanted to predict your Final Exam grade, we couldn’t use your Final Project grade, because we (probably) won't have the Final Project graded before the Final Exam! Feel free to ask questions if you're not sure. |

### Step 4: Baseline Model

| Step               | Analysis in Notebook                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Report on Website                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Baseline Model** | Train a "baseline model" for your prediction task that uses at least two features. (For this requirement, two features means selecting at least two unique columns from your original dataset.) You can leave numerical features as-is, but you'll need to take care of categorical columns using an appropriate encoding. Implement all steps (feature transforms and model training) in a single `sklearn` Pipeline. <br><br>**_Note_**: **Both now and in Step 5: Final Model, make sure to evaluate your model's ability to generalize to unseen data!** <br><br>There is no "required" performance metric that your baseline model needs to achieve. | Describe your model and state the features in your model, including how many are quantitative, ordinal, and nominal, and how you performed any necessary encodings. Report the performance of your model and whether or not you believe your current model is "good" and why.<br><br>**_Tip_**: Make sure to hit all of the points above: many Final Projects in the past have lost points for not doing so. |

### Step 5: Final Model

| Step            | Analysis in Notebook                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Report on Website                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Final Model** | Create a "final" model that improves upon the "baseline" model you created in Step 4. Do so by engineering at least two new features from the data, on top of any categorical encodings you performed in Baseline Model Step. (For instance, you may use a `StandardScaler` on a quantitative column and a `QuantileTransformer` transformer on a different column to get two new features.) Again, implement all steps in a single `sklearn` Pipeline. While deciding what features to use, you **must** perform a search for the best hyperparameters (e.g. tree depth) to use amongst a list(s) of options, either by using `GridSearchCV` or through some manual iterative method. In your notebook, state which hyperparameters you plan to tune and why before actually tuning them.<br><br>**_Optional_**: You are encouraged to try many different modeling algorithms for your final model (i.e. `LinearRegression`, `RandomForestClassifier`, `Lasso`, `SVC`, etc.) If you do this, make sure to clearly indicate in your notebook which model is your actual final model as that will be used to grade the above requirements.<br><br>**_Note 1_**: When training your model, make sure you use the same training and testing sets from your baseline model. This way, the evaluation metric you get on your final model can be compared to your baseline's on the basis of the model itself and not the dataset it was trained on. Based on which method you use for hyperparameter tuning, this may mean that you will need to use some of your training data as your validation data. If this is the case, make sure to train your final model on the whole training set to evaluation.<br><br>**_Note 2_**: You will not be graded on "how much" your model improved from Step 4: Baseline Model to Step 5: Final Model. What you will be graded on is on whether or not your model improved, as well as your thoughtfulness and effort in creating features, along with the other points above.<br><br>**_Note 3_**: Don't try to improve your model's performance just by blindly transforming existing features into new ones. Think critically about what each transformation you're doing actually does. For example, there's no use in using a `StandardScaler` transformer if your goal is to reduce the MSE of a linear model: as we learned in Lecture 18, standardizing features in a regression model does not change the model's predictions, only its coefficients! | State the features you added and **why** they are good for the data and prediction task. Note that you can't simply state "these features improved my accuracy", since you'd need to choose these features and fit a model before noticing that – instead, talk about _why_ you believe these features improved your model's performance from the perspective of the data generating process. <br><br>Describe the modeling algorithm you chose, the hyperparameters that ended up performing the best, and the method you used to select hyperparameters and your overall model. Describe how your Final Model's performance is an improvement over your Baseline Model's performance.<br><br>**_Optional_**: Include a visualization that describes your model's performance, e.g. a confusion matrix, if applicable. |

### Style

While your website will be neatly organized and tailored for public consumption, it is important to keep your analysis notebook organized as well. Follow these guidelines:

- Your work for each of the five project steps described above (Introduction, Data Cleaning and Exploratory Data Analysis, ..., Final Model) should be completed in code cells underneath the Markdown header of that section's name.
- You should **only include work that is relevant** to posing, explaining, and answering the question(s) you state in your website. You should include data quality, cleaning, and missingness assessments, and intermediate models and features you tried, though these should broadly be relevant to the tasks at hand.
- Make sure to clearly explain what each component of your notebook **means**. Specifically:
  - All plots should have titles, labels, and a legend (if applicable), even if they don't make it into your website. Plots should be self-contained – readers should be able to understand what they describe without having to read anything else.
  - All code cells should contain a comment describing how the code works (unless the code is self-explanatory – use your best judgement).

---

## Part 2: Report

Your website is the public-facing component of your Final Project. The purpose of your website is to provide the general public – your classmates, friends, family, recruiters, and random internet strangers – with an overview of your project and its findings, without forcing them to understand every last detail. Once you've completed your analysis and know _what_ you will put in your website, start reading this section.

The easiest (and free) option is to use GitHub Pages with [Jekyll](https://jekyllrb.com), a framework built into GitHub that allows you to create professional-looking websites just by writing Markdown. GitHub Pages does the "hard" part of converting your Markdown to HTML. In fact, [practicaldsc.org](https://practicaldsc.org) is built using Jekyll!

If you'd like, you can also choose to build a dynamic website using frameworks like Streamlit or Marimo, or do things more from scratch a la EECS 485. We will not be able to provide much guidance if you go down this path, so only go down this road if you've made custom websites before. The key requirement is that your website must be publicly accessible for your final submission.

{: .blue }
Read more about how to create your website [**here**](website).

---

## Submission and Rubric

Overall, the homework is worth 100 points. We describe the breakdown in the [Rubric](#rubric) section below.

### Checkpoint Submission

As mentioned at the top of this page, this project has a required checkpoint, worth **15 of the 100 points**. You can submit the checkpoint [**here on Gradescope**](https://www.gradescope.com/courses/930446/assignments/5948624). The checkpoint asks you to answer the following questions:

1. (3 points) Which of the three datasets did you choose and why? Or did you get pre-approval to choose your own dataset, and why?
1. (6 points) Upload a screenshot of a `plotly` visualization you've created while completing Part 1, Step 2: Data Cleaning and Exploratory Data Analysis.
1. (6 points) What is the column you plan on trying to predict in Part 1, Steps 3-5? Is it a classification or regression problem? Explain.

### Final Submission

You will ultimately submit your project in two ways:

1. By uploading a **PDF version** of your notebook to the specific "Final Project Notebook PDF (Dataset)" assignment on Gradescope that's specific to your dataset.
   - To export your notebook as a PDF, first, restart your kernel and run all cells. Then, go to "File > Print Preview". Then, save a print preview of the webpage as a PDF. There are other ways to save a notebook as a PDF but they may require that you have additional packages installed on your computer, so this is likely the most straightforward.
   - It's fine if your `plotly` graphs don't render in the PDF output of your notebook. However, **make sure none of the code is cut off in your notebook's PDF**. **You will lose 5% of the points available on this project if your code is cut off.**
   - This notebook asks you to include a link to your website; make sure to do so.
2. By submitting a **link to your website** to the "Final Project Website Link (All Datasets)" assignment on Gradescope.
   - We will use the links provided on Gradescope to create a "showcase site" with links to everyone's websites so that the rest of the class can see your work!
   - Here, you'll also need to provide your group member name(s), email(s), and the title of your website.

To both submissions, make sure to tag your partner. You don't need to submit your actual `.ipynb` file anywhere. **While your website must be public and you should share it with others, you should _not_ make your code for this project available publicly.**

{: .warning }
Remember that you can't use slip days on the final submission. There are a lot of moving parts to this assignment – don't wait until the last minute to try and submit!

### Rubric

Your project will be graded out of 100 points. The rough rubric is shown below. If you satisfy these requirements as described above, you will receive full credit.

Note that the rubric is intentionally vague when it comes to Steps 3-5. This is because an exact rubric would specify exactly what you need to do to build a model, but figuring out what to do is a large part of Steps 3-5.

| Component                                                                                                                                                                                                                                            | Weight         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **Checkpoint**                                                                                                                                                                                                                                       | 15 points      |
| **Step 1: Introduction**                                                                                                                                                                                                                             | 5 points       |
| **Step 2: Data Cleaning and Exploratory Data Analysis** <br>• Cleaned data (5 points)<br>• Performed univariate analyses (5 points)<br>• Performed bivariate analyses and aggregations (5 points)<br>• Commented on imputation strategies (5 points) | 20 points      |
| **Step 3: Framing a Prediction Problem**                                                                                                                                                                                                             | 5 points       |
| **Step 4: Baseline Model**                                                                                                                                                                                                                           | 20 points      |
| **Step 5: Final Model**                                                                                                                                                                                                                              | 25 points      |
| **Overall: Included all necessary components on the website**                                                                                                                                                                                        | 10 points      |
| **Total**                                                                                                                                                                                                                                            | **100 points** |

---

## Partner Guidelines

Working with a partner? Keep the following points in mind:

1. You are both required to actively contribute to all parts of the project. You must both be working on the assignment at the same time together, either physically or virtually on a Zoom call. You are encouraged to follow the **pair programming model**, in which you work on just a single computer and alternate who writes the code and who thinks about the problems at a high level. **In particular, you cannot split up the project and each work on separate parts independently.** So, you **cannot** say Partner 1 is responsible for the analysis and Partner 2 is responsible for the website.
1. You should decide on your partnership as soon as possible, but certainly before the checkpoint deadline of March 28th, which you're required to submit in your partnerships.
1. Ultimately, you will submit three deliverables for this project to three separate Gradescope assignments – the checkpoint, a PDF of your notebook, and a link to your website. **Make sure to have just one partner submit these deliverables, and have them tag the other partner!** That is, don't make duplicate submissions of the same work.