from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import os
import importlib
from sys import path
path.append(os.getcwd())
path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from server import app, server
from presentation import slide_order, prev_text, next_text, slide_orderDict
# add the slides to the object space if they are in the slide order
for x in os.listdir(os.getcwd() + "/slides"):
    slide_name = x.split(".")[0]
    if slide_name in slide_order:
        globals()["slide_" + slide_name] = importlib.import_module(
                "slides." + slide_name
        )


# helper function that returns dict of enumerated slide names
def slide_dict():
    d = {v: k for k, v in dict(enumerate(slide_order)).items()}
    d["/"] = 0
    return d


nav_style = dict(
        textAlign="center",
)


def nav_button_div(text):
    """helper function to return the navigation buttons easily"""
    return dbc.Button(html.H4(text), style=dict(width="100%"), color="primary")


header_height, footer_height = "6rem", "5rem"
navPagesStyle = {
        "position": "absolute",
        "top"     : 15,
        "right"   : 0,
        "height"  : footer_height,
}
footerStyle = {
        "position"        : "absolute",
        "bottom"          : 0,
        "left"            : 0,
        "right"           : 0,
        "height"          : "3rem",
        "padding"         : "1rem 1rem",
        "background-color": "SlateGray",
        "width"           : "100%"
}
containerStyle = {
        "aspect-ratio": "4 / 3",
        "width"       : "100%",
        "height"      : "100%",
        "background"  : "ghostwhite",
        "position"    : "absolute",
        "top"         : "0",
        "left"        : "0",
        "right"       : "0",
        "bottom"      : "0",

}


# logo if there is one
def get_logo():
    assets = os.listdir(os.getcwd() + "/assets/")
    split_assets = [x.split(".")[0] for x in assets]
    for i, x in enumerate(split_assets):
        if x == "logo":
            return html.Img(src="assets/" + assets[i], style=dict(height="50px"))
    return html.Img(
            height="40px",
            src="https://github.com/russellromney/dash-slides/assets/raw/logo.png",
    )


app.layout = dbc.Container(
        style=containerStyle,
        children=[
                html.Div([
                        html.Div(id="current-slide", style=dict(display="none", children="")),
                        # nav div
                        html.Div(
                                [
                                        dcc.Location(id="url", refresh=False),

                                        html.Div(id="page-content", style={"width": "100%", "height": "100%",}),
                                ], style={"width": "100%", "height": "100%"}
                        ),
                        html.Table(
                                children=[
                                        html.Tr(
                                                [
                                                        html.Td('Fotios Branikas',
                                                                style={"text-align": "center", "width": "33.3%"},
                                                                className="text-white"),
                                                        html.Td('National Technical University of Athens',
                                                                style={"text-align": "center", "width": "33.3%"},
                                                                className="text-white"),
                                                        html.Td([

                                                                dbc.ButtonGroup(
                                                                        [
                                                                                dbc.Button("April 19, 2024", style={
                                                                                        "background": "SlateGray",
                                                                                        "border"    : "SlateGray",
                                                                                        "text-align": "center"},
                                                                                           href=""
                                                                                           ),
                                                                                dbc.Button("<", style={
                                                                                        "background": "SlateGray",
                                                                                        "border"    : "SlateGray",
                                                                                        "text-align": "center"},
                                                                                           id="previous-link",
                                                                                           href="",
                                                                                           ),
                                                                                dbc.DropdownMenu(
                                                                                        id="slide-count", style={
                                                                                                "background": "SlateGray",
                                                                                                "text-align": "center"},
                                                                                        group=True,
                                                                                        children=[
                                                                                                dbc.DropdownMenuItem(
                                                                                                        k,
                                                                                                        href="/" + s,
                                                                                                )
                                                                                                for k,s in slide_orderDict.items()
                                                                                        ],
                                                                                ),
                                                                                dbc.Button(">", style={
                                                                                        "background": "SlateGray",
                                                                                        "border"    : "SlateGray",
                                                                                        "text-align": "center"},
                                                                                           id="next-link",
                                                                                           href="",
                                                                                           ),
                                                                        ],
                                                                        size="lg",
                                                                        style={"background": "SlateGray"}
                                                                )
                                                        ], style={"text-align": "center", "width": "33.3%"},
                                                                className="text-white"),
                                                ]
                                        )], style=footerStyle,
                        ), ], style=containerStyle)
        ],
)


###
# url function
@app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")],
)
def change_slide(pathname):
    """gets current slide goes either back a slide or forward a slide"""
    if pathname == "/" or pathname == "/" + slide_order[0] or pathname == None:
        return globals()["slide_" + slide_order[0]].content
    else:
        try:
            pathname = pathname.split("/")[1].strip()
            return globals()["slide_" + pathname].content
        except:
            return "404"


###

###
# navigation functions
@app.callback(
        [Output("next-link", "href"), Output("previous-link", "href")],
        [Input("current-slide", "children")],
        [State("url", "pathname")],
)
def navigate(current_slide, pathname):
    """
    - listens to
        - next/previous buttons
    - determines the current slide name
    - changes 'next' and 'previous' to the names of the slides on each side of the current slide
    - if this is the last or first slide, 'next' or 'previous' will just refresh the current slide
    """
    next_slide = current_slide
    previous_slide = current_slide
    current_order = slide_dict()[current_slide]
    num_slides = max(slide_dict().values())

    # if we're on the first slide, clicking 'previous' just refreshes the page
    if current_order != 0:
        previous_slide = slide_order[current_order - 1]
    # if we're on the last slide, clicking 'next' just refreshes the page
    if current_order != num_slides:
        next_slide = slide_order[current_order + 1]

    return next_slide, previous_slide


@app.callback(Output("current-slide", "children"), [Input("url", "pathname")])
def set_slide_state(pathname):
    """
    returns the name of the current slide based on the pathname
    this runs first and triggers navigate (changes the relative hrefs of 'next' and 'previous')
    """
    if pathname is None:
        return "/"
    if "/" in pathname:
        if pathname == "/":
            return pathname
        return pathname.split("/")[1].strip()


@app.callback(Output("slide-count", "label"), [Input("current-slide", "children")])
def update_slide_count(current_slide):
    """shows the current slide number out of the total"""
    total = len(slide_order)
    current = slide_dict()[current_slide] + 1
    return "{}/{}".format(current, total)


if __name__ == "__main__":
    app.run_server(
            host="0.0.0.0",
            port=2011,
            debug=False,
    )
