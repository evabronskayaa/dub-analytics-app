from dash import html
import dash_bootstrap_components as dbc

header = html.Header(
    dbc.Container([
        html.H1('DUB'),
    ],
        id='header',
        className="",
        style=dict(textAlign='left'),
        fluid=True,
    ),
)