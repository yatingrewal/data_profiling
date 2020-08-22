from plotly.subplots import make_subplots 

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sys

import pandas as pd
import plotly.graph_objs as go
from plotly import tools
import os

import plotly.figure_factory as ff

from math import sqrt

DATA_DIR = './base_data'
file_path = os.path.join(DATA_DIR, 'train.csv')
train_df = pd.read_csv(file_path)

numerical_columns = list(train_df.select_dtypes(exclude = 'object').columns)
numerical_component= html.Div(
    style={'margin-top': "100px", "font_size": "20px", "font_family": "Courier New, monospace" },
    children=[
        html.P(
            children = "Numerical Features",
            style = {'text-align': "center", "font-family": "Courier New, monospace", "font-size": '30px'},
        ),

        html.Div(
            style = {'display': 'flex'},
            children= [
                dcc.Dropdown(
                options=[
                    {'label': col, 'value': col} for  col in list(numerical_columns)
                ],
                style={'width': "200px", "border": "1px solid grey"},
                id = 'numerical_features',
                placeholder = "Select Feature"
            ),
            dcc.Dropdown(
                options=[
                    {'label': col, 'value': col} for  col in ['year', 'month', 'dayofweek']
                ],
                style={'width': "200px", "border": "1px solid grey"},
                id = 'timeline2',
                placeholder = 'Select Resolution'
            )]
            ),

        dcc.Graph(id='graph2')
    ])

def get_numerical_figure(Feature, resolution):
    if not Feature or not resolution :
        return go.Figure()

    fig = make_subplots(rows=1, cols=2, subplot_titles=("Distribution", "Relation with Target"))
    Feature = str(Feature)
    data = []
    for frequency in list(train_df[resolution].unique()):
        feature_data_day = train_df[train_df[resolution] == frequency ]
        trace = go.Histogram(
            x= list(feature_data_day[Feature].value_counts()),
            name = "{}-{}".format(resolution,frequency),
            nbinsx=30
        )
        fig.add_trace(trace, row =1, col= 1)

    trace_scatter = go.Scatter(
        x= list(train_df.head(1000)[Feature].values),
        y= list(train_df.head(1000).logerror.values),
        mode='markers',
        name = '{} vs {}'.format(Feature, "logerror")
    )
   
    fig.append_trace(trace_scatter, 1, 2) 

    layout=go.Layout(
        height = 600,
        xaxis=dict(
            title='Labels',
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

    # Update xaxis properties
    fig.update_xaxes(title_text="Value", row=1, col=1)
    fig.update_xaxes(title_text= Feature, row=1, col=2)

    # Update yaxis properties
    fig.update_yaxes(title_text="Count", row=1, col=1)
    fig.update_xaxes(title_text="logerror", row=1, col=2)

    fig.layout.update(barmode='overlay')

    return fig