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

header_component = html.H1(
        children='Data Profiling',
        style=Styles
    )