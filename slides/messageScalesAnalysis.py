# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Message Size Scale Analysis'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = [
        html.P(["- Small Message Sizes ( = [1, 5, 10] * ", html.Img(src="assets/sqrtWSSize.svg", width="31%")," )"]),
            html.P(["These cases are similar across all the the tested number of messages.  "
                     "This may allude to the fact that for smaller data sizes, the system can parallelize "
                     "communication and yields a similar performance for different small message sizes."
                    "  The amount of parallelization happening, varies across processes, thus the "
                    "relatively high standard deviation."],
                   style={"margin-left":"15px"}),
        html.Br(),
        html.P(["- Large Message Sizes ( = [50, 100] * ", html.Img(src="assets/sqrtWSSize.svg", width="31%")," )"]),
            html.P(["The impact of changes in both of the communication parameters, is substantia.  "
                            "This happens because processes cannot parallelize heavy communicational loads."
                            "  The lower standard deviation, also supports this."],
                   style={"margin-left":"15px"}),
]
# plots = [html.Br(), html.Embed(src="assets/dataGeneratorCommPattern.pdf#toolbar=0&navpanes=0&scrollbar=0",
#                                    height="100%", width="100%")]
figure = [html.Br(), html.Img(src="assets/64_20_VarComm_Plot.png", width="100%")]

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

plotAndComments = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(figure),
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
                                )), style={"textAlign"  : "justify", "display": "flex",
                                           "align-items": "center", "justify-content": "left"}),
                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)
content = [
        titleBar,
        plotAndComments
]
