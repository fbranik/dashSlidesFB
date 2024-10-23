# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Random Forests and Gradient Boosting"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

figureRF = [html.Img(src="assets/treesAndForests.png", width="100%")]
figureGB = [html.Img(src="assets/gradientBoosting.png", width="100%")]

plot1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(figureRF),
                                # dbc.Col(html.P("Random Forest"), style={"textAlign"      : "center", "display": "flex",
                                #                                         "align-items"    : "center",
                                #                                         "justify-content": "center"})
                        ], style={"padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)

content = [
        titleBar,
        html.Br(),
        plot1,
]
