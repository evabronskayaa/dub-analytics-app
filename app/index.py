from dash import Output, Input, callback, State, html

from app import app
from data import wb_data
from data_processing import get_pivot_nunique_stats, create_product_card, sort_df_by_filter, \
    sort_df_by_all_filters
from plots import draw_barchart, draw_piechart


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


@callback(
    Output("modal-simple-3", "opened"),
    Input("modal-demo-button-3", "n_clicks"),
    State("modal-simple-3", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, opened):
    return not opened


@callback(
    Output("modal-simple-4", "opened"),
    Input("modal-demo-button-4", "n_clicks"),
    State("modal-simple-4", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, opened):
    return not opened


@app.callback(
    Output('competitor-stats-barchart', 'figure'),
    Input('checkbx-brand', 'value'),
    Input('checkbx-gender', 'value'),
    Input('checkbx-category', 'value'),
)
def draw_competitor_stats(checkbx_brand, checkbx_gender, checkbx_category):
    filtrated_df = sort_df_by_all_filters(df=wb_data,
                                          checkbx_brand=checkbx_brand,
                                          checkbx_gender=checkbx_gender,
                                          checkbx_category=checkbx_category)

    filtrated_df = sort_df_by_filter(df=filtrated_df, series_name='brand', series_values=checkbx_brand)

    pivot = get_pivot_nunique_stats(filtrated_df, 'brand')

    return draw_barchart(pivot, 'brand', title='Количество предложений по конкурентам')


@app.callback(
    Output('gender-stats-piechart', 'figure'),
    Input('checkbx-brand', 'value'),
    Input('checkbx-gender', 'value'),
    Input('checkbx-category', 'value'),
)
def draw_gender_stats(checkbx_brand, checkbx_gender, checkbx_category):
    filtrated_df = sort_df_by_all_filters(df=wb_data,
                                          checkbx_brand=checkbx_brand,
                                          checkbx_gender=checkbx_gender,
                                          checkbx_category=checkbx_category)

    pivot = get_pivot_nunique_stats(filtrated_df, 'gender')

    return draw_piechart(pivot)


@app.callback(
    Output('category2-stats-barchart', 'figure'),
    Input('checkbx-brand', 'value'),
    Input('checkbx-gender', 'value'),
    Input('checkbx-category', 'value'),
)
def draw_category_stats(checkbx_brand, checkbx_gender, checkbx_category):
    filtrated_df = sort_df_by_all_filters(df=wb_data,
                                          checkbx_brand=checkbx_brand,
                                          checkbx_gender=checkbx_gender,
                                          checkbx_category=checkbx_category)

    pivot = get_pivot_nunique_stats(filtrated_df, 'category2')

    return draw_barchart(pivot, 'category2', title='Количество предложений по категориям')


@app.callback(
    Output('card_1', 'children'),
    Output('card_2', 'children'),
    Output('card_3', 'children'),
    Output('card_4', 'children'),
    Output('pagination', 'total'),
    Input('pagination', 'page'),
    Input('checkbx-brand', 'value'),
    Input('checkbx-gender', 'value'),
    Input('checkbx-category', 'value'),
    Input("framework-select", "value")
)
def draw_competitor_stats(page, checkbx_brand, checkbx_gender, checkbx_category, sorting):
    filtrated_df = sort_df_by_all_filters(df=wb_data,
                                          checkbx_brand=checkbx_brand,
                                          checkbx_gender=checkbx_gender,
                                          checkbx_category=checkbx_category)

    if sorting is None:
        sorting = ['rating', 'orders_count', 'feedbacks_count']
    else:
        sorting = [sorting]

    top_positions = filtrated_df.sort_values(sorting, ascending=False).head(32)

    max_page = top_positions.shape[0] // 4
    top_positions = top_positions[:max_page * 4]
    top_positions = top_positions[:page * 4]

    card_1, card_2, card_3, card_4 = create_product_card(top_positions.iloc[-1],
                                                         top_positions.iloc[-2],
                                                         top_positions.iloc[-3],
                                                         top_positions.iloc[-4])

    return card_1, card_2, card_3, card_4, max_page


if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(host='0.0.0.0', debug=True)
