# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Data Gathering and Filtering'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = ["Before beginning training the models, the following filter was applied:"]
figureHist = [html.Img(src="assets/featureHistogram.png", width="50%")]
dataFilter = html.Img(src="assets/dataFilter.png", width="25%")
comment2 = ["This was done to reduce the noise non-practical cases introduce."]
text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Data Filtering",
                                                               style={"background": "slategray",
                                                                      "color"     : "white"}),
                                                dbc.CardBody(
                                                        [

                                                                html.P(comment1,
                                                                       className="card-text"), html.Div(dataFilter,
                                                                                                        style={
                                                                                                                "textAlign"      : "center",
                                                                                                                "display"        : "flex",
                                                                                                                "align-items"    : "center",
                                                                                                                "justify-content": "center"}),
                                                                html.Br(), html.P(comment2,
                                                                       className="card-text")
                                                        ]
                                                ),
                                        ],
                                        className="mb-3", style={"color": "black", "background": "ghostwhite"},
                                        outline=True
                                ))),

                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)
comment0 = "To construct the data-set, the feature space was swept for the following values:"
featureSpace = html.Ul([
        html.Li("Working Set Size (per process) = [2MiB, 8MiB, 32MiB, 128MiB, 256MiB, 512MiB]"),
        html.Br(), html.Li("Computational Load Type = ['Memory Bound', 'Compute Bound']"),
        html.Br(), html.Li(["Message Size = [1, 5, 10, 50, 100] * ", html.Img(src="assets/sqrtWSSize.svg", width="18%")]),
        html.Br(), html.Li("Number of Messages = [2, 4, 8]"),
        html.Br(), html.Li("Number of Computing Nodes = [4, 8, 16, 32, 64]"),
        html.Br(), html.Li("Processes per Node = [2, 4, 8, 16, 20]")
])
text2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Feature Space Sweep",
                                                               style={"background": "slategray",
                                                                      "color"     : "white"}),
                                                dbc.CardBody(
                                                        [

                                                                html.P(comment0,
                                                                       className="card-text"), featureSpace
                                                        ]
                                                ),
                                        ],
                                        className="mb-3", style={"color": "black", "background": "ghostwhite"},
                                        outline=True
                                ))),

                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)

content = [
        titleBar,
        html.Br(),
        text2,
        text1,
]
