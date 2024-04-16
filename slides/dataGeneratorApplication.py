# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = 'Data Generator Application'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})


stencilApplications = ("The Data Generator Application, was developed in C using MPI."
                       "  It is based on the Jacobi kernel for a 2-D data grid and it involves the partitioning of this"
                       " data grid. The number of partitions, is equal to the number of available processes and each"
                       " process takes responsibility of one data partition. For data on the borders of each partition,"
                       " communication between neighbouring processes is needed. "
                       " The following pseudocode snippet and the accompanying figure, sum up the operation of our application: "
                      )

appCode = html.Pre(["""
 for time:
     iNeighbourIndex = 0
     while MessagesSent < """,html.B("NumberOfMessages"),""":
         if iNeighbourIndex > NumberOfNeighbours-1:
            iNeighbourIndex = 0
         iNeighbour = Neighbours[iNeighbourIndex]
         MPI_Irecv(""",html.B("MessageSize"),""", iNeighbour)
         MPI_Isend(MessageSize, iNeighbour)
         MessagesSent++
         iNeighbourIndex++
 
     MPI_Waitall(MessagesToSend,MessagesToRecv)
 
     for i in """,html.B("rows"),""":
         for j in """,html.B("columns"),""":
             for """,html.B("NumberOfExtraOperations"),""":
                 compute(i, j, u_previous, u_current)
                 """], style={"font-size":"15px"})

# appFigure = [html.Br(), html.Embed(src="assets/dataGeneratorCommPattern.pdf#toolbar=0&navpanes=0&scrollbar=0",
#                                    height="100%", width="100%")]

appFigure = [html.Br(), html.Img(src="assets/dataGeneratorCommPattern.png", width="100%")]

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(stencilApplications,
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
code1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(appCode),
                                dbc.Col(appFigure),
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
        code1,

]
