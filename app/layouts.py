from dash import html
import dash_bootstrap_components as dbc

from components import header, general_metrics, competitors_offers, menu

layout = html.Div([
    dbc.Container(
        children=[header, menu, general_metrics, competitors_offers],
        fluid=True,
    ),
])

