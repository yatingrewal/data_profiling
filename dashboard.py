from _plotly_future_ import v4_subplots 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sys

import pandas as pd
import plotly.graph_objs as go
from plotly import tools

from components.header.layout import header_component
from math import sqrt
import os
from components.views import * 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': 'black',
    'text': '#7FDBFF'
}

app = dash.Dash()
app.config['suppress_callback_exceptions']=True

app.layout = html.Div(
    children=[
        header_component,
        overview_component,
        missing_value_component,
        categorical_component,
        numerical_component
    ])

@app.callback(
    dash.dependencies.Output('graph1', 'figure'),
    [dash.dependencies.Input('categorical_features', 'value'),
     dash.dependencies.Input('timeline1', 'value')])
def update_graph(feature, resolution):
    return get_categorical_figure(feature, resolution)

@app.callback(
    dash.dependencies.Output('graph2', 'figure'),
    [dash.dependencies.Input('numerical_features', 'value'),
     dash.dependencies.Input('timeline2', 'value')])
def update_graph(feature, resolution):
    return get_numerical_figure(feature, resolution)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0' ,debug=True, port = 80)