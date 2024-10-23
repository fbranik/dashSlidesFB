# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Data Sizes and Strong/Weak Scaling"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

comment1 = "Two of the previous five parameters are data sizes; the working set size and the message size."
comment2 = ("For the working set size, there is a choice to be made on how it changes as the number of total processes"
            " grows.  There are two main approaches: ")
scaling = html.Ul([
        html.Li([html.B("Strong Scaling, "),
                 "where the total problem size remains constant as the number of processes grows."]),
        html.Li([html.B("Weak Scaling, "),
                 "where the total problem size changes in accordance to the growing resources."]),
])
comment3 = ("Because computer clusters are designed in a way that enables large system scales that work with greater"
            " data sizes, "
            "the strategy that was chosen for the context of our experiments is weak scaling.")

comment4 = ("For the message size, it was chosen for it to be a function of the working set size, "
            " specifically some multiple of it's square root. This was done to imitate the exchange of"
            " the face of a 2D data grid.")

appFigure = [html.Br(), html.Img(src="assets/dataGeneratorCommPattern.png", width="100%")]

text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardBody(
                                                        [
                                                                html.P(comment1), html.Br(), html.P(comment2),
                                                                scaling, html.P(comment3),
                                                                html.Br(), html.P(comment4)
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
