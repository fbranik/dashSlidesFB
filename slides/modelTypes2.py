# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Basic Modeling Concepts'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

analyticalModels = ("They have closed form solutions and rely on formal methodologies"
                    " to represent the behaviour of parallel applications. Based in mathematics and theory.")

semiEmpiricalModels = ("The meeting point of theory and observation. "
                       " They combine data from the execution of a benchmark/data generator program with a theoretical framework.  ")

empiricalModelsML = ("Models that prioritize data over theory. They use a dataset constructed from the execution of"
                     " a data generator program, for a range of values of selected features/independent variables.  "
                     "Machine learning algorithms are leveraged to identify patterns, correlations, and predictive"
                     " factors within the data.")


def2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Analytical Models",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(analyticalModels,
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
                                                dbc.CardHeader("Semi-Empirical Models",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(semiEmpiricalModels,
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
                                                dbc.CardHeader("Empirical Models - Machine Learning",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(empiricalModelsML,
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
tradeoff = ("When designing and reviewing models, one can observe a pattern when it comes to how complex a model is,"
            " how well it performs and how many different cases it may cover.  More complex models often "
            "give great performance for specific scenarios and can be more difficult to interpret."
            "  Simpler models may be more intuitive, at the cost of performance.")


def1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Complexity/Performance/Range Tradeoff",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(tradeoff,
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
        def3,
        def4,


]
