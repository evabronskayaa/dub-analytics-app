from dash import dash
import dash_bootstrap_components as dbc

from layouts import layout

app = dash.Dash(__name__, title='DUB Analytics')
app.config.suppress_callback_exceptions = True

app.layout = layout

