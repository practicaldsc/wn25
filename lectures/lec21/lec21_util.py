from lec_utils import *
from ipywidgets import interact
import pickle
import os

from sklearn.neighbors import KNeighborsClassifier

def create_base_scatter(X_train, y_train):
    fig = (
        X_train.assign(Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'}))
                .plot(kind='scatter', x='Glucose', y='BMI', color='Outcome', 
                      color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                      title='Relationship between Glucose, BMI, and Diabetes', size_max=7, size=[1] * len(X_train))
                .update_layout(width=700, height=500)
    )
    return fig

def show_decision_boundary(model, X_train, y_train, title=''):
    from plotly.subplots import make_subplots

    # Create grid for decision boundary
    tol = 0
    x_min, x_max = X_train['Glucose'].min() - tol, X_train['Glucose'].max() + tol
    y_min, y_max = X_train['BMI'].min() - tol, X_train['BMI'].max() + tol
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                        np.linspace(y_min, y_max, 400))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Create figure
    fig = make_subplots()
    
    # Add decision boundary
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, 400),
        y=np.linspace(y_min, y_max, 400),
        z=Z,
        colorscale=[(0, 'orange'), (1, 'blue')],
        opacity=0.5,
        showscale=False
    ))

    # Add scatter points
    fig.add_trace(go.Scatter(
        x=X_train.loc[y_train == 0, 'Glucose'],
        y=X_train.loc[y_train == 0, 'BMI'],
        mode='markers',
        marker=dict(color='orange', size=8),
        name='no diabetes'
    ))
    
    fig.add_trace(go.Scatter(
        x=X_train.loc[y_train == 1, 'Glucose'],
        y=X_train.loc[y_train == 1, 'BMI'],
        mode='markers',
        marker=dict(color='blue', size=8),
        name='yes diabetes'
    ))

    # Update layout
    fig.update_layout(
        title=dict(text=title, font=dict(size=20)),
        xaxis_title='Glucose',
        yaxis_title='BMI',
        showlegend=True,
        legend=dict(font=dict(size=12)),
        width=700,
        height=500
    )

    fig.update_xaxes(range=[x_min, x_max])
    fig.update_yaxes(range=[y_min, y_max])

    return fig

def visualize_k(k, X_train, y_train):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return show_decision_boundary(model, X_train, y_train, title='k-NN Decision Boundary for k = ' + str(k))

def visualize_depth(depth, X_train, y_train):
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X_train, y_train)
    return show_decision_boundary(model, X_train, y_train, title='Decision Boundary for a Tree of Depth ' + str(depth))

def plot_sigmoid(w0, w1):
    xs = np.linspace(-10, 10)
    inps = w0 + w1 * xs
    ys = 1 / (1 + np.e ** (-inps))
    
    title = r'$y = \sigma(' + (f'{w0} +' if w0 != 0 else '') +  (f'{w1}x' if w1 != 1 else 'x') + r')$'

    fig = px.line(x=xs, y=ys, title=title)
    
    return fig

def show_three_sigmoids():
    fig1 = plot_sigmoid(w0=0, w1=1)
    fig2 = plot_sigmoid(w0=-15, w1=5)
    fig3 = plot_sigmoid(w0=-0.5, w1=-0.4)

    combined_fig = make_subplots(rows=1, cols=3,
                                 subplot_titles = [figi.layout.title['text'] for figi in [fig1, fig2, fig3]])

    combined_fig.add_trace(fig1.data[0], row=1, col=1)
    combined_fig.add_trace(fig2.data[0], row=1, col=2)
    combined_fig.add_trace(fig3.data[0], row=1, col=3)

    combined_fig.update_layout(width=1200)
    
    return combined_fig

def show_logistic(model_logistic, X_train, y_train, t=0.5, show_training=False, show_threshold=False):
    num_points = 50
    glucoses = np.linspace(0, 210, num_points)
    bmis = np.linspace(0, 80, num_points)
    (gridX, gridY) = np.meshgrid(glucoses, bmis)

    # Reshape grid for predict_proba
    grid = np.column_stack((gridX.ravel(), gridY.ravel()))
    grid = pd.DataFrame(grid, columns=['Glucose', 'BMI'])
    Z = model_logistic.predict_proba(grid)[:, 1].reshape(gridX.shape)

    surface = go.Surface(x=gridX, y=gridY, z=Z, colorscale='Blues', name='Predicted Probabilities', showscale=False)

    data = go.Scatter3d(x=X_train['Glucose'], y=X_train['BMI'], z=y_train, 
                        mode='markers', marker={'size': 5, 'color': 'black'},
                        name='Training Data')
    
    threshold = go.Surface(x=gridX, y=gridY, z=Z * 0 + t, colorscale='greens', showscale=False)
    
    figs = [surface]
    
    if show_training:
        figs.append(data)

    if show_threshold:
        figs.append(threshold)
        
    fig = go.Figure(figs)
        
    fig.update_layout(title=f'Predicted Probability of Diabetes Given Glucose and BMI' + (f'<br>Threshold = {t}' if t != 0.5 else ''), 
                      width=1000, height=800, scene = dict(
        xaxis_title = "Glucose",
        yaxis_title = "BMI",
        zaxis_title = "Probability"), showlegend=True)
    
    return fig

def precompute_models(X_train, y_train):
    """Precompute KNN models for k=1 to 51 and save them to a file"""
    models = {}
    for k in range(1, 52):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        models[k] = model
    
    # Save models to file
    with open('data/precomputed_knn_models.pkl', 'wb') as f:
        pickle.dump(models, f)
    
    return models

def load_precomputed_models():
    """Load precomputed models from file"""
    if os.path.exists('data/precomputed_knn_models.pkl'):
        with open('data/precomputed_knn_models.pkl', 'rb') as f:
            return pickle.load(f)
    return None

# This is saved to disk in the notebook and reloaded in by the pickling defined below.
def decision_boundary_slide_k(X_train, y_train, k_max=50):
    """Create a slider for decision boundaries with precomputed models"""
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    # Load precomputed models
    models = load_precomputed_models()
    if models is None:
        print("Precomputing models...")
        models = precompute_models(X_train, y_train)

    else:
        print("Using precomputed models...")
    
    # Create grid for decision boundary
    x_min, x_max = X_train['Glucose'].min(), X_train['Glucose'].max()
    y_min, y_max = X_train['BMI'].min(), X_train['BMI'].max()
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                        np.linspace(y_min, y_max, 400))
    
    # Create figure
    fig = make_subplots()
    
    # Add scatter points (they will be the same for all k)
    fig.add_trace(go.Scatter(
        x=X_train.loc[y_train == 0, 'Glucose'],
        y=X_train.loc[y_train == 0, 'BMI'],
        mode='markers',
        marker=dict(color='orange', size=8),
        name='no diabetes'
    ))
    
    fig.add_trace(go.Scatter(
        x=X_train.loc[y_train == 1, 'Glucose'],
        y=X_train.loc[y_train == 1, 'BMI'],
        mode='markers',
        marker=dict(color='blue', size=8),
        name='diabetes'
    ))
    
    # Create frames for each k
    frames = []
    for k in range(1, k_max+1):
        model = models[k]
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
        # Create a frame with only the contour trace
        frames.append(go.Frame(
            data=[go.Contour(
                x=np.linspace(x_min, x_max, 400),
                y=np.linspace(y_min, y_max, 400),
                z=Z,
                colorscale='Plotly3',
                opacity=0.5,
                showscale=False
            ),
            go.Scatter(
                x=X_train.loc[y_train == 0, 'Glucose'],
                y=X_train.loc[y_train == 0, 'BMI'],
                mode='markers',
                marker=dict(color='orange', size=8),
                name='no diabetes'
            ),
            go.Scatter(
                x=X_train.loc[y_train == 1, 'Glucose'],
                y=X_train.loc[y_train == 1, 'BMI'],
                mode='markers',
                marker=dict(color='blue', size=8),
                name='diabetes'
            )],
            name=f'k={k}',
            layout=go.Layout(
                title=dict(text='k-NN Decision Boundary for k = ' + str(k), font=dict(size=20))
            )
        ))
    
    # Add initial contour (for k=1)
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, 400),
        y=np.linspace(y_min, y_max, 400),
        z=models[1].predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape),
        colorscale='Plotly3',
        opacity=0.5,
        showscale=False
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(text='k-NN Decision Boundary for k = 1', font=dict(size=20)),
        xaxis_title='Glucose',
        yaxis_title='BMI',
        showlegend=True,
        legend=dict(font=dict(size=12)),
        width=700,
        height=500,
        updatemenus=[{
            'type': 'buttons',
            'buttons': [
                {
                    'label': '▶️ Play',
                    'method': 'animate',
                    'args': [None, {
                        'frame': {'duration': 1000, 'redraw': True},
                        'fromcurrent': True,
                        'transition': {'duration': 0, 'easing': 'sin'}
                    }]
                }
            ]
        }]
    )
    
    # Add slider
    fig.update_layout(
        sliders=[{
            'active': 0,
            'currentvalue': {
                'prefix': 'k = ',
                'font': {'size': 16}
            },
            'steps': [{'args': [
                [f'k={k}'],
                {'frame': {'duration': 0, 'redraw': True},
                 'mode': 'immediate',
                 'transition': {'duration': 0, 'easing': 'sin'}}
            ],
                      'label': str(k),
                      'method': 'animate'} for k in range(1, k_max+1)]
        }]
    )

    fig.update_xaxes(range=[x_min, x_max])
    fig.update_yaxes(range=[y_min, y_max])
    
    # Add frames to figure
    fig.frames = frames
    
    return fig

def show_slider():
    with open('imgs/knn-slider.pkl', 'rb') as f:
        knn_slider = pickle.load(f)
    display(knn_slider)

def create_scaled_version(X_train, y_train):
    X_train_scaled = X_train.copy()
    X_train_scaled['Glucose * 2'] = X_train_scaled['Glucose'] * 2
    fig = (
        X_train_scaled.assign(Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'}))
        .plot(kind='scatter', x='Glucose * 2', y='BMI', color='Outcome', 
                      color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                      title='Relationship between Glucose * 2, BMI, and Diabetes')
                .update_layout(width=1300)
                .update_xaxes(tickvals=np.arange(0, 500, 100))
    )
    return fig

def show_diabetes_decision_tree(model_tree, X_train):
    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 5))
    return plot_tree(model_tree, feature_names=X_train.columns, class_names=['no db', 'yes db'], 
              filled=True, fontsize=10, impurity=False)

def penguin_scatter_3d(X_train, y_train):
    fig = px.scatter_3d(X_train, 
                x='bill_length_mm', 
                y='body_mass_g', 
                z='bill_depth_mm',
                color=y_train, 
                color_discrete_map={'Chinstrap': '#c45bcc', 'Gentoo': '#077575', 'Adelie': '#ff7400'},
                title='Bill Depth vs. Bill Length and Body Mass',
                width=800, height=600)

    fig.add_layout_image(
        dict(
            source="imgs/lter_penguins.png",
            xref="paper",
            yref="paper",
            x=0.7,
            y=0.8,
            sizex=0.35,
            sizey=0.35,
            xanchor="left",
            yanchor="top",
            opacity=0.7,
            layer="above"
        )
    )

    fig.update_layout(showlegend=False)

    return fig
    

def penguin_scatter_2d(X_train, y_train):
    fig = px.scatter(X_train, 
                x='bill_length_mm', 
                y='body_mass_g', 
                color=y_train, 
                title='Body Mass vs. Bill Length',
                color_discrete_map={'Chinstrap': '#c45bcc', 'Gentoo': '#077575', 'Adelie': '#ff7400'},
                width=800, height=600,
                size_max=10,
                size=[5] * X_train.shape[0])


    fig.add_layout_image(
        dict(
            source="imgs/lter_penguins.png",
            xref="paper",
            yref="paper",
            x=0.05,
            y=0.95,
            sizex=0.35,
            sizey=0.35,
            xanchor="left",
            yanchor="top",
            opacity=0.7,
            layer="above"
        )
    )

    fig.update_layout(showlegend=False, xaxis_title='Bill Length', yaxis_title='Body Mass')

    return fig

def penguin_decision_boundary(model, X_train, y_train, title=''):
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    # Create grid for decision boundary
    tol = 0
    x_min, x_max = X_train['bill_length_mm'].min() - tol, X_train['bill_length_mm'].max() + tol
    y_min, y_max = X_train['body_mass_g'].min() - tol, X_train['body_mass_g'].max() + tol
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                        np.linspace(y_min, y_max, 400))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    Z = (Z == 'Adelie') * 0 + (Z == 'Chinstrap') * 0.5 + (Z == 'Gentoo') * 1

    color_map={'Chinstrap': '#c45bcc', 'Gentoo': '#077575', 'Adelie': '#ff7400'}

    # Create figure
    fig = make_subplots()
    
    # Add decision boundary
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, 400),
        y=np.linspace(y_min, y_max, 400),
        z=Z,
        colorscale=[[0, color_map['Adelie']], [0.5, color_map['Chinstrap']], [1, color_map['Gentoo']]],
        opacity=0.5,
        showscale=False
    ))

    for c in color_map:
        fig.add_trace(go.Scatter(
            x=X_train.loc[y_train == c, 'bill_length_mm'],
            y=X_train.loc[y_train == c, 'body_mass_g'],
            mode='markers',
            marker=dict(color=color_map[c], size=12),
            name=c
        ))

    # Update layout
    fig.update_layout(
        title=dict(text=title, font=dict(size=20)),
        xaxis_title='Bill Length',
        yaxis_title='Body Mass',
        showlegend=True,
        legend=dict(font=dict(size=12)),
        width=800,
        height=600
    )

    fig.update_xaxes(range=[x_min, x_max])
    fig.update_yaxes(range=[y_min, y_max])

    fig.add_layout_image(
        dict(
            source="imgs/lter_penguins.png",
            xref="paper",
            yref="paper",
            x=0.05,
            y=0.95,
            sizex=0.35,
            sizey=0.35,
            xanchor="left",
            yanchor="top",
            opacity=0.7,
            layer="above"
        )
    )

    fig.update_layout(showlegend=False)

    return fig

def show_penguin_decision_tree(model_tree, X_train):
    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 5))
    return plot_tree(model_tree, feature_names=X_train.columns, class_names=['Adelie', 'Gentoo', 'Chinstrap'], 
              filled=True, fontsize=10, impurity=False)
