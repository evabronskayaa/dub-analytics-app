from dash import html
import dash_bootstrap_components as dbc

from components import header, general_metrics, competitors_offers

layout = html.Div([
    dbc.Container(
        children=[header, general_metrics, competitors_offers],
        fluid=True,
    ),
])

