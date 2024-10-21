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

appCode = html.Pre(["""
for time:
    iNeighbourIndex = 0
    while MessagesSent < """, ("NumberOfMessages"), """:
        if iNeighbourIndex > NumberOfNeighbours-1:
           iNeighbourIndex = 0
        iNeighbour = Neighbours[iNeighbourIndex]
        MPI_Irecv(""", ("MessageSize"), """, iNeighbour)
        MPI_Isend(MessageSize, iNeighbour)
        MessagesSent++
        iNeighbourIndex++

    MPI_Waitall(MessagesToSend, MessagesToRecv)

    for i in """, ("rows"), """:
        for j in """, ("columns"), """:
            for """, ("NumberOfExtraOperations"), """:
                compute(i, j, u_previous, u_current)
                """], style={"font-size": "18px"})

simplifiedCode = html.Pre(["""
 for time:
     communication(NumberOfMessages, MessageSize)

     MPI_Waitall(MessagesToSend,MessagesToRecv)

     computation(WorkingSetSize, NumberOfExtraOperations)
                 """], style={"font-size": "18px"})

appFigure = [html.Br(), html.Img(src="assets/dataGeneratorCommPattern.png", width="100%")]
arrow = [html.Br(), html.Img(src="assets/codeArrow.png", width="50%")]

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

simplifiedCode = html.Div(
        html.Table(
                [
                        html.Tr(
                                [
                                        html.Td(arrow, style={"textAlign"  : "center", "display": "flex",
                                                              "align-items": "center", "justify-content": "right"}),
                                        html.Td(simplifiedCode),

                                ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                        ),
                ], )
)

content = [
        titleBar,
        html.Br(),
        code,
        # simplifiedCode
]
