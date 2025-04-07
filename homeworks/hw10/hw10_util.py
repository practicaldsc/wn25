# Helper functions for Homework 10.

import pandas as pd
import numpy as np
import warnings
warnings.simplefilter('ignore')

import plotly
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

from plotly.subplots import make_subplots

# Preferred styles
pio.templates["pds"] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor="center"),
    )
)
pio.templates.default = "simple_white+pds"

# Use plotly as default plotting engine
pd.options.plotting.backend = "plotly"

def wine_scatter(X_train_wine, y_train_wine):
    fig = (
        X_train_wine.assign(Class=y_train_wine)
        .sort_values('Class')
        .plot(kind='scatter', 
              x='Alcohol', 
              y='Color Intensity', 
              color='Class', 
              color_discrete_map={'Grape 1': px.colors.qualitative.Vivid[0], 
                                  'Grape 2': px.colors.qualitative.Vivid[1], 
                                  'Grape 3': px.colors.qualitative.Vivid[2]},
              title='Color Intensity vs. Alcohol % by Grape Class')
        .update_layout(width=800)
        )
    return fig

def show_wine_decision_boundary(model, X_train_wine, y_train_wine, title=''):
    
    # Create grid for decision boundary
    tol = 0
    x_min, x_max = X_train_wine['Alcohol'].min() - tol, X_train_wine['Alcohol'].max() + tol
    y_min, y_max = X_train_wine['Color Intensity'].min() - tol, X_train_wine['Color Intensity'].max() + tol
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                        np.linspace(y_min, y_max, 400))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    Z = (Z == 'Grape 1') * 0 + (Z == 'Grape 2') * 0.5 + (Z == 'Grape 3') * 1

    color_map={'Grape 1': '#c45bcc', 'Grape 2': '#077575', 'Grape 3': '#ff7400'}

    # Create figure
    fig = make_subplots()
    
    # Add decision boundary
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, 400),
        y=np.linspace(y_min, y_max, 400),
        z=Z,
        colorscale=[[0, color_map['Grape 1']], [0.5, color_map['Grape 2']], [1, color_map['Grape 3']]],
        opacity=0.5,
        showscale=False
    ))

    for c in color_map:
        fig.add_trace(go.Scatter(
            x=X_train_wine.loc[y_train_wine == c, 'Alcohol'],
            y=X_train_wine.loc[y_train_wine == c, 'Color Intensity'],
            mode='markers',
            marker=dict(color=color_map[c], size=12),
            name=c
        ))

    # Update layout
    fig.update_layout(
        title=dict(text=title, font=dict(size=20)),
        xaxis_title='Alcohol',
        yaxis_title='Color Intensity',
        showlegend=True,
        legend=dict(font=dict(size=12)),
        width=800,
        height=600
    )

    fig.update_xaxes(range=[x_min, x_max])
    fig.update_yaxes(range=[y_min, y_max])

    return fig

def show_wine_decision_tree(model, X_train_wine):
    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt
    plt.figure(figsize=(14, 8), dpi=125)
    return plot_tree(model, feature_names=X_train_wine.columns, class_names=['Grape 1', 'Grape 2', 'Grape 3'], 
              filled=False, fontsize=10, impurity=False)

def show_wine_confusion_matrix(model, X_test_wine, y_test_wine):
    from sklearn.metrics import confusion_matrix
    
    y_pred = model.predict(X_test_wine)
    cm = confusion_matrix(y_test_wine, y_pred)

    labels = ['Grape 1', 'Grape 2', 'Grape 3']
    
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale='Purples',
        text=cm,
        texttemplate='%{text}',
        hovertemplate='Predicted %{x}<br>Actually %{y}<br>Count: %{z}<extra></extra>'
    ))
    
    # Update layout
    fig.update_layout(
        title='Wine Classification Confusion Matrix on Test Set',
        xaxis_title='Predicted Grape',
        yaxis_title='Actually Grape',
        xaxis=dict(tickmode='array', tickvals=list(range(len(labels))), ticktext=labels),
        yaxis=dict(tickmode='array', tickvals=list(range(len(labels))), ticktext=labels),
        width=600,
        height=600
    )
    
    return fig

def show_wine_decision_boundaries_grid(model_dict, X_train_wine, y_train_wine):
    # Create a 2x3 subplot grid
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=list(model_dict.keys()),
        horizontal_spacing=0.1,
        vertical_spacing=0.15
    )

    # Create grid for decision boundary
    tol = 0
    x_min, x_max = X_train_wine['Alcohol'].min() - tol, X_train_wine['Alcohol'].max() + tol
    y_min, y_max = X_train_wine['Color Intensity'].min() - tol, X_train_wine['Color Intensity'].max() + tol
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                        np.linspace(y_min, y_max, 400))

    color_map={'Grape 1': '#c45bcc', 'Grape 2': '#077575', 'Grape 3': '#ff7400'}

    # Add plots to each subplot
    for i, (model_name, model) in enumerate(model_dict.items(), 1):
        row = (i - 1) // 3 + 1  # Calculate row position
        col = (i - 1) % 3 + 1   # Calculate column position

        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        Z = (Z == 'Grape 1') * 0 + (Z == 'Grape 2') * 0.5 + (Z == 'Grape 3') * 1

        # Add decision boundary
        fig.add_trace(go.Contour(
            x=np.linspace(x_min, x_max, 400),
            y=np.linspace(y_min, y_max, 400),
            z=Z,
            colorscale=[[0, color_map['Grape 1']], [0.5, color_map['Grape 2']], [1, color_map['Grape 3']]],
            opacity=0.5,
            showscale=False
        ), row=row, col=col)

        # Add scatter points
        for c in color_map:
            fig.add_trace(go.Scatter(
                x=X_train_wine.loc[y_train_wine == c, 'Alcohol'],
                y=X_train_wine.loc[y_train_wine == c, 'Color Intensity'],
                mode='markers',
                marker=dict(color=color_map[c], size=8),
                name=c
            ), row=row, col=col)

    # Update layout
    fig.update_layout(
        showlegend=False,
        width=800,
        height=600
    )

    # Update axes for all subplots
    for i in range(1, 7):
        fig.update_xaxes(range=[x_min, x_max], title_text='Alcohol', row=(i-1)//3+1, col=(i-1)%3+1)
        fig.update_yaxes(range=[y_min, y_max], title_text='Color Intensity', row=(i-1)//3+1, col=(i-1)%3+1)

    return fig

def compute_and_plot_accuracies(model_dict, X_train_wine, y_train_wine, X_test_wine, y_test_wine, features, title='Model Accuracies'):
    # Calculate accuracies
    train_accuracies = {}
    test_accuracies = {}
    
    for model_name, model in model_dict.items():
        train_accuracies[model_name] = model.score(X_train_wine[features], y_train_wine)
        test_accuracies[model_name] = model.score(X_test_wine[features], y_test_wine)
    
    # Create bar chart
    fig = go.Figure()
    
    # Add training accuracy bars (blue)
    fig.add_trace(go.Bar(
        y=list(model_dict.keys()),
        x=list(train_accuracies.values()),
        name='Training Accuracy',
        orientation='h',
        marker_color=px.colors.qualitative.D3[0]
    ))
    
    # Add testing accuracy bars (orange)
    fig.add_trace(go.Bar(
        y=list(model_dict.keys()),
        x=list(test_accuracies.values()),
        name='Test Accuracy',
        orientation='h',
        marker_color=px.colors.qualitative.D3[1]
    ))
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Accuracy',
        yaxis_title='Model',
        barmode='group',
        width=800,
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def compare_model_dictionaries(model_dict1, model_dict2, X_train_wine, y_train_wine, X_test_wine, y_test_wine, features):
    # Create subplots with 1 row and 2 columns
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=('Pre-Standardization', 'Post-Standardization'),
        horizontal_spacing=0.25
    )
    
    # Plot first model dictionary
    fig1 = compute_and_plot_accuracies(model_dict1, X_train_wine, y_train_wine, X_test_wine, y_test_wine, features)
    for trace in fig1.data:
        fig.add_trace(trace, row=1, col=1)
    
    # Plot second model dictionary
    fig2 = compute_and_plot_accuracies(model_dict2, X_train_wine, y_train_wine, X_test_wine, y_test_wine, features)
    for trace in fig2.data:
        trace.showlegend=False
        fig.add_trace(trace, row=1, col=2)
    
    # Update layout
    fig.update_layout(
        width=1400,
        height=500,
        showlegend=True
    )
    
    # Update y-axis range to be consistent across both plots
    max_y = max(len(model_dict1), len(model_dict2))
    fig.update_yaxes(range=[-0.6, max_y - 0.25], row=1, col=1)
    fig.update_yaxes(range=[-0.6, max_y -0.25], row=1, col=2)
    
    return fig

# Helper functions for gradient descent.

def tukey(y_actual, y_pred, c=50):
    error = y_actual - y_pred
    if np.abs(error) <= c:
        return 1 - (1 - (error / c) ** 2) ** 3
    else:
        return 1

def empirical_risk(loss_function, w, xs, ys):
    return np.mean([
        loss_function(ys[i], w[0] + w[1] * xs[i], c=50)
        for i in range(len(xs))
    ])

def draw_loss_surface_tukey_commute(xs, ys, path=None):
    w0_range = np.linspace(80, 170, 100)
    w1_range = np.linspace(-15, 2, 100)
    w0_grid, w1_grid = np.meshgrid(w0_range, w1_range)
    
    loss_grid = np.zeros_like(w0_grid)
    for i in range(len(w0_range)):
        for j in range(len(w1_range)):
            loss_grid[j, i] = empirical_risk(tukey, [w0_range[i], w1_range[j]], xs, ys)

    fig = make_subplots(rows=1, cols=2, 
                       specs=[[{"type": "surface"}, {"type": "contour"}]],
                       column_widths=[0.6, 0.4])

    fig.add_trace(
        go.Surface(
            x=w0_grid,
            y=w1_grid,
            z=loss_grid,
            colorscale='RdBu_r',
            colorbar={"title": "Empirical Risk"},
        ),
        row=1, col=1
    )

    fig.add_trace(go.Contour(
            z=loss_grid,
            x=w0_range,
            y=w1_range,
            colorscale='RdBu_r',
            colorbar=dict(title='Empirical Risk'),
            contours=dict(
                showlabels=True,
                labelfont=dict(size=12, color='white')
                ),
            # xaxis_title="w0",
            # yaxis_title="w1"
        ),
        row=1, col=2
     )

    if path is not None:
        # Calculate step size to plot 100 points
        n_points = len(path)
        step = 1#max(1, n_points // 100)
        
        # Get the points to plot
        path_x = path[::step, 0]
        path_y = path[::step, 1]
        
        # Calculate the loss values for the path points
        path_z = np.array([empirical_risk(tukey, p, xs, ys) for p in path[::step]])
        
        # Add path to surface plot
        fig.add_trace(go.Scatter3d(
            x=path_x,
            y=path_y,
            z=path_z,
            mode='lines+markers',
            line=dict(color='gold', width=2),
            marker=dict(size=4, color='gold'),
            name='Gradient Descent Path',
            hovertemplate='Iteration: %{text}',
            text=[f'{i}' for i in range(len(path_x))]
        ), row=1, col=1)
        
        # Add path to contour plot
        fig.add_trace(go.Scatter(
            x=path_x,
            y=path_y,
            mode='lines+markers',
            line=dict(color='gold', width=2),
            marker=dict(size=4, color='gold'),
            name='Gradient Descent Path',
            hovertemplate='Iteration: %{text}',
            text=[f'{i}' for i in range(len(path_x))]
        ), row=1, col=2)

    title_text = 'Tukey Loss Surface using Commute Times Data'
    if path is not None:
        title_text += f'; <span style="color:gold">Gradient Descent Path in Gold ({len(path)} Total Steps)</span>'

    fig.update_layout(
        title_text=title_text, 
        width=1400, height=600, scene=dict(
            zaxis_title='R(w0, w1)',
            xaxis_title='w0',
            yaxis_title='w1',
            aspectratio=dict(x=1, y=1, z=1),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1))
        ),
    showlegend=False)

    fig.update_xaxes(title='w0', row=1, col=2)
    fig.update_yaxes(title='w1', row=1, col=2)
    
    return fig