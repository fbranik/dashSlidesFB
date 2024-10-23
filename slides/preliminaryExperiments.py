# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Preliminary Experiments'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

introExp = [
        "Before moving on to the construction of the data-set, a series of experiments and analyses, focusing on different"
        " aspects of the data generator application, was conducted."]

experiments = html.Dl([
        html.Dt(["Statistical Analysis"]),
        html.Dd(["- The distribution of the communication times reported by all processes is looked into."]),
        html.Dt(["Message Size Scale Analysis"]),
        html.Dd(["- The behaviour of communication is examined for large and small messages."]),
        html.Dt(["Constant Message Size Scenario"]),
        html.Dd(["- Some cases were the message size does not change with the working set size are analyzed."]),
        html.Dt(["Communication-Computation Interference"]), html.Dd([
                                                                             "- Possible interference is explored by imposing different barriers between the two phases of execution."]),
])
text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [

                                                dbc.CardBody(
                                                        [
                                                                html.P(introExp),
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
text2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Analyses and Scenarios",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                experiments,
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
        text2,

]
