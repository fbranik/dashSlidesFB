# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Feature Review'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = ["Gives a first image, but more details are needed."]

# plots = [html.Br(), html.Embed(src="assets/dataGeneratorCommPattern.pdf#toolbar=0&navpanes=0&scrollbar=0",
#                                    height="100%", width="100%")]

boxPlotFigure = [html.Br(), html.Img(src="assets/arisNodesOverviewFeatures.png", width="100%")]

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
                                dbc.Col(boxPlotFigure),
                        ], style={"margin-left": "98px", "padding-right": "50px", "width": "90%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)

content = [
        titleBar,
        html.Br(),
        plot1,
        # text1


]
