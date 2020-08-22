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


from math import sqrt

DATA_DIR = './base_data'
file_path = os.path.join(DATA_DIR, 'train.csv')
train_df = pd.read_csv(file_path)

categorical_columns = train_df.select_dtypes(include = 'object').columns
categorical_df = train_df[categorical_columns]


categorical_component= html.Div(
    style={'margin-top': "100px", "font_size": "20px", "font_family": "Courier New, monospace" },
    children=[
        html.P(
            children = "Categorical Features",
            style = {'text-align': "center", "font-family": "Courier New, monospace", "font-size": '30px'},
        ),

        html.Div(
            style = {'display': 'flex'},
            children= [
                dcc.Dropdown(
                options=[
                    {'label': col, 'value': col} for  col in list(categorical_columns)
                ],
                style={'width': "200px", "border": "1px solid grey"},
                id = 'categorical_features',
                placeholder = "Select Feature"
            ),
            dcc.Dropdown(
                options=[
                    {'label': col, 'value': col} for  col in ['year', 'month', 'dayofweek']
                ],
                style={'width': "200px", "border": "1px solid grey"},
                id = 'timeline1',
                placeholder = 'Select Resolution'
            )]
            ),

        dcc.Graph(id='graph1')
    ])

def get_categorical_figure(Feature, resolution):
    if not Feature or not resolution :
        return go.Figure()
        # Feature = categorical_columns[0]
        # resolution = 'year'
    Feature = str(Feature)
    labels_to_consider = train_df[Feature].value_counts().head(12).index
    feature_data = train_df[train_df[Feature].isin(labels_to_consider)] 
    data = []
    for frequency in list(feature_data[resolution].unique()):
        feature_data_day = feature_data[feature_data[resolution] == frequency ]
        trace = go.Bar(
            x=feature_data_day[Feature].value_counts().to_dense().keys(),
            y=feature_data_day[Feature].value_counts(),
            text=feature_data_day[Feature].value_counts(),
            textposition='auto',
            name = "{}-{}".format(resolution,frequency)
        )
        data.append(trace)

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
    fig=go.Figure(data=data,layout=layout)

    return fig
