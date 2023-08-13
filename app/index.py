import pandas as pd

from dash import Output, Input, callback
from app import app

from data import wb_data
from data_processing import get_pivot_nunique_stats
from plots import draw_competitor_stats_barchart, draw_gender_stats_piechart, draw_price_history_indicator

# callbacks are here

@callback(
    Output('menu', 'opened'),
    Output('drawer-menu', 'opened'),
    Input('menu', 'opened'),
    Input('drawer-menu', 'opened'),
    prevent_initial_call=True,
)
def drawer_demo(opened_menu, opened_drawer):
    return (False, False) if not (opened_menu or opened_drawer) else (False, True)


@app.callback(
    Output('competitor_stats_piechart', 'figure'),
)
def draw_competitor_stats():
    pivot = get_pivot_nunique_stats(wb_data, 'brand')
    return draw_competitor_stats_barchart(pivot)


@app.callback(
    Output('gender_stats_piechart', 'figure'),
)
def draw_competitor_stats():
    pivot = get_pivot_nunique_stats(wb_data, 'gender')
    return draw_gender_stats_piechart(pivot)



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
