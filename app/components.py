import pandas as pd

from dash import html, dash, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from data import wb_data
from data_processing import get_unique_series_values


header_filters = dmc.Grid([
    dmc.CheckboxGroup(
        id="checkbx-brand",
        label="Конкурент",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="LIME", value="LIME"),
            dmc.Checkbox(label="Befree", value="Befree"),
            dmc.Checkbox(label="Bershka", value="Bershka"),
            dmc.Checkbox(label="Pull&Bear", value="Pull&Bear"),
        ],
        value=[],
        className='menu-item'
    ),
    dmc.CheckboxGroup(
        id="checkbx-gender",
        label="Коллекция",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="Woman", value="Женский"),
            dmc.Checkbox(label="Man", value="Мужской"),
        ],
        value=[],
        className='menu-item'
    ),
    dmc.Spoiler(
        showLabel="Еще",
        hideLabel="Скрыть",
        maxHeight=80,
        children=[
            dmc.CheckboxGroup(
                id="checkbx-category",
                label="Категория",
                orientation="horizontal",
                offset="md",
                mb=10,
                children=[dmc.Checkbox(label=i, value=i) 
                          for i in sorted(get_unique_series_values(df=wb_data[wb_data.category2.notna()], 
                                                            series_name='category2'))
                ],
                value=[],
                className='menu-item'
            ),
        ],
        className='category-checkboxes'
    ),
    dmc.CheckboxGroup(
        id="checkbox-sizes",
        label="Размер",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="XXS", value="XXS"),
            dmc.Checkbox(label="XS", value="XS"),
            dmc.Checkbox(label="S", value="S"),
            dmc.Checkbox(label="M", value="M"),
            dmc.Checkbox(label="L", value="L"),
            dmc.Checkbox(label="XL", value="XL"),
            dmc.Checkbox(label="XXL", value="XXL"),
        ],
        value=[],
        className='menu-item'
    ),
],
    className='menu'
)

header = html.Header([
    dmc.Burger(id='menu', opened=False, className='burger'),
    dmc.Drawer(
        [header_filters],
        id='drawer-menu',
        title='Фильтры',
        padding='md',
        size=450,
        opened=False,
        zIndex=10000,
    ),
    dmc.Image(
        src='assets/img/logo.png', alt='logo', width=75, className='center-block'
    )],
    id='header',
    className='container',
)

general_metrics = html.Div([
    dmc.Grid([
        dmc.Col(dcc.Graph(id='competitor-stats-barchart'), span=3, className='graph', mr=5),
        dmc.Col(dcc.Graph(id='gender-stats-piechart'), span=3, className='graph', mx=5),
        dmc.Col(dcc.Graph(id='category2-stats-barchart'), span=3, className='graph', ml=5),
    ],
        gutter="xl",
        grow=True,
        className='graphs'
    )
])

card_1 = html.Div(id='card_1')
card_2 = html.Div(id='card_2')
card_3 = html.Div(id='card_3')
card_4 = html.Div(id='card_4')

cards = dmc.SimpleGrid(
    cols=2,
    # rows=2,
    children=[
        card_1, card_2, card_3, card_4
    ]
)

competitors_offers = html.Div([
    dmc.Text('Топ-10 предложений конкурентов', className='block-title'),
    cards,
    dmc.Pagination(id='pagination', total=5, siblings=1, page=1, radius=0, color='#000000', withControls=True,
                   style={'float': 'right'}),
],
    className='offers'
)

footer = dmc.Footer([
    dmc.Text("DUB ANALYTICS | 2023")
],
    height=100,
    className='footer'
)
