from lec_utils import *
from ipywidgets import interact

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder, FunctionTransformer, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

from IPython.display import Markdown


def sample_from_pop(n=100):
    np.random.seed(23) # For reproducibility.
    x = np.linspace(-2, 3, n)
    y = x ** 3 + (np.random.normal(0, 3, size=n))
    return pd.DataFrame({'x': x, 'y': y})

def fit_and_show_fit(X_train, y_train, d=25):
    model = make_pipeline(PolynomialFeatures(d, include_bias=False), LinearRegression())
    model.fit(X_train, y_train)
    fig = px.scatter(x=X_train['x'], y=y_train, title="Sample 1's Training Data", width=1000, height=600)
    fig.add_trace(go.Scatter(
        x=X_train['x'].sort_values(),
        y=model.predict(X_train.sort_values('x')),
        mode='lines',
        line=dict(width=4),
        name=f'Fit Polynomial of Degree {d}'
    ))
    return model, fig

def display_poly(coefs, precision=2):
    from IPython.display import Markdown
    
    out = '$$'
    not_first_flag = False
    for exp, coef in enumerate(coefs):
        format_coef = f"{abs(coef):.{precision}f}"
        if exp == 0 and not np.isclose(coef, 0):
            out += format_coef
            not_first_flag = True
        else:
            if coef < 0:
                sign = '-'
            elif coef > 0:
                if not_first_flag:
                    sign = '+'
                else:
                    sign = ''
            if not np.isclose(coef, 0):
                out += sign + format_coef + 'x' + ('^{' + str(exp) + '}' if exp != 1 else '')
                not_first_flag = True
        
    display(Markdown(out + '$$'))

def display_features(poly_model, precision=2):
    display_poly(np.append(
    poly_model.intercept_,
    poly_model.coef_
), precision=precision)
    

# Inspiration: https://dsc40a.com/demos/6_regularization_demo
# Credits to Claude for the plotting code.
def plot_coefficient_magnitudes(poly_model):

    coefficients = poly_model.coef_

    # Create x-axis labels (w0, w1, w2, etc.)
    x_labels = [f'x^{i}' for i in range(1, len(coefficients) + 1)]
    
    # Separate positive and negative coefficients
    positive_coeffs = [max(0, coef) for coef in coefficients]
    negative_coeffs = [min(0, coef) for coef in coefficients]
    
    # Create traces for positive and negative coefficients
    trace_positive = go.Bar(
        x=x_labels,
        y=positive_coeffs,
        name='Positive Coefficients',
        marker_color='green'
    )
    
    trace_negative = go.Bar(
        x=x_labels,
        y=negative_coeffs,
        name='Negative Coefficients',
        marker_color='red'
    )
    
    # Create the layout
    layout = go.Layout(
        title='Coefficient Magnitudes',
        xaxis=dict(title='Degree'),
        yaxis=dict(title=r'$ \text{Coefficient } (w^*)$)'),
        barmode='relative',
        width=900,
        showlegend=False
    )
    
    # Create the figure
    fig = go.Figure(data=[trace_positive, trace_negative], layout=layout)
    
    return fig


def display_commute_coefs(best_estimator):
    names = np.append(
        'intercept', 
        best_estimator[:-1].get_feature_names_out())
    
    coefs = np.append(
        best_estimator[-1].intercept_,
        best_estimator[-1].coef_
    )
    
    assert len(names) == len(coefs), 'length of names != length of coefs'
    
    frame = pd.DataFrame().assign(feature=names, coef=coefs).set_index('feature')
    
    return frame

def plot_given_model_dict(X_train, y_train, model_dict):
    fig = px.scatter(x=X_train['x'], y=y_train, title="Sample 1's Training Data")

    for model in model_dict:
        model_obj, model_col = model_dict[model]
        fig.add_trace(go.Scatter(
            x=X_train['x'].sort_values(),
            y=model_obj.predict(X_train.sort_values('x')),
            mode='lines',
            line=dict(width=4, color=model_col),
            name=model
        ))

    fig.update_layout(width=1000, height=600)

    return fig

def show_ols_surface():
    
    df = pd.read_csv('data/commute-times.csv')
    df['day_of_month'] = pd.to_datetime(df['date']).dt.day
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    X_train, X_test, y_train, y_test = train_test_split(df.drop('minutes', axis=1), df['minutes'], random_state=23)

    X_train_design = X_train[['departure_hour', 'day_of_month']]
    X_train_design['1'] = 1
    X_train_design = X_train_design[['1', 'departure_hour', 'day_of_month']]
    
    def mse_for_commute_model(w):
        w = np.array([146.26, w[0], w[1]])
        return np.mean((y_train - X_train_design @ w) ** 2)

    num_points = 50
    uvalues = np.linspace(-35, 35, num_points)
    vvalues = np.linspace(-35, 35, num_points)
    (u,v) = np.meshgrid(uvalues, vvalues)
    ws = np.vstack((u.flatten(), v.flatten()))
    MSE = np.array([mse_for_commute_model(w) for w in ws.T])
    loss_surface = go.Surface(x=u, y=v, z=np.reshape(MSE, u.shape), showscale=True)

    fig = go.Figure(data=[loss_surface])
    
    w1_star, w2_star = (-8.777573705501238, 0.12760277945258872)
    
    fig.add_trace(go.Scatter3d(
        x=[w1_star],
        y=[w2_star],
        z=[mse_for_commute_model((w1_star, w2_star))],
        mode='markers',
        marker=dict(
            color='gold', 
            size=15,
            symbol='circle'
        )
    ))
    
    fig.add_trace(go.Scatter3d(
            x=[w1_star + 2],  # Slight offset to position annotation
            y=[w2_star+1],
            z=[mse_for_commute_model((w1_star, w2_star))],
            mode='text',
            text=['w*'],
            textfont=dict(
                color='gold',
                size=20
            )
    ))
    
    # fig.add_trace(opt_point)
    fig.update_layout(title=("Mean Squared Error for<br>Regression Model with 2 Features"), scene = dict(
        xaxis_title = "w1",
        yaxis_title = "w2",
        zaxis_title = 'Mean Squared Error'),
                     width=700, height=700, showlegend=False)
    
    return fig

import numpy as np
import plotly.graph_objs as go2

def show_ols_contour():

    df = pd.read_csv('data/commute-times.csv')
    df['day_of_month'] = pd.to_datetime(df['date']).dt.day
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    X_train, X_test, y_train, y_test = train_test_split(df.drop('minutes', axis=1), df['minutes'], random_state=23)

    X_train_design = X_train[['departure_hour', 'day_of_month']]
    X_train_design['1'] = 1
    X_train_design = X_train_design[['1', 'departure_hour', 'day_of_month']]
    
    def mse_for_commute_model(w):

        # Prepend fixed intercept term
        w_full = np.array([146, w[0], w[1]])
        
        # Predict using weights
        y_pred = X_train_design @ w_full
        
        # Calculate MSE
        mse = np.mean((y_train - y_pred) ** 2)
        
        return mse
    
    num_points = 100  # Increased for smoother contours
    uvalues = np.linspace(-35, 35, num_points)
    vvalues = np.linspace(-35, 35, num_points)
    u, v = np.meshgrid(uvalues, vvalues)
    
    loss_surface = np.array([
        mse_for_commute_model([wi, vi]) 
        for wi, vi in zip(u.flatten(), v.flatten())
    ]).reshape(u.shape)
            
    # Create Plotly figure with slider
    fig = go.Figure()

    w1_star, w2_star = (-8.777573705501238, 0.12760277945258872)
    
    fig.add_trace(go.Contour(
            z=loss_surface,
            x=uvalues,  # x-axis values
            y=vvalues,  # y-axis values
            colorscale='Viridis',
            showscale=True,
            contours=dict(
                start=np.min(loss_surface),
                end=np.max(loss_surface),
                size=(np.max(loss_surface) - np.min(loss_surface)) / 40,
                showlabels=True,
                labelfont=dict(size=8, color='white')
        )
    ))

    fig.add_trace(go.Scatter(
        x=[w1_star],
        y=[w2_star],
        mode='markers',
        marker=dict(
            color='gold', 
            size=15,
            symbol='circle'
        )
    ))
    
    fig.add_trace(go.Scatter(
            x=[w1_star-4],  # Slight offset to position annotation
            y=[w2_star],
            mode='text',
            text=['w*'],
            textfont=dict(
                color='gold',
                size=20
            )
    ))

    # Update layout
    fig.update_layout(
        title=("Mean Squared Error for Regression Model with 2 Features"),
        xaxis_title="w1",
        yaxis_title="w2",
        width=700, 
        height=700,
        showlegend=False
    )
    
    return fig

def show_ridge_contour():
    df = pd.read_csv('data/commute-times.csv')
    df['day_of_month'] = pd.to_datetime(df['date']).dt.day
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    X_train, X_test, y_train, y_test = train_test_split(df.drop('minutes', axis=1), df['minutes'], random_state=23)
    X_train_design = X_train[['departure_hour', 'day_of_month']]
    X_train_design['1'] = 1
    X_train_design = X_train_design[['1', 'departure_hour', 'day_of_month']]
    
    def mse_for_commute_model(w):
        w_full = np.array([146, w[0], w[1]])
        y_pred = X_train_design @ w_full
        mse = np.mean((y_train - y_pred) ** 2)
        return mse
    
    num_points = 100
    uvalues = np.linspace(-35, 35, num_points)
    vvalues = np.linspace(-35, 35, num_points)
    u, v = np.meshgrid(uvalues, vvalues)
    
    loss_surface = np.array([
        mse_for_commute_model([wi, vi]) 
        for wi, vi in zip(u.flatten(), v.flatten())
    ]).reshape(u.shape)
            
    # Create Plotly figure with slider
    fig = go.Figure()
    
    fig.add_trace(go.Contour(
            z=loss_surface,
            x=uvalues,
            y=vvalues,
            colorscale='Viridis',
            showscale=True,
            contours=dict(
                start=np.min(loss_surface),
                end=np.max(loss_surface),
                size=(np.max(loss_surface) - np.min(loss_surface)) / 40,
                showlabels=True,
                labelfont=dict(size=8, color='white')
        )
    ))
    
    # Add default lambda constraint circle
    lambda_default = 0.001  # Default lambda value
    default_circle_x = np.cos(np.linspace(0, 2*np.pi, 100)) / np.sqrt(lambda_default)
    default_circle_y = np.sin(np.linspace(0, 2*np.pi, 100)) / np.sqrt(lambda_default)
    
    fig.add_trace(go.Scatter(
        x=default_circle_x,
        y=default_circle_y,
        mode='lines',
        fill='toself',
        fillcolor='rgba(255,0,0,0.2)',
        line=dict(color='red'),
        name='Regularization Constraint'
    ))
    
    w1_star, w2_star = (-8.777573705501238, 0.12760277945258872)
    fig.add_trace(go.Scatter(
        x=[w1_star],
        y=[w2_star],
        mode='markers',
        marker=dict(
            color='gold', 
            size=15,
            symbol='circle'
        ),
        name='Optimal Weights'
    ))
    
    fig.add_trace(go.Scatter(
            x=[w1_star-4],  # Slight offset to position annotation
            y=[w2_star],
            mode='text',
            text=['w*'],
            textfont=dict(
                color='gold',
                size=20
            )
    ))
    
    # Update layout to include slider and add top padding
    fig.update_layout(
        title={"text": "Mean Squared Error with <span style='color:red'>Ridge Regression Constraint</span>"},
        xaxis_title="w1",
        yaxis_title="w2",
        width=700, 
        height=700,
        showlegend=False,
        sliders=[{
            'active': 0,
            'currentvalue': {'prefix': r'Regularization Hyperparameter: '},
            'pad': {'t': 50},
            'steps': [{
                'method': 'restyle',
                'args': [
                    {'x': [np.cos(np.linspace(0, 2*np.pi, 100)) / np.sqrt(10**(-3 + i/20))],
                     'y': [np.sin(np.linspace(0, 2*np.pi, 100)) / np.sqrt(10**(-3 + i/20))]},
                    [1]
                ],
                'label': f'λ={10**(-3 + i/20):.3f}'
            } for i in range(1, 41)]
        }]
    )
    
    return fig


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split

def show_lasso_contour():
    df = pd.read_csv('data/commute-times.csv')
    df['day_of_month'] = pd.to_datetime(df['date']).dt.day
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    X_train, X_test, y_train, y_test = train_test_split(df.drop('minutes', axis=1), df['minutes'], random_state=23)
    X_train_design = X_train[['departure_hour', 'day_of_month']]
    X_train_design['1'] = 1
    X_train_design = X_train_design[['1', 'departure_hour', 'day_of_month']]
    
    def mse_for_commute_model(w):
        w_full = np.array([146, w[0], w[1]])
        y_pred = X_train_design @ w_full
        mse = np.mean((y_train - y_pred) ** 2)
        return mse
    
    num_points = 100
    uvalues = np.linspace(-35, 35, num_points)
    vvalues = np.linspace(-35, 35, num_points)
    u, v = np.meshgrid(uvalues, vvalues)
    
    loss_surface = np.array([
        mse_for_commute_model([wi, vi]) 
        for wi, vi in zip(u.flatten(), v.flatten())
    ]).reshape(u.shape)
            
    # Create Plotly figure with slider
    fig = go.Figure()
    
    fig.add_trace(go.Contour(
            z=loss_surface,
            x=uvalues,
            y=vvalues,
            colorscale='Viridis',
            showscale=True,
            contours=dict(
                start=np.min(loss_surface),
                end=np.max(loss_surface),
                size=(np.max(loss_surface) - np.min(loss_surface)) / 40,
                showlabels=True,
                labelfont=dict(size=8, color='white')
        )
    ))

    def l1_norm_ball(r):
        # Generate x values from -r to r
        x_values = np.linspace(-r, r, 1000)
        
        # Calculate corresponding y values for each x
        y_positive = r - np.abs(x_values)
        y_negative = -y_positive
        
        # Return x and y values to fill in
        return np.concatenate([x_values, x_values[::-1]]), np.concatenate([y_positive, y_negative])

    # Add default lambda constraint circle
    lambda_default = 0.001  # Default lambda value
    default_circle_x, default_circle_y = l1_norm_ball(1 / np.sqrt(lambda_default))
    
    norm_ball = fig.add_trace(go.Scatter(
        x=default_circle_x,
        y=default_circle_y,
        mode='lines',
        fill='toself',
        fillcolor='rgba(255,0,0,0.2)',
        line=dict(color='red'),
        name='Regularization Constraint'
    ))
    
    w1_star, w2_star = (-8.777573705501238, 0.12760277945258872)
    fig.add_trace(go.Scatter(
        x=[w1_star],
        y=[w2_star],
        mode='markers',
        marker=dict(
            color='gold', 
            size=15,
            symbol='circle'
        ),
        name='Optimal Weights'
    ))
    
    fig.add_trace(go.Scatter(
            x=[w1_star-4],  # Slight offset to position annotation
            y=[w2_star],
            mode='text',
            text=['w*'],
            textfont=dict(
                color='gold',
                size=20
            )
    ))
    
    # Update layout to include slider and add top padding
    fig.update_layout(
        title={"text": "Mean Squared Error with <span style='color:red'>LASSO (L1) Constraint</span>"},
        xaxis_title="w1",
        yaxis_title="w2",
        width=700, 
        height=700,
        showlegend=False,
        sliders=[{
            'active': 0,
            'currentvalue': {'prefix': r'Regularization Hyperparameter: '},
            'pad': {'t': 50},
            'steps': [{
                'method': 'restyle',
                'args': [
                    {'x': [l1_norm_ball(1 / np.sqrt(10**(-3 + i/20)))[0]], 
                     'y': [l1_norm_ball(1 / np.sqrt(10**(-3 + i/20)))[1]]},
                    [1]  # The trace index (1 for the second trace, i.e., the norm ball trace)
                ],
                'label': f'λ={10**(-3 + i/20):.3f}'
            } for i in range(1, 41)]
        }]
    )

    return fig