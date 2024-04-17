# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Communication-Computation Interference 1"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})
comment1 = "To examine interference between the two phases of execution, a small addition was made:"
comment2 = ("Barriers, are a synchronization tool that force a subset of processes to wait until all "
            " processes in this subset have reached the barrier."
            )
comment3 = ["By changing the number of computing operations per element we can create different computational loads."
            "  As the number of operations grows, the loads progress from being Memory Bound to being Compute Bound.  "
            "This is because more operations force each datum to spend more time in the processor and not in the memory "
            "bus during its transfer."]
simplifiedCode = html.Pre([""" for time:
     communication(NumberOfMessages, MessageSize)
     
     MPI_Waitall(MessagesToSend,MessagesToRecv)
     
     MPI_Barrier(custom_communicator); // synchronize a set of processes
     
     computation(WorkingSetSize, NumberOfExtraOperations)"""], style={"font-size": "18px"})

barriers = html.Ul([
        html.Li(["The ", html.B("Global Barrier "), "forces synchronization across all processes."]),
        html.Li(["The ", html.B("Socket Barrier "), "forces synchronization across all processes that reside on the same processor."]), ]
)
loads = html.Ul([
        html.Li(["We call ", html.B("Memory Bound "), "a computation load with one operation per element"]),
        html.Li(["We call ", html.B("Compute Bound X "), "a computation load with X operations per element"]),
])
barriersPro = html.P("+ They can be helpful in efficient shared resources usage.", style={"color": "seagreen"})
barriersCon = html.P("- They may cause unnecessary delays. ", style={"color": "firebrick"})

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Barriers",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment1,
                                                                       className="card-text"), simplifiedCode,
                                                                html.P(comment2), barriers, barriersPro, barriersCon
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
                                                dbc.CardHeader("Computational Loads",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment3,
                                                                       className="card-text"), loads
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
        text1,
        text2

]
