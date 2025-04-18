import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from lec_utils import *


def fit_polys(train_sample, degs):
    # Create all three Pipelines.
    pls = [
        Pipeline(
            [("poly", PolynomialFeatures(d)), ("lin-reg", LinearRegression())]
        )
        for d in degs
    ]

    # Fit all three Pipelines.
    [pl.fit(train_sample[["x"]], train_sample["y"]) for pl in pls]

    # Return the relevant fit Pipelines.
    return pls


def train_and_plot(train_sample, test_sample, degs, data_name):
    pred_funcs = fit_polys(train_sample, degs)

    mses = [
            np.mean(
                (pred_funcs[i].predict(test_sample[["x"]]) - test_sample["y"])
                ** 2
            )
        for i in range(len(pred_funcs))
    ]
    titles = [
        f"Degree {degs[i]}, MSE: {np.round(mses[i], 3)}"
        for i in range(len(pred_funcs))
    ]

    fig = make_subplots(rows=1, cols=len(pred_funcs))

    for i in range(len(pred_funcs)):
        fig.add_trace(
            go.Scatter(
                x=test_sample["x"],
                y=test_sample["y"],
                name="Actual Data",
                mode="markers",
                marker={"color": "#4c72b0"},
            ),
            row=1,
            col=i + 1,
        )

        fig.add_trace(
            go.Scatter(
                x=test_sample["x"],
                y=pred_funcs[i].predict(test_sample[["x"]]),
                name="Predictions",
                line={"color": "orange", "width": 4},
            ),
            row=1,
            col=i + 1,
        )

    fig["data"][0]["name"] = data_name
    fig["data"][1]["name"] = "Fit Model"

    for i in range(2, len(fig["data"])):
        fig["data"][i]["showlegend"] = False

    for i, val in enumerate(titles):
        fig['layout'][f'xaxis{"" if i == 0 else i + 1}']['title'] = val
    #     fig['data'][i]['xaxis_title'] = titles[i]

    fig.update_layout(width=950, height=500)

    return fig


def plot_multiple_models(sample_1, sample_2, degs, data=False):
    sample_1_funcs = fit_polys(sample_1, degs)
    sample_2_funcs = fit_polys(sample_2, degs)

    fig = make_subplots(
        rows=1,
        cols=len(degs),
        subplot_titles=[f"Degree {deg}" for deg in degs],
    )

    for i in range(len(degs)):

        if data:
            fig.add_trace(
                        go.Scatter(
                            x=sample_1["x"],
                            y=sample_1["y"],
                            name="Sample 1",
                            mode="markers",
                            marker={"color": "#4c72b0"},
                        ),
                        row=1,
                        col=i + 1,
                    )

        fig.add_trace(
            go.Scatter(
                x=sample_1["x"],
                y=sample_1_funcs[i].predict(sample_1[["x"]]),
                line={"color": "orange", "width": 4},
            ),
            row=1,
            col=i + 1,
        )

        fig.add_trace(
            go.Scatter(
                x=sample_2["x"],
                y=sample_2_funcs[i].predict(sample_2[["x"]]),
                line={"color": "purple", "width": 4},
            ),
            row=1,
            col=i + 1,
        )

    if data:
        ranger = range(1, 3)
    else:
        ranger = range(2)

    for i in ranger:
        fig["data"][i]["name"] = f"Trained on Sample {i+(0 if data else 1)}"

    for i in range(max(ranger) + 1, len(fig["data"])):
        fig["data"][i]["showlegend"] = False

    fig.update_layout(width=950, height=500)

    return fig


def format_results(searcher):
    cv = sum([1 if ('split' in s and '_test_score' in s) else 0 for s in list(searcher.cv_results_.keys())])
    deg = searcher.cv_results_['mean_fit_time'].shape[0]
    
    df = -pd.DataFrame(np.vstack([searcher.cv_results_[f'split{i}_test_score'] for i in range(cv)]))
    df.index = [f'Fold {i}' for i in range(1, cv + 1)]
    df.columns = [f'Degree {j}' for j in range(1, deg + 1)]
    return df