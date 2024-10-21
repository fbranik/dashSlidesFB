# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...

title = 'Intro'
# titleBar = html.H4(title, className="bg-primary text-white p-4 mb-2 text-left"),
titleBar = html.H4('I', className="p-4 mb-2 text-left", style={'background': 'ghostwhite', 'color': 'ghostwhite',
                                                               "font-size" : "30px"})

row1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(html.Img(src="assets/logo.png", width="80%"))),
                        ]
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)
row2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        dbc.CardBody([
                                                "National Technical University of Athens", html.Br(),
                                                "School of Electrical and Computer Engineering", html.Br(), html.Br(),
                                                "Fotios Branikas", html.Br(), html.Br(),
                                                html.B("Performance Analysis and Modeling of Parallel Applications in"),
                                                html.Br(),
                                                html.B("Distributed Memory Architectures"),
                                                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                                                "Diploma Thesis", html.Br(), html.Br(), html.Br(),
                                                ""
                                        ]),
                                        className="mb-3", style={"color" : "black", "background": "ghostwhite",
                                                                 "border": "ghostwhite"},
                                ))),

                        ]
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)
content = [
        titleBar,
        row1, html.Br(), html.Br(), html.Br(),
        row2

]
