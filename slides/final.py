# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600

import dash_mantine_components as dmc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from fs.filesize import binary as binarySize
import pandas as pd

from custom_utilities.custom_functions import create_table

tradeoffFig = html.P("Thank you for your time and attention.")
q = html.P("Questions?")
modelResults = dbc.Row(
        children=[

                dbc.Row([

                        dbc.Col([tradeoffFig],
                                style={"padding"    : "20px", "textAlign": "center", "display": "flex",
                                       "align-items": "center", "justify-content": "center", "font-size": "50px"}),
                ]),
                dbc.Row([

                        dbc.Col([q],
                                style={"padding"    : "20px", "textAlign": "center", "display": "flex",
                                       "align-items": "center", "justify-content": "center", "font-size": "50px"}),
                ]),
        ])

title = ''
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={
        "background": "slategray"})

content = [
        titleBar,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        html.Br(),
        modelResults

]
