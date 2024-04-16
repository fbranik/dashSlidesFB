from presentation import presentation_title
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, ClientsideFunction, html, dcc, ctx

external_stylesheets = [dbc.themes.BOOTSTRAP]
url_theme1 = dbc.themes.SANDSTONE


# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


app = dash.Dash(__name__,external_stylesheets=[url_theme1, dbc_css])
app.config.suppress_callback_exceptions = True
app.title = presentation_title
app.clientside_callback(
    """
        function(id) {
            document.addEventListener("keydown", function(event) {
                if (event) {
                    if (event.keyCode == '37' || event.keyCode ==  '38') {
                        document.getElementById('previous-link').click()
                        event.stopPropogation()
                    }
                    if (event.keyCode == '39' || event.keyCode == '40') {
                        document.getElementById('next-link').click()
                        event.stopPropogation()
                    }
                }
            });
            return window.dash_clientside.no_update       
        }
    """,
    Output("previous-link", "id"),
    Input("previous-link", "id")
)
server = app.server
