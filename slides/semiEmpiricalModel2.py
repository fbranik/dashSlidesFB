# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Semi-Empirical Model 2'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = [""]
figurePred = [html.Img(src="assets/mpiExchangeMsgSizePrediction.png", width="70%")]
figureError = [html.Img(src="assets/mpiExchangePredError.png", width="70%")]
comment2 = ["These plots, sum up the model's performance on the Exchange benchmark data."
            "  The percentage error reaches acceptable levels (±15%).  "
            "However, when trying to predict cases of our data generator application, this model yields percentage errors"
            " in the area of 100%.  This happens, despite the similarity in the communication patterns of"
            " the two applications, and one reason for it, is the lack of computation in the Exchange benchmark.  "
            "This is a live example of the modeling tradeoff that was mentioned."]
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
                        ], style={"margin-left": "188px", "margin-top": "10px", "padding-right": "50px", "width": "75%"}
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
text2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment2,
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

content = [
        titleBar,
        plot1,
        html.Br(),
        plot2, html.Br(),text2
]
