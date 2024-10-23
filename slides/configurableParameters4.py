# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Configurable Parameters"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})
comment1 = "Data Generator Application Parameters: "
configurableParameters = html.Ul([
        html.Li(["Working Set Size (per process)", html.Br(),
                 html.P("- grows with the Number of total Processes to follow Weak Scaling")]),
        html.Li(["Number of Computing Operations (per element)", html.Br(),
                 html.P([" - viewed as", html.B(" Computation Load Type"),
                         " where: 1 op. = Memory Bound, X ops. = Compute Bound X"])]),
        html.Li(["Message Size", html.Br(),
                 html.P("- equal to a multiple of the square root of the Working Set Size")]),
        html.Li("Number of Messages"), html.Br(),
])

comment2 = "Execution environment Parameters"
environmentParameters = html.Ul([
        html.Li("Number of Computing Nodes"), html.Br(),
        html.Li("Number of Processes per Node"), html.Br(),
])

comment3 = "In modeling configurable parameters/independent variables are called features."

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment1), configurableParameters,
                                                                html.P(comment2), environmentParameters,
                                                                html.Br(), html.P(comment3, style={"font-size": "30px"})
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
        text1,

]
