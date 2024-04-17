# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Semi-Empirical Model 1'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = ["The Intel MPI Benchmark was used as a base for a simple semi-empirical model: "]
figure = [html.Img(src="assets/exchangePattern.png", width="55%")]
expression = html.Img(src="assets/semiEmpiricalExpression.png", width="70%")
comment2 = [html.P("By observing the data from this benchmark's execution, the expression the following"
            " expression was deducted:"), html.Br(),
            html.P(expression, style={"margin-left":"230px"}), html.Br(),
            html.P("The reason that this model only has 2 independent variables, is that those are"
                   " the only ones configurable in the context of the chosen benchmark."),
            html.P("The base case, is an execution of the benchmark for 1 process per node on 64 nodes"
                   " and for a message size of 4 KiB.")]

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment1,
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
plot1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(figure),
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
                                                            comment2
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
        text1,
        plot1,
        html.Br(),
        text2,

]
