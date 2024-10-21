# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Preliminary Experiments Insights"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

insightsGained = [
        html.Ul([
                html.Li(["The mean can be used as a representative value.  ", html.Br(),"(Statistical Analysis)"]),  html.Br(),
                html.Li(["For smaller messages the number of messages is not relevant.  ", html.Br(),"(Message Size Scale Analysis)"]),    html.Br(),
                html.Li(["Communication and Computation resource contention, can translate into significant change of performance.  ", html.Br(),"(Constant Message Size Scenario)"]), html.Br(),
                html.Li(["This interference is likely to happen for smaller communication or memory intensive computation.  ", html.Br(),"(Communication-Computation Interference)"]), html.Br(),
                html.Li(["Focused, local barriers, may be beneficial to performance under these conditions.  ", html.Br(),"(Communication-Computation Interference)"]), html.Br(),
                # html.Li(
                #     "As the working set size grows (and thus computation time), so does communication time, even in some cases "
                #     " where communication remains constant."),

        ]),
        # html.P("The above may in part be caused by the fact that we "
        #        " have unsynchronized processes with two phases of execution.  "
        #        "These conditions create a time drift that affects the waiting time for each process' "
        #        "communication requests.")
]
comment1 = []

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Insights Gained",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        insightsGained, className="card-text",
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
        text1

]
