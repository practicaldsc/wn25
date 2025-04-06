from lec_utils import *
from ipywidgets import interact

from IPython.display import Markdown

def f(w):
    return 5 * (w**4) - (w**3) - 5 * (w**2) + 2 * w - 9

def df(w):
    return 20 * (w**3) - 3 * (w**2) - 10 * w + 2

def create_tangent_line(w):
    slope = df(w)
    intercept = f(w) - slope * w
    return lambda w: intercept + slope * w

def draw_f():
    ws = np.linspace(-1.25, 1.25, 1000)
    ys = f(ws)

    fig = px.line(x=ws, y=ys)
    fig.update_layout(xaxis_title='$w$', 
                  yaxis_title='$f(w)$', 
                  title='$f(w) = 5w^4 - w^3 - 5w^2 + 2w - 9$',
                  width=800, height=500)
    
    return fig
    
def show_tangent(w0):
    fig = draw_f()
    tan_fn = create_tangent_line(w0)
    fig2 = go.Figure(fig.data)
    fig2.add_trace(go.Scatter(x=[w0], y=[f(w0)], marker={'color': 'red', 'size': 20}, showlegend=False))
    fig2.add_trace(go.Scatter(x=[-5, 5], y=[tan_fn(-5), tan_fn(5)], line={'color': 'red'}, name='Tangent Line'))
    fig2.update_xaxes(range=[-1.25, 1.25]).update_yaxes(range=[-12, -4])
    fig2.update_layout(title=f'Tangent line to f(w) at w = {round(w0, 2)}<br>Slope of tangent line: {round(df(w0), 5)}', 
                       xaxis_title=r'$w$', 
                       yaxis_title=r'$f(w) = 5w^4 - w^3 - 5w^2 + 2w - 9$', 
                       showlegend=False)
    return fig2.update_layout(width=800, height=500)

def minimizing_animation(w0, alpha):

    play_button = {'label': '▶️ Start animation', 'method': 'animate', 'args': [None]}

    stop_button = dict(label='⏯️ Stop animation', method='animate', visible = True,
                args=[(), {'frame': {'duration': 0, 'redraw': False}, 'mode': 'next', 'fromcurrent': True}])

    w = w0
    ws = []
    dfws = []
    for i in range(50):
        ws.append(w)
        dfws.append(df(w))
        w = w - alpha * df(w)

    fig = draw_f()
        
    grad_anim = go.Figure(
        data=[fig.data[0], go.Scatter(x=[ws[0]], y=[f(ws[0])], marker={'size': 20}, showlegend=False)],
        frames=[
            go.Frame(data=[fig.data[0], go.Scatter(x=[ws[i]], y=[f(ws[i])], marker={'size': 20}, showlegend=False)])
            for i in range(50)
        ],
        layout=go.Layout(updatemenus=[dict(
            type="buttons",
            buttons=[play_button, stop_button])],
             title=f'Gradient Descent<br>Initial Guess = {w0}&nbsp;&nbsp;&nbsp;&nbsp;Step Size = {alpha}'))
    

    grad_anim.update_layout(width=1000, height=700)
    
    return grad_anim

def convexity_visual(a, b, t):
    ws = np.linspace(-20, 20, 1000)

    f = lambda x: x**3 - 3*x**2 + 4*x - 1

    fig = px.line(x=ws, y=f(ws)).update_traces(line=dict(width=8))
    fig.update_layout(xaxis_title='$w$', 
                      yaxis_title='$f(w)$', 
                      width=800, height=600)

    fig.add_trace(go.Scatter(x=[a, b], y=[f(a), f(b)])).update_traces(line=dict(width=8))
    fig.add_trace(go.Scatter(x=[(1-t) * a + t * b], y=[f((1-t) * a + t * b)], mode='markers')).update_traces(marker=dict(size=25))
    fig.add_trace(go.Scatter(x=[(1-t) * a + t * b], y=[(1-t) * f(a) + t * f(b)], mode='markers')).update_traces(marker=dict(size=25))
    fig.update_layout(showlegend=False, title=f't={t}')
    return fig

def make_scatter(df):

    fig = px.scatter(df,
               x='departure_hour',
               y='minutes',
               size=np.ones(len(df)) * 50,
               size_max=8)
    fig.update_xaxes(title='Home Departure Time (AM)')
    fig.update_yaxes(title='Minutes')
    fig.update_layout(title='Commuting Time vs. Home Departure Time')
    fig.update_layout(width=700)
    
    return fig


import numpy as np
import plotly.graph_objects as go

def make_3D_surface():
    # Define a function with multiple local maxima and minima
    def f(x1, x2):
        return 3 * np.sin(2*x1) * np.cos(2*x2) + x1**2 + x2**2

    def dfx1(x1, x2):
        return 6 * np.cos(2 * x1) * np.cos(2 * x2) + 2 * x1

    def dfx2(x1, x2):
        return -6 * np.sin(2 * x1) * np.sin(2 * x2) + 2 * x2

    # Create a grid of x1 and x2 values
    lim = 2
    x1_range = np.linspace(-lim, lim, 100)
    x2_range = np.linspace(-lim, lim, 100)
    x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
    
    # Calculate the function values for each point in the grid
    z_values = f(x1_grid, x2_grid)

    # Create the 3D surface plot
    fig = go.Figure(data=[
        go.Surface(
            x=x1_grid,
            y=x2_grid,
            z=z_values,
            colorscale='RdBu_r',
            contours=dict(
                z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project=dict(z=True))
            )
        )
    ])

    # Add coordinate axes
    fig.add_trace(go.Scatter3d(x=[-2, 2], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='gray', width=2), showlegend=False))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[-2, 2], z=[0, 0], mode='lines', line=dict(color='gray', width=2), showlegend=False))

    # Update the layout
    fig.update_layout(
        title='$$f(w_1, w_2) = 3  \sin(2 w_1) \cos(2 w_2) + w_1^2 + w_2^2$$',
        scene=dict(
            xaxis_title='w1',
            yaxis_title='w2',
            zaxis_title='f(w1, w2)',
            aspectratio=dict(x=1, y=1, z=1),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1))
        ),
        width=800,
        height=700,
        margin=dict(l=65, r=50, b=65, t=90),
    )

    return fig


def make_3D_contour(with_gradient=False, w1_start=-0.5, w2_start=1, neg=False):
    import numpy as np
    import plotly.graph_objects as go
    
    # Define a function with multiple local maxima and minima
    def f(x1, x2):
        # This combines sine waves with a quadratic component
        return 3 * np.sin(2*x1) * np.cos(2*x2) + x1**2 + x2**2

    def dfx1(x1, x2):
        return 6 * np.cos(2 * x1) * np.cos(2 * x2) + 2 * x1

    def dfx2(x1, x2):
        return -6 * np.sin(2 * x1) * np.sin(2 * x2) + 2 * x2

    # Create a grid of x1 and x2 values
    lim = 2
    x1_range = np.linspace(-lim, lim, 100)
    x2_range = np.linspace(-lim, lim, 100)
    x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

    # Calculate the function values for each point in the grid
    z_values = f(x1_grid, x2_grid)

    # Create the contour plot - note the different parameter structure for go.Contour
    fig = go.Figure(data=[
        go.Contour(
            z=z_values,          # For contour plots, z is the height data matrix
            x=x1_range,          # x-coordinates (not the grid)
            y=x2_range,          # y-coordinates (not the grid)
            colorscale='RdBu_r',
            contours=dict(
                showlabels=True,  # Show contour labels
                labelfont=dict(size=12, color='white')
            )
        )
    ])

    # Add gradient vector if requested
    if with_gradient:
        grad_pt = w1_start, w2_start
        a = 0.1
        grad_x, grad_y = dfx1(*grad_pt), dfx2(*grad_pt)
        w1_start, w2_start = grad_pt
        if neg:
            w1_end, w2_end = w1_start - grad_x * a, w2_start - grad_y * a
        else:
            w1_end, w2_end = w1_start + grad_x * a, w2_start + grad_y * a
        
        # Add gradient line
        fig.add_trace(go.Scatter(
            x=[w1_start, w1_end], y=[w2_start, w2_end],
            mode='lines+markers',
            line=dict(color='red' if neg else 'gold', width=5),
            # marker=dict(size=4, color='gold'),
        ))

        # Add arrowhead
        alph = 0.01
        if neg:
            ax = w1_start - grad_x * alph
            ay = w2_start - grad_y * alph
        else:
            ax = w1_start + grad_x * alph
            ay = w2_start + grad_y * alph

        fig.add_annotation(
            x=w1_end, y=w2_end,
            ax=ax, ay=ay,
            xref='x', yref='y', axref='x', ayref='y',
            showarrow=True, arrowhead=3, arrowsize=1.5,
            arrowwidth=3, arrowcolor='red' if neg else 'gold'
        )

    if with_gradient:
        col = 'red' if neg else 'gold'
        text = 'Negative of the Gradient Vector' if neg else 'Gradient Vector'
        title=f'<span style="color:{col}"><b>{text}</b></span> at Point ({w1_start}, {w2_start})'
    else:
        title = '$$f(w_1, w_2) = 3  \sin(2 w_1) \cos(2 w_2) + w_1^2 + w_2^2$$'

    # Add axis labels
    fig.update_layout(
        title=title,
        xaxis_title='w1',
        yaxis_title='w2',
        width=800,
        height=700,
        margin=dict(l=65, r=50, b=65, t=90),
        showlegend=True
    )

    # Show the plot
    return fig


def show_gd_path_contour(w1_start=-0.5, w2_start=1, step_size=0.1, iterations=10):
    # Define the function and its derivatives
    def f(x1, x2):
        return 3 * np.sin(2*x1) * np.cos(2*x2) + x1**2 + x2**2

    def dfx1(x1, x2):
        return 6 * np.cos(2 * x1) * np.cos(2 * x2) + 2 * x1

    def dfx2(x1, x2):
        return -6 * np.sin(2 * x1) * np.sin(2 * x2) + 2 * x2

    # Create grid for contour plot
    lim = 2
    x1_range = np.linspace(-lim, lim, 100)
    x2_range = np.linspace(-lim, lim, 100)
    x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
    z_values = f(x1_grid, x2_grid)

    # Initialize figure
    fig = go.Figure(data=[
        go.Contour(
            z=z_values, x=x1_range, y=x2_range,
            colorscale='RdBu_r',
            contours=dict(showlabels=True, labelfont=dict(size=12, color='white'))
        )
    ])

    # Perform gradient descent if enabled
    w1, w2 = w1_start, w2_start
    path_x, path_y = [w1], [w2]
    
    for _ in range(iterations):
        grad_x, grad_y = dfx1(w1, w2), dfx2(w1, w2)
        w1, w2 = w1 - step_size * grad_x, w2 - step_size * grad_y
        path_x.append(w1)
        path_y.append(w2)
    
    # Add descent path to the plot
    fig.add_trace(go.Scatter(
        x=path_x, y=path_y, mode='lines+markers',
        line=dict(color='gold', width=3),
        marker=dict(size=8, color='gold')
    ))

    title = f'<b><span style="color:gold">Gradient Descent Path</span></b> from ({w1_start}, {w2_start})'


    # Update layout
    fig.update_layout(
        title=title, xaxis_title='w1', yaxis_title='w2',
        width=800, height=700, margin=dict(l=65, r=50, b=65, t=90)
    )
    
    return fig

def show_gd_path_surface(w1_start=-0.5, w2_start=1, step_size=0.1, iterations=10):
    # Define the function and its derivatives
    def f(x1, x2):
        return 3 * np.sin(2*x1) * np.cos(2*x2) + x1**2 + x2**2

    def dfx1(x1, x2):
        return 6 * np.cos(2 * x1) * np.cos(2 * x2) + 2 * x1

    def dfx2(x1, x2):
        return -6 * np.sin(2 * x1) * np.sin(2 * x2) + 2 * x2

    # Create grid for contour plot
    lim = 2
    x1_range = np.linspace(-lim, lim, 100)
    x2_range = np.linspace(-lim, lim, 100)
    x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
    z_values = f(x1_grid, x2_grid)

    # Initialize figure
    fig = go.Figure(data=[
        go.Surface(
            x=x1_grid,
            y=x2_grid,
            z=z_values,
            colorscale='RdBu_r',
            contours=dict(
                z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project=dict(z=True))
            )
        )
    ])

    # Perform gradient descent if enabled
    w1, w2 = w1_start, w2_start
    path_x, path_y = [w1], [w2]
    path_z = [f(w1, w2)]
    
    for _ in range(iterations):
        grad_x, grad_y = dfx1(w1, w2), dfx2(w1, w2)
        w1, w2 = w1 - step_size * grad_x, w2 - step_size * grad_y
        path_x.append(w1)
        path_y.append(w2)
        path_z.append(f(w1, w2))
    
    # Add descent path to the plot
    fig.add_trace(go.Scatter3d(
        x=path_x, y=path_y, z=path_z, mode='lines+markers',
        line=dict(color='gold', width=2),
        marker=dict(size=8, color='gold')
    ))

    title = f'<b>Gradient Descent Path</b> from ({w1_start}, {w2_start})'


    # Update layout
    fig.update_layout(
        # title='$$f(w_1, w_2) = 3  \sin(2 w_1) \cos(2 w_2) + w_1^2 + w_2^2$$',
        scene=dict(
            xaxis_title='w1',
            yaxis_title='w2',
            zaxis_title='f(w1, w2)',
            aspectratio=dict(x=1, y=1, z=1),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1))
        ),
        width=800,
        height=700,
        margin=dict(l=65, r=50, b=65, t=90),
    )
    
    return fig


from plotly.subplots import make_subplots

def display_paths(w1_start=-0.5, w2_start=1, step_size=0.1, iterations=10):
    # Call the functions that return Plotly figures
    fig1 = show_gd_path_contour(w1_start, w2_start, step_size, iterations)
    fig2 = show_gd_path_surface(w1_start, w2_start, step_size, iterations)
    
    # Extract traces and titles
    traces1 = fig1.data
    traces2 = fig2.data
    title1 = fig1.layout.title.text if fig1.layout.title.text else "Plot 1"
    title2 = fig2.layout.title.text if fig2.layout.title.text else "Plot 2"
    
    # Create a subplot figure
    fig = make_subplots(rows=1, cols=2, specs=[
        [{"type": "contour"}, {"type": "surface"}]
    ], shared_xaxes=True, shared_yaxes=True)
    
    # Add traces to the new figure
    for trace in traces1:
        fig.add_trace(trace, row=1, col=1)
    for trace in traces2:
        fig.add_trace(trace, row=1, col=2)
    
    # Update layout
    fig.update_layout(title_text=title1, width=1600, height=700, scene=dict(
            xaxis_title='w1',
            yaxis_title='w2',
            zaxis_title='f(w1, w2)',
            aspectratio=dict(x=1, y=1, z=1),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1))
        ),
        showlegend=False)
    
    # Show the figure
    fig.show()