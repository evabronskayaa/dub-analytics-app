import pandas as pd

from dash import Output, Input, callback
from app import app

from data import wb_data
from data_processing import get_pivot_nunique_stats
from plots import draw_barchart, draw_piechart, draw_indicator


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
    Output('competitor-stats-barchart', 'figure'),
    Input('drawer-menu', 'figure'),
)
def draw_competitor_stats(value):
    pivot = get_pivot_nunique_stats(wb_data, 'brand')
    return draw_barchart(pivot, 'brand', title='Количество предложений по конкурентам')


@app.callback(
    Output('gender-stats-piechart', 'figure'),
    Input('drawer-menu', 'figure'),
)
def draw_competitor_stats(value):
    pivot = get_pivot_nunique_stats(wb_data, 'gender')
    return draw_piechart(pivot)


@app.callback(
    Output('category2-stats-barchart', 'figure'),
    Input('drawer-menu', 'figure'),
)
def draw_competitor_stats(value):
    pivot = get_pivot_nunique_stats(wb_data, 'category2')
    return draw_barchart(pivot, 'category2', title='Количество предложений по категориям')


@app.callback(
    Output('competitor_stats_piechart', 'figure'),
    Input('checkbx-gender', 'value'),
)
def draw_competitor_stats(checkbx_gender):
    pivot = get_pivot_nunique_stats(wb_data, 'gender')
    return draw_piechart(pivot)


@app.callback(
    Output('gender_stats_piechart', 'figure'),
    Input('checkbx-brand', 'value'),
)
def draw_competitor_stats(rb_brand):
    if rb_brand is not None:
        filtered_data = wb_data[wb_data.brand.isin([rb_brand])]
    pivot = get_pivot_nunique_stats(filtered_data, 'brand')
    return draw_barchart(pivot, 'brand')

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(host='0.0.0.0', debug=True)
