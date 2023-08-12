from dash import html
import dash_bootstrap_components as dbc

from components import header


layout = html.Div([
    dbc.Container(
        children=[header],
        fluid=True,
    ),
])

