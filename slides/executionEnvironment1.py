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

arisComment = ["Example of 2 Aris Nodes using the ", html.I("map-by node"), " option:"]

highlightComment = html.Ul([
        html.Li(html.B("Number of Computing Nodes"),
                style={"color": "#6083FE"}),
        html.Li(html.B("Processes per Node"),
                style={"color": "peru"}), html.Br(),

])
arisFigure = [html.Br(), html.Img(src="assets/arisNodeOrderHighlight.png", width="100%")]

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
text2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(highlightComment,
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
        text2

]
