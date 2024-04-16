# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...

title = 'Intro'

accordion = html.Div(
        dbc.Accordion(
                [
                        dbc.AccordionItem(
                                "This is the content of the first section",
                                title="Item 1",
                        ),
                ],
                active_item="item-1",
                always_open=True, style={"padding": "75px"}
        )
)

content = [
        html.H4(title, className="bg-primary text-white p-4 mb-2 text-left"),

        html.Div(
                style=dict(textAlign="center"),
                children=[
                        html.Br(),
                        html.Div(accordion)
                ])

]


@app.callback(Output("intro-div", "children"), [Input("intro-button", "n_clicks")])
def create_template_graph(n):
    return "Button has been clicked {} times.".format(n)
