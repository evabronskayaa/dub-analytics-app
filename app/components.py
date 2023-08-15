from dash import html, dash, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from data import wb_data

header_accordion = dmc.Grid([
    dmc.CheckboxGroup(
        id="checkbox-group",
        label="Конкурент",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="LIME", value="react"),
            dmc.Checkbox(label="Befree", value="vue"),
            dmc.Checkbox(label="Bershka", value="svelte"),
            dmc.Checkbox(label="Pull&Bear", value="angular"),
        ],
        value=[],
        className='menu-item'
    ),
    dmc.CheckboxGroup(
        id="checkbox-group2",
        label="Коллекция",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="Woman", value="react"),
            dmc.Checkbox(label="Man", value="vue"),
        ],
        value=[],
        className='menu-item'
    ),
    dmc.CheckboxGroup(
        id="checkbox-group3",
        label="Категория",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="Пальто", value="react"),
            dmc.Checkbox(label="Куртки", value="vue"),
            dmc.Checkbox(label="Платья", value="vue"),
            dmc.Checkbox(label="Топы", value="vue"),
            dmc.Checkbox(label="Юбки", value="vue"),
            dmc.Checkbox(label="Блузки", value="vue"),
            dmc.Checkbox(label="Шорты", value="vue"),
            dmc.Checkbox(label="Футболки", value="vue"),
            dmc.Checkbox(label="Джинсы", value="vue"),
            dmc.Checkbox(label="Рубашки", value="vue"),
            # dmc.Checkbox(label="Свитеры", value="vue"),
            # dmc.Checkbox(label="Блузки-боди", value="vue"),
            # dmc.Checkbox(label="Кардиганы", value="vue"),
            # dmc.Checkbox(label="Толстовки", value="vue"),
            # dmc.Checkbox(label="Пуловеры", value="vue"),
            # dmc.Checkbox(label="Комбинезоны", value="vue"),
            #
            # dmc.Checkbox(label="Блейзеры", value="vue"),
            # dmc.Checkbox(label="Дубленки", value="vue"),
            # dmc.Checkbox(label="Леггинсы", value="vue"),
            # dmc.Checkbox(label="Плащи", value="vue"),
            #
            # dmc.Checkbox(label="Пуховики", value="vue"),
            # dmc.Checkbox(label="Пиджаки", value="vue"),
            # dmc.Checkbox(label="Рубашки пижамные", value="vue"),
            # dmc.Checkbox(label="Бомберы", value="vue"),
            #
            # dmc.Checkbox(label="Лонгсливы", value="vue"),
            # dmc.Checkbox(label="Тренчкоты", value="vue"),
            # dmc.Checkbox(label="Жилеты", value="vue"),
            # dmc.Checkbox(label="Ветровки", value="vue"),
            #
            # dmc.Checkbox(label="Полукомбинезоны", value="vue"),
            # dmc.Checkbox(label="Джемперы", value="vue"),
            # dmc.Checkbox(label="Худи", value="vue"),
            # dmc.Checkbox(label="Футболки-поло", value="vue"),
            #
            # dmc.Checkbox(label="Свитшоты", value="vue"),
            # dmc.Checkbox(label="Жакеты", value="vue"),
            # dmc.Checkbox(label="Жилеты утепленные", value="vue"),
            #
            # dmc.Checkbox(label="Сарафаны", value="vue"),
            # dmc.Checkbox(label="Брюки пижамные", value="vue"),
            # dmc.Checkbox(label="Шорты пижамные", value="vue"),
            #
            # dmc.Checkbox(label="Водолазки", value="vue"),
            # dmc.Checkbox(label="Бермуды", value="vue"),
            # dmc.Checkbox(label="Туники", value="vue"),
            #
            # dmc.Checkbox(label="Дождевики", value="vue"),
            # dmc.Checkbox(label="Велосипедки", value="vue"),
            # dmc.Checkbox(label="Джеггинсы", value="vue"),
            # dmc.Checkbox(label="Парки", value="vue"),

        ],
        value=[],
        className='menu-item'
    ),
    dmc.CheckboxGroup(
        id="checkbox-group4",
        label="Размер",
        orientation="horizontal",
        offset="md",
        mb=10,
        children=[
            dmc.Checkbox(label="XXS", value="react"),
            dmc.Checkbox(label="XS", value="vue"),
            dmc.Checkbox(label="S", value="vue"),
            dmc.Checkbox(label="M", value="vue"),
            dmc.Checkbox(label="L", value="vue"),
            dmc.Checkbox(label="XL", value="vue"),
            dmc.Checkbox(label="XXL", value="vue"),
        ],
        value=[],
        className='menu-item'
    ),
    dmc.Button("Применить", style={'width': '100%'}),

],
    className='menu'
)

header = html.Header([
    dmc.Burger(id='menu', opened=False, className='burger'),
    dmc.Drawer(
        [header_accordion],
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

card = dmc.Card([
    dmc.CardSection([
        html.Div(id='top_positions_first_product_img', )
    ],
        className='img'
    ),
    html.Div([
        html.Div([
            dmc.Text(id='top_positions_first_brand', weight=700, className='card-text'),
            dmc.Text(id='top_positions_first_name', weight=500, className='card-text'),
            dmc.Text(
                id='top_positions_first_rating',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                id='top_positions_first_feedbacks_count',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                id='top_positions_first_materials',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                id='top_positions_first_description',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
        ],
            className='card-section'
        ),
        dmc.Button("Подробнее", id="modal-demo-button"),
    ],
        className='card-section2'
    ),

    dmc.Modal(
        title=wb_data.brand.iloc[0],
        id="modal-simple",
        zIndex=10000,
        children=[
            dmc.Image(
                src=wb_data.product_img.iloc[0],
                width=250,
                height=400,
            ),
            dmc.Text(wb_data.name.iloc[0], weight=500, className='card-text'),
            dmc.NavLink(wb_data.product_url.iloc[0], className='card-text'),
            dmc.Space(h=20),
            dmc.Text(
                wb_data.materials.iloc[0],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                wb_data.manufacturer_country.iloc[0],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            # dmc.Text(
            #     wb_data.season.iloc[0],
            #     size="sm",
            #     color="dimmed",
            #     className='card-text'
            # ),
            dmc.Text(
                wb_data.colors.iloc[0],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                wb_data.sizes.iloc[0],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                wb_data.description.iloc[0],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dcc.Graph(id='price_history')
        ],
    ),
],
    withBorder=True,
    className='card left-block',
)

card2 = dmc.Card([
    dmc.CardSection([
        html.Div(id='top_positions_second_product_img', )],
        className='img'
    ),
    html.Div([
        html.Div([
            dmc.Text(id='top_positions_second_brand', weight=700, className='card-text'),
            dmc.Text(id='top_positions_second_name', weight=500, className='card-text'),
            dmc.Text(
                id='top_positions_second_rating',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                id='top_positions_second_feedbacks_count',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                id='top_positions_second_materials',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                id='top_positions_second_description',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
        ],
            className='card-section'
        ),
        dmc.Button("Подробнее", id="modal-demo-button3"),
    ],
        className='card-section2'
    ),

    dmc.Modal(
        title="New Modal",
        id="modal-simple3",
        zIndex=10000,
        children=[
            dmc.Text("I am in a modal component."),
            dmc.Space(h=20),
            dmc.Group([
                dmc.Button(
                    "Close",
                    color="red",
                    variant="outline",
                    id="modal-close-button3",
                ),
            ],
                position="right",
            ),
        ],
    ),
],
    withBorder=True,
    className='card right-block',
)

cards = html.Div([
    card, card2
],
    className='container'
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
    dmc.Text("DUB Analytics | 2023")
],
    height=100,
    className='footer'
)
