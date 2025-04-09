from lec_utils import *
from ipywidgets import interact

### Classification part ---

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

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve
from sklearn.linear_model import LogisticRegression

def predict_thresholded(X_train, y_train, X, T):
    model_logistic_multiple = LogisticRegression()
    model_logistic_multiple.fit(X_train, y_train)
    probs = model_logistic_multiple.predict_proba(X)[:, 1]
    return (probs >= T).astype(int)

def plot_vs_threshold(X_train, y_train, metric):

    fn_dict = {'Precision': precision_score, 'Recall': recall_score, 'Accuracy': accuracy_score, 'F1 Score': f1_score}

    metric_fn = fn_dict[metric]

    thresholds = np.arange(0, 1.005, 0.005)
    values = []
    for t in thresholds:
        preds = predict_thresholded(X_train, y_train, X_train, t)
        value = metric_fn(y_train, preds)
        values.append(value)
        
    fig = px.line(x=thresholds, y=values,
                  title=f'{metric} vs. Threshold',
                  labels={'x': 'Threshold', 'y': f'Training {metric}'})
    
    return fig.update_layout(width=800)

def pr_curve(X_train, y_train):

    precisions = []
    recalls = []

    thresholds = np.arange(0, 1.005, 0.005)
    values = []
    for t in thresholds:
        preds = predict_thresholded(X_train, y_train, X_train, t)
        precision = precision_score(y_train, preds)
        recall = recall_score(y_train, preds)
        precisions.append(precision)
        recalls.append(recall)
        
    fig = px.line(x=recalls, y=precisions, hover_name='Threshold = ' + pd.Series(thresholds).astype(str),
                  title=f'Precision vs. Recall',
                  labels={'x': 'Recall', 'y': f'Precision'})
    
    return fig.update_layout(width=800)


def draw_roc_curve(X_train, y_train):
    model_logistic_multiple = LogisticRegression()
    model_logistic_multiple.fit(X_train, y_train)
    probs = model_logistic_multiple.predict_proba(X_train)[:, 1]

    fprs, tprs, thresholds = roc_curve(y_train.to_numpy(), probs)
        
    fig = px.line(x=fprs, y=tprs, hover_name='Threshold = ' + pd.Series(thresholds).astype(str),
                  title=f'ROC Curve<br>(True Positive Rate vs. False Positive Rate)',
                  labels={'x': 'False Positive Rate', 'y': 'True Positive Rate'})
    
    return fig.update_layout(width=800)

from sklearn.metrics import confusion_matrix

def show_confusion(X_train, y_train, T):
    # Get predictions and confusion matrix
    y_pred = predict_thresholded(X_train, y_train, X_train, T)
    cm = confusion_matrix(y_train, y_pred)
    
    # Create plotly heatmap
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=['Predicted Negative', 'Predicted Positive'],
        y=['Actual Negative', 'Actual Positive'],
        colorscale='Blues',
        text=[['True Negatives (TN)', 'False Positives (FP)'],
              ['False Negatives (FN)', 'True Positives (TP)']],
        texttemplate='%{text}<br>%{z}',
        textfont=dict(size=12),
        hovertemplate='Count: %{z}<br>Category: %{text}'
    ))

    # Update layout
    fig.update_layout(
        title=dict(
            text=f'Confusion Matrix<br>with Threshold {T}',
            y=0.95,  # Adjust title position
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        width=600,
        height=500,
        margin=dict(t=90),  # Add top margin
        xaxis=dict(side='top'),
        yaxis=dict(autorange='reversed')
    )

    return fig

def show_one_feature_plot(X_train, y_train):
    fig = px.scatter(X_train.assign(Diabetes=y_train, 
                          Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})),
           x='Glucose',
           y='Diabetes',
           color='Outcome',
           color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
           width=800, size=np.ones(X_train.shape[0]), size_max=8)
    return fig

def show_one_feature_plot_in_1D(X_train, y_train, thres=True):

    fig = px.scatter(X_train.assign(Diabetes=y_train, 
                          Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})),
           x='Glucose',
           y=[0] * X_train.shape[0],
           color='Outcome',
           color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
           size_max=10,
           size=[5] * X_train.shape[0],
           width=1000)
    
    if thres:
        fig.add_trace(go.Scatter(
            x=[139.17, 139.17],
            y=[-0.1, 0.1],
            name=f'Threshold of Glucose = 140',
            line=(dict(color='purple', width=4))
        ))

    fig.update_yaxes(range=(-0.03, 0.03))

    fig.add_annotation(
        x=170,
        y=0.015,
        text="<span style='color:blue'>classified as <b>diabetes</b> ➡️</span>",
        showarrow=False
    )

    fig.add_annotation(
        x=100,
        y=0.015,
        text="<span style='color:orange'>⬅️ classified as <b>no diabetes</b></span>",
        showarrow=False
    )

    return fig

def create_base_scatter(X_train, y_train):
    fig = (
        X_train.assign(Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'}))
                .plot(kind='scatter', x='Glucose', y='BMI', color='Outcome', 
                      color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                      title='Relationship between Glucose, BMI, and Diabetes', size_max=7, size=[1] * len(X_train))
                .update_layout(width=700, height=500)
    )
    return fig

def lin_sep_1D():
    df = pd.DataFrame().assign(x=[1, 2, 4, 9, 12, 15, 16, 20, 20.5], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['x'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y=[0] * df.shape[0], color='Outcome', size_max=10, size=[5] * df.shape[0], width=600, height=200, 
                   title='Linearly Separable, d=1',
                   color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},)

def lin_sep_1D_elevated():
    df = pd.DataFrame().assign(x=[1, 2, 4, 9, 12, 15, 16, 20, 20.5], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['x'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y='y', color='Outcome', size_max=10, size=[5] * df.shape[0], width=800, height=400, 
                   title='Linearly Separable, d=1',
                   color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},)

def non_lin_sep_1D():
    df = pd.DataFrame().assign(Glucose=[1, 2, 20.5, 9, 12, 16, 15, 20, 4], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['Glucose'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y=[0] * df.shape[0], color='Outcome', size_max=10, size=[5] * df.shape[0], width=800, height=200, 
                   title='NOT Linearly Separable, d=1', color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'})

def bad_example_1D():
    df = pd.DataFrame().assign(Glucose=[1, 2, 20.5, 9, 12, 16, 15, 20, 4], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['Glucose'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y='y', color='Outcome', size_max=10, size=[5] * df.shape[0], width=800, height=200, 
                   title='NOT Linearly Separable, d=1', color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'})


def lin_sep_2D():

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate linearly separable data
    # Class 1: Points clustered around (2, 2)
    class1_x = np.random.normal(2, 0.5, 10)
    class1_y = np.random.normal(2, 0.5, 10)

    # Class 2: Points clustered around (5, 5)
    class2_x = np.random.normal(3.5, 0.5, 10)
    class2_y = np.random.normal(3.5, 0.5, 10)

    # Create DataFrame
    df = pd.DataFrame({
        'x': np.concatenate([class1_x, class2_x]),
        'y': np.concatenate([class1_y, class2_y]),
        'Outcome': ['no diabetes']*10 + ['yes diabetes']*10
    })

    df['x'] = df['x'] * 35
    df['y'] = 20 + df['y'] * 5

    # Create Plotly figure
    fig = px.scatter(df, x='x', y='y', color='Outcome', 
                     title='Linearly Separable, d=2',
                     labels={'x': 'Glucose', 'y': 'BMI'},
                     color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                     size_max=10, size=[5] * df.shape[0], width=800)


    return fig

def non_lin_sep_2D():

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate linearly separable data
    # Class 1: Points clustered around (2, 2)
    class1_x = np.random.normal(2, 1.5, 10)
    class1_y = np.random.normal(2, 1.5, 10)

    # Class 2: Points clustered around (5, 5)
    class2_x = np.random.normal(3.5, 2.5, 10)
    class2_y = np.random.normal(3.5, 2.5, 10)

    # Create DataFrame
    df = pd.DataFrame({
        'x': np.concatenate([class1_x, class2_x]),
        'y': np.concatenate([class1_y, class2_y]),
        'Outcome': ['no diabetes']*10 + ['yes diabetes']*10
    })

    df['x'] = df['x'] * 35
    df['y'] = 20 + df['y'] * 5

    # Create Plotly figure
    fig = px.scatter(df, x='x', y='y', color='Outcome', 
                     title='NOT Linearly Separable, d=2',
                     labels={'x': 'Glucose', 'y': 'BMI'},
                     color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                     size_max=10, size=[5] * df.shape[0], width=800)


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

    dpi = 600
    
    # Create grid for decision boundary
    tol = 0
    x_min, x_max = X_train['bill_length_mm'].min() - tol, X_train['bill_length_mm'].max() + tol
    y_min, y_max = X_train['body_mass_g'].min() - tol, X_train['body_mass_g'].max() + tol
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, dpi),
                        np.linspace(y_min, y_max, dpi))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    Z = (Z == 'Adelie') * 0 + (Z == 'Chinstrap') * 0.5 + (Z == 'Gentoo') * 1

    color_map={'Chinstrap': '#c45bcc', 'Gentoo': '#077575', 'Adelie': '#ff7400'}

    # Create figure
    fig = make_subplots()
    
    # Add decision boundary
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, dpi),
        y=np.linspace(y_min, y_max, dpi),
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