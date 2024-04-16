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
comment1 = "The previous pseudocode, can be simplified even more: "
comment2 = "This form makes the application's configurable parameters clear: "

configurableParameters = html.Ul([
        html.Li("Number of Messages"),
        html.Li("Message Size"),
        html.Li("Working Set Size (per process)"),
        html.Li("Number of Computing Operations (per element)"),
])
comment3 = "Apart from these, there are also 2 additional parameters that depend on the execution environment: "
environmentParameters = html.Ul([
        html.Li("Number of Computing Nodes"),
        html.Li("Number of Processes per Node"),
])
simplifiedCode = html.Pre(["""
 for time:
     communication(NumberOfMessages, MessageSize)
     
     MPI_Waitall(MessagesToSend,MessagesToRecv)
     
     computation(WorkingSetSize, NumberOfExtraOperations)
                 """], style={"font-size": "18px"})

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
                                                                html.P(comment1,
                                                                       className="card-text"), simplifiedCode,
                                                                html.P(comment2), configurableParameters, html.Br(),
                                                                html.P(comment3), environmentParameters
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
