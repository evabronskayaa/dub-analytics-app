import pandas as pd
from datetime import datetime, date

from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from plots import draw_indicator


def get_pivot_nunique_stats(df: pd.DataFrame, index: str) -> pd.DataFrame:
    temp = df.groupby(index)[['product_id']] \
        .nunique() \
        .reset_index() \
        .rename(columns={'product_id': 'count_items'}) \
        .sort_values(by='count_items', ascending=False)

    return temp[:5]


def get_price_history_data(current_price: int,
                           price_history: str) -> (list, list):
    try:
        price_history = eval(price_history)
    except:
        return None
    price_history = [{'dt': datetime.fromtimestamp(pair['dt']),
                      'price': pair['price']['RUB'] / 100} for pair in price_history]

    dates_data = [x['dt'] for x in price_history]
    prices_data = [x['price'] for x in price_history]

    dates_data.append(date.today())
    prices_data.append(current_price)

    return dates_data, prices_data


def draw_competitor_stats(product):
    dates_data, prices_data = get_price_history_data(current_price=product.sale_price,
                                                     price_history=product.price_history)
    return draw_indicator(dates_data, prices_data)


def sort_df_by_filter(df, series_name, series_values):
    if not series_values:
        series_values = df[series_name].unique()

    df = df[df[series_name].isin(series_values)]
    return df


def sort_df_by_all_filters(df, checkbx_brand, checkbx_gender, checkbx_category):
    filtrated_df = sort_df_by_filter(df=df, series_name='brand', series_values=checkbx_brand)
    filtrated_df = sort_df_by_filter(df=filtrated_df, series_name='gender', series_values=checkbx_gender)
    filtrated_df = sort_df_by_filter(df=filtrated_df, series_name='category2', series_values=checkbx_category)

    return filtrated_df


def create_product_small_card(product, modal_demo_button_id='modal-demo-button'):
    card_img = dmc.CardSection([
        html.Div([
            dmc.Image(
                src=product.product_img,
                width=250,
                height=400,
            )])
    ],
        className='img'
    )

    card_content = html.Div([
        html.Div([
            dmc.Text(product.brand, weight=700, className='card-text'),
            dmc.Text(product.product_name, weight=500, className='card-text'),
            dmc.Text(
                product.orders_count_str,
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                product.rating_str,
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                product.feedbacks_count_str,
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                product.materials,
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                product.description[:200],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
        ],
            className='card-section'
        ),
        dmc.Button("Подробнее", id=modal_demo_button_id),
    ],
        className='card-section2'
    )

    return card_img, card_content


def create_product_modal_card(product, modal_simple_id='modal-simple'):
    modal = dmc.Modal(
        id=modal_simple_id,
        zIndex=10000,
        children=[
            html.Div([
                html.Div([dmc.Image(
                    src=product.product_img,
                    width=418,
                    height=625,
                    style={'margin': '-18.75% 0 -3.75% 0'}
                )])
            ], className='card-section'),
            html.Div([
                dmc.Text(product.brand, weight=700, size="xl", className='card-text'),
                dmc.Text(product.product_name, weight=500, size="xl", className='card-text'),
                dmc.Anchor('Ссылка на товар на Wildberries', href=product.product_url),
                dmc.Space(h=20),
                dcc.Graph(figure=draw_competitor_stats(product)),
                dmc.Space(h=20),
                dmc.Text(
                    product.orders_count_str,
                    color="#000000",
                    className='card-text'
                ),
                dmc.Text(
                    product.rating_str,
                    color="#000000",
                    className='card-text'
                ),
                dmc.Text(
                    product.feedbacks_count_str,
                    color="#000000",
                    className='card-text'
                ),
                dmc.Text(
                    product.volume_str,
                    color="#000000",
                    className='card-text',
                    style={'margin-bottom': '20px'}
                ),
                dmc.Text(
                    product.materials,
                    color="dimmed",
                    className='card-text'
                ),
                dmc.Text(
                    product.manufacturer_country,
                    color="dimmed",
                    className='card-text'
                ),
                dmc.Text(
                    product.colors,
                    color="dimmed",
                    className='card-text'
                ),
                dmc.Text(
                    product.sizes,
                    color="dimmed",
                    className='card-text'
                ),
                dmc.Spoiler(
                    showLabel="Показать полностью",
                    hideLabel="Скрыть",
                    maxHeight=50,
                    children=[
                        dmc.Text(
                            product.description,
                            color="dimmed",
                            className='card-text'
                        )
                    ],
                ),
            ],
                className='card-section modal-text modal',
            )
        ],
        className='card-section2'
    )

    return modal


def create_product_card(product_1, product_2):
    small_card_1_img, small_card_1_content = create_product_small_card(product_1, modal_demo_button_id='modal-demo-button')
    small_card_2_img, small_card_2_content = create_product_small_card(product_2, modal_demo_button_id='modal-demo-button-2')

    modal_card_1 = create_product_modal_card(product_1, modal_simple_id='modal-simple')
    modal_card_2 = create_product_modal_card(product_2, modal_simple_id='modal-simple-2')

    card_1 = dmc.Card([
        small_card_1_img, small_card_1_content,
        modal_card_1
    ],
        withBorder=True,
        className='card',
    )

    card_2 = dmc.Card([
        small_card_2_img, small_card_2_content,
        modal_card_2
    ],
        withBorder=True,
        className='card',
    )

    return card_1, card_2
