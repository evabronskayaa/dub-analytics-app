import pandas as pd

from dash import Output, Input, callback, State, html
import dash_mantine_components as dmc

from app import app
from data import wb_data
from data_processing import get_pivot_nunique_stats, get_price_history_data
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


@callback(
    Output("modal-simple", "opened"),
    Input("modal-demo-button", "n_clicks"),
    State("modal-simple", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, opened):
    return not opened


@callback(
    Output("modal-simple-2", "opened"),
    Input("modal-demo-button-2", "n_clicks"),
    State("modal-simple-2", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, opened):
    return not opened


@app.callback(
    Output('competitor-stats-barchart', 'figure'),
    Input('drawer-menu', 'figure'),
)
def draw_competitor_stats(rb_brand):
    pivot = get_pivot_nunique_stats(wb_data, 'brand')
    return draw_barchart(pivot, 'brand', title='Количество предложений по конкурентам')


@app.callback(
    Output('gender-stats-piechart', 'figure'),
    Input('drawer-menu', 'figure'),
)
def draw_competitor_stats(checkbx_gender):
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
    Output('price-history', 'figure'),
    Input('drawer-menu', 'figure'),
)
def draw_competitor_stats(value):
    dates_data, prices_data = get_price_history_data(current_price=wb_data.sale_price,
                                                     price_history=wb_data.price_history)
    return draw_indicator(dates_data, prices_data)


# @app.callback(
#     Output('gender_stats_piechart', 'figure'),
#     Input('checkbx-brand', 'value'),
# )
# def draw_competitor_stats(rb_brand):
#     if rb_brand is not None:
#         filtered_data = wb_data[wb_data.brand.isin([rb_brand])]
#
#     pivot = get_pivot_nunique_stats(filtered_data, 'brand')
#     return draw_barchart(pivot, 'brand')


@app.callback(
    Output('top_positions_first_product_img', 'children'),
    Output('top_positions_first_brand', 'children'),
    Output('top_positions_first_name', 'children'),
    Output('top_positions_first_orders_count', 'children'),
    Output('top_positions_first_rating', 'children'),
    Output('top_positions_first_feedbacks_count', 'children'),
    Output('top_positions_first_materials', 'children'),
    Output('top_positions_first_description', 'children'),

    Output('top_positions_first_modal_product_img', 'children'),
    Output('top_positions_first_modal_product_url', 'href'),
    Output('top_positions_first_modal_brand', 'children'),
    Output('top_positions_first_modal_name', 'children'),
    Output('top_positions_first_modal_manufacturer_country', 'children'),
    # Output('top_positions_first_modal_season', 'children'),
    Output('top_positions_first_modal_rating', 'children'),
    Output('top_positions_first_modal_feedbacks_count', 'children'),
    Output('top_positions_first_modal_materials', 'children'),
    Output('top_positions_first_modal_description', 'children'),
    Output('top_positions_first_modal_sizes', 'children'),
    Output('top_positions_first_modal_colors', 'children'),
    Output('top_positions_first_modal_orders_count', 'children'),
    Output('top_positions_first_modal_volume', 'children'),

    Output('top_positions_second_product_img', 'children'),
    Output('top_positions_second_brand', 'children'),
    Output('top_positions_second_name', 'children'),
    Output('top_positions_second_rating', 'children'),
    Output('top_positions_second_feedbacks_count', 'children'),
    Output('top_positions_second_materials', 'children'),
    Output('top_positions_second_description', 'children'),

    Output('top_positions_second_modal_product_img', 'children'),

    Input('pagination', 'page'),
)
def draw_competitor_stats(page):
    top_positions = wb_data.sort_values(['rating', 'orders_count', 'feedbacks_count'], ascending=False).head(10)

    match page:
        case 1:
            top_positions = top_positions[:2]
        case 2:
            top_positions = top_positions[2:4]
        case 3:
            top_positions = top_positions[4:6]
        case 4:
            top_positions = top_positions[6:8]
        case 5:
            top_positions = top_positions[8:10]

    product_img_1 = dmc.Image(
        src=top_positions.product_img.iloc[0],
        width=250,
        height=400,
    )

    product_img_modal_1 = dmc.Image(
        src=top_positions.product_img.iloc[0],
        width=418,
        height=600,
    )

    product_img_2 = dmc.Image(
        src=top_positions.product_img.iloc[1],
        width=250,
        height=400,
    )

    product_img_modal_2 = dmc.Image(
        src=top_positions.product_img.iloc[1],
        width=418,
        height=600,
    )

    return product_img_1, top_positions.brand.iloc[0], top_positions.name.iloc[0], top_positions.orders_count_str.iloc[0],\
        top_positions.rating_str.iloc[0], top_positions.feedbacks_count_str.iloc[0], top_positions.materials.iloc[0], \
        top_positions.description.iloc[0][:200] + '...', \
        product_img_modal_1, top_positions.product_url.iloc[0], top_positions.brand.iloc[0], \
        top_positions.name.iloc[0], top_positions.manufacturer_country.iloc[0], top_positions.rating_str.iloc[0], \
        top_positions.feedbacks_count_str.iloc[0], top_positions.materials.iloc[0], top_positions.description.iloc[0],  top_positions.sizes.iloc[0], \
        top_positions.colors.iloc[0], top_positions.orders_count_str.iloc[0], top_positions.volume_str.iloc[0], \
        product_img_2, top_positions.brand.iloc[1], top_positions.name.iloc[1], \
        top_positions.rating.iloc[1], top_positions.feedbacks_count.iloc[1], top_positions.materials.iloc[1], \
        top_positions.description.iloc[1][:200] + '...', product_img_modal_2


if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(host='0.0.0.0', debug=True)
