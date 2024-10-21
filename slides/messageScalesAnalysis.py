# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600
title = "Message Size Scale Analysis"
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

big = [html.Img(src="assets/64_20_VarComm_Plot_Big.png", width="100%")]
small = [html.Img(src="assets/64_20_VarComm_Plot_Small.png", width="100%")]

plot1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(small),
                                dbc.Col(big, style={"textAlign"  : "center", "display": "flex",
                                                    "align-items": "center", "justify-content": "center"}),

                        ], style={"padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)
plot2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col([html.P(["Small Messages", html.Br(), html.Br(),
                                                 html.P("- Large Standard Deviation"),
                                                 html.P("- Number of Messages does not make significant changes")], )],
                                        style={"textAlign"      : "left",
                                               "display"        : "flex",
                                               "align-items"    : "center",
                                               "justify-content": "center"}),

                                dbc.Col([html.P(["Large Messages", html.Br(), html.Br(),
                                                 html.P("- Small Standard Deviation"),
                                                 html.P("- Number of Messages has clear effect")], )],
                                        style={"textAlign"      : "left",
                                               "display"        : "flex",
                                               "align-items"    : "center",
                                               "justify-content": "center"}),

                        ], style={"padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "center", "display": "flex",
                  "align-items": "center", "justify-content": "center"}
)

content = [
        titleBar,
        html.Br(),
        plot1,
        html.Hr(),
        plot2,
]
