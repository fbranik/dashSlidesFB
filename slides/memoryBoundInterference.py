# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Communication-Computation Interference 2"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = [
        "As mentioned, performance for smaller messages is more susceptible to changes. This can also be seen in these cases"
        ", where imposing barriers in beneficial for smaller messages but has almost no effect for large message cases."]
# plots = [html.Br(), html.Embed(src="assets/dataGeneratorCommPattern.pdf#toolbar=0&navpanes=0&scrollbar=0",
#                                    height="100%", width="100%")]

figure = [html.Br(), html.Img(src="assets/MemoryBound_64Barriers.png", width="70%")]

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
                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)
content = [
        titleBar,
        plotAndComments,
]
