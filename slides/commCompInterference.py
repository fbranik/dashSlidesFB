# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Communication/Computation Interference"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})
comment1 = "To examine interference between the two phases of execution, a small addition was made:"
comment2 = ("Barriers, are a synchronization tool that force a subset of processes to wait until all "
            " processes in this subset have reached the barrier."
            )

simplifiedCode = html.Pre(["""
 for time:
     communication(NumberOfMessages, MessageSize)
     
     MPI_Waitall(MessagesToSend,MessagesToRecv)
     
     MPI_Barrier(custom_communicator); // synchronize a set of processes
     
     computation(WorkingSetSize, NumberOfExtraOperations)"""], style={"font-size": "18px"})

barriers = html.Dl([
html.Dt(["Global Barrier"]),
        html.Dd(["- It forces synchronization across all processes."]),
        html.Dt(["Socket Barrier"]),
        html.Dd(["- It forces synchronization across all processes that reside on the same processor."]), ]
)

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment1,
                                                                       className="card-text"), simplifiedCode,
                                                                html.P(comment2), barriers
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
        text1,

]
