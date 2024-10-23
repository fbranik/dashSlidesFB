# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Target Systems and Applications'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

computerClustersT = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [

                                                dbc.CardBody(
                                                        [
                                                                html.P("Computer Clusters",
                                                                       className="card-text"),
                                                        ]
                                                ),
                                        ],
                                        className="mb-3", style={"background": "slategray", "color": "white"},
                                        outline=True,
                                ))),

                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)
computerClusters = html.Div(
        [

                dbc.Row(dbc.Col(html.Div(html.Img(src="assets/computerCluster.png", width="50%"))))
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)

messagePassingT = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [

                                                dbc.CardBody(
                                                        [
                                                                html.P("Message Passing",
                                                                       className="card-text"),
                                                        ]
                                                ),
                                        ],
                                        className="mb-3", style={"background": "slategray", "color": "white"},
                                        outline=True,
                                ))),

                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)
messagePassing = html.Div(
        [
                dbc.Row(dbc.Col(html.Div(html.Img(src="assets/messagePassing.png", width="50%"))))
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)

content = [
        titleBar,
        html.Br(),
        html.Br(),
        computerClustersT,
        computerClusters,
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Col([messagePassingT, html.Br(),
                          messagePassing]), dbc.Col()])

]
