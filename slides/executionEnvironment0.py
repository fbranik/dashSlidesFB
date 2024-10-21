# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Execution Environment'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

arisComment = ["Example of 2 Aris Nodes using the ", html.I("map-by node")," option:"]

# arisFigure = [html.Br(), html.Embed(src="assets/dataGeneratorCommPattern.pdf#toolbar=0&navpanes=0&scrollbar=0",
#                                    height="100%", width="100%")]

arisFigure = [html.Br(), html.Img(src="assets/arisNodeOrder.png", width="100%")]

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(arisComment,
                                                                       className="card-text"),
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
arisFigure = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(arisFigure),
                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)

content = [
        titleBar,
        html.Br(),
        html.Br(),
        text1,
        arisFigure,
        html.Br(),
]
