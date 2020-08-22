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

def missing_figure():
    missing_values = train_df.isnull().sum().reset_index()
    missing_values.rename(columns = {'index': "features", 0: 'counts' }, inplace = True)
    missing_values['percentage'] =(missing_values["counts"]/train_df.shape[0])*100

    trace = go.Bar(
    y    =  list(missing_values.counts.values),
    x    =  list(missing_values.features.values),
    text = list(missing_values.percentage.values),
    marker = dict(color='red'),
    opacity=0.8
    )

    layout=go.Layout(
        title='Missing Values',
        titlefont=dict(family="Courier New, monospace", size=30, color="black"),
        xaxis=dict(
            title='Features',
            ticks='',
            tickangle = 90,
            tickfont=dict(family='Rockwell', color='black', size=14),
            title_font=dict(size=18, family='Rockwell', color='green')
            ),
        yaxis=dict(
            title='Value',
            ticks='', 
            linewidth=2,
            linecolor='grey', 
            tickangle= 90, 
            tickfont=dict(family='Rockwell', color='black', size=14),
            title_font=dict(size=18, family='Rockwell', color='green')
            ),
        margin=dict(pad=5),
    )
    fig=go.Figure(data=[trace],layout=layout)
    return fig

missing_value_component = html.Div(
        children= [
                dcc.Graph(id='missing_values', figure = missing_figure()) 
        ]
    )
