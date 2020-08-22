import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sys

import pandas as pd
import plotly.graph_objs as go
from plotly import tools

from .styles import Styles

from math import sqrt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': 'white',
    'text': '#7FDBFF'
}

graph_component = html.Div(
        style=Styles,
        children= [
                dcc.Graph(id='graph_profile' ) 
        ]
    )
