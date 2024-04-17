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

figureRF = [html.Img(src="assets/randomForest.png", width="100%")]
figureGB = [html.Img(src="assets/gradientBoosting.png", width="100%")]
comment = ["Due to a consistently better performance, a tuned version of the Gradient Boosting model was chosen. "
           " However, the comparison with the relatively simpler Random Forest model, is another example of the modeling"
           "tradeoff that has been mentioned."]
plot1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(figureRF),
                                dbc.Col(html.P("Random Forest"), style={"textAlign"      : "center", "display": "flex",
                                                                        "align-items"    : "center",
                                                                        "justify-content": "center"})
                        ], style={"padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)
plot2 = html.Div(
        [
                dbc.Row(
                        [

                                dbc.Col(html.P("Gradient Boosting"), style={"textAlign"      : "center",
                                                                            "display"        : "flex",
                                                                            "align-items"    : "center",
                                                                            "justify-content": "center"}),
                                dbc.Col(figureGB),

                        ], style={"padding-right": "50px", "width": "100%"}
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
                                                                html.P(comment,
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
        html.Br(),
        plot1,
        html.Hr(),
        plot2,
        html.Br(),
        text2
]
