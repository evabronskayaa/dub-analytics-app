from dash import html
import dash_bootstrap_components as dbc

from components import header, general_metrics, competitors_offers, footer

layout = html.Div([
    dbc.Container(
        children=[header, general_metrics, competitors_offers, footer],
        fluid=True,
    ),
])

