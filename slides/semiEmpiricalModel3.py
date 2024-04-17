# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Semi-Empirical Model 3'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = ["The following, sum up the model's performance on the Exchange benchmark data."]
figurePred = [html.Img(src="assets/mpiExchangeMsgSizePrediction.png", width="60%")]
figureError = [html.Img(src="assets/mpiExchangePredError.png", width="60%")]

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment1,
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
plot1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(figurePred),
                        ], style={"margin-left": "188px", "padding-right": "50px", "width": "75%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)
plot2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(figureError),
                        ], style={"margin-left": "188px", "padding-right": "50px", "width": "75%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)


content = [
        titleBar,
        html.Br(),
        text1,
        plot1,
        html.Br(),
        plot2
]
