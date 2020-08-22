import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sys

import pandas as pd
import plotly.graph_objs as go
from plotly import tools
import os

from math import sqrt

DATA_DIR = './base_data'
file_path = os.path.join(DATA_DIR, 'train.csv')
train_df = pd.read_csv(file_path)

numerical_columns = list(train_df.select_dtypes(exclude = 'object').columns)

overview_component = html.Div(
    children=[
        html.H2(
            children = "Number of Rows :{}".format(train_df.shape[0])
        ),
        html.H2(
            children = "Number of Features :{}".format(train_df.shape[1])
        ),
        html.H2(
            children = "Number of Numerical Features :{}".format(len(numerical_columns))
        ),

        html.H2(
            children = "Target : {}".format("logerror")
        )
    ])
