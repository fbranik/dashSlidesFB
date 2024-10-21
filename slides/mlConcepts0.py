# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Machine Learning Concepts and Definitions"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

decisionTrees = [html.P("- They find correlation between the features by making subsets of the dataset based on feature values."),
                 html.P("- Prone to overfitting when each subset represents small number of points")]
ensembleMethods = [html.P("- They use multiple 'weak' learners to construct more accurate models.")]

dataSplit = (" The available dataset is randomized and split in two subsets, "
             "one to be used in training and one for testing.")

def2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Train/Test Data Split",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(dataSplit,
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
def3 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Decision Trees",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(decisionTrees,
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

def4 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Ensemble Methods",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(ensembleMethods,
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
hyperparameterTuning = ("Various values "
                        "for the parameters of the structure of a model are tested, to find "
                        "an optimal configuration.")


def5 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Hyperparameter Tuning",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(hyperparameterTuning,
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
content = [
        titleBar,
        html.Br(),
        html.Br(),
        def2,
        # def5,
        # def3,
        # def4,
        #

]
