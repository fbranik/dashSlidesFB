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

appCode = html.Pre([""" for time:
     communication(NumberOfMessages, MessageSize)

     MPI_Waitall(MessagesToSend,MessagesToRecv)

     """,html.B("MPI_Barrier(custom_communicator);", style={"font-size": "22px"}),"""

     computation(WorkingSetSize, NumberOfExtraOperations)"""], style={"font-size": "18px"})

appFigure = [html.Br(), html.Img(src="assets/nodeGlobalBarrier.png", width="100%")]

code = html.Div(
        html.Table(
                [
                        html.Tr(
                                [
                                        html.Td(appCode), html.Td(appFigure),

                                ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                        ),
                ], )
)

content = [
        titleBar,
        html.Br(),
        code,
]
