from dash import html, dash, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


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
                children=[
                    dmc.Checkbox(label="Брюки", value="Брюки"),
                    dmc.Checkbox(label="Джинсы", value="Джинсы"),
                    dmc.Checkbox(label="Платья", value="Платья"),
                    dmc.Checkbox(label="Топы", value="Топы"),
                    dmc.Checkbox(label="Футболки", value="Футболки"),
                    dmc.Checkbox(label="Юбки", value="Юбки"),
                    dmc.Checkbox(label="Блузки", value="Блузки"),
                    dmc.Checkbox(label="Верхняя одежда", value="Верхняя одежда"),
                    # dmc.Checkbox(label="Пальто", value="Пальто"),
                    # dmc.Checkbox(label="Куртки", value="Куртки"),
                    dmc.Checkbox(label="Шорты", value="Шорты"),
                    dmc.Checkbox(label="Рубашки", value="Рубашки"),
                    dmc.Checkbox(label="Свитеры", value="Свитеры"),
                    dmc.Checkbox(label="Блузки-боди", value="Блузки-боди"),
                    dmc.Checkbox(label="Кардиганы", value="Кардиганы"),
                    dmc.Checkbox(label="Толстовки", value="Толстовки"),
                    dmc.Checkbox(label="Пуловеры", value="Пуловеры"),
                    dmc.Checkbox(label="Комбинезоны", value="Комбинезоны"),
                    dmc.Checkbox(label="Блейзеры", value="Блейзеры"),
                    # dmc.Checkbox(label="Дубленки", value="Дубленки"),
                    dmc.Checkbox(label="Леггинсы", value="Леггинсы"),
                    # dmc.Checkbox(label="Плащи", value="Плащи"),
                    # dmc.Checkbox(label="Пуховики", value="Пуховики"),
                    dmc.Checkbox(label="Пиджаки", value="Пиджаки"),
                    dmc.Checkbox(label="Рубашки пижамные", value="Рубашки пижамные"),
                    dmc.Checkbox(label="Бомберы", value="Бомберы"),
                    dmc.Checkbox(label="Лонгсливы", value="Лонгсливы"),
                    # dmc.Checkbox(label="Тренчкоты", value="Тренчкоты"),
                    dmc.Checkbox(label="Жилеты", value="Жилеты"),
                    # dmc.Checkbox(label="Ветровки", value="Ветровки"),
                    dmc.Checkbox(label="Полукомбинезоны", value="Полукомбинезоны"),
                    dmc.Checkbox(label="Джемперы", value="Джемперы"),
                    dmc.Checkbox(label="Худи", value="Худи"),
                    dmc.Checkbox(label="Футболки-поло", value="Футболки-поло"),
                    dmc.Checkbox(label="Свитшоты", value="Свитшоты"),
                    dmc.Checkbox(label="Жакеты", value="Жакеты"),
                    # dmc.Checkbox(label="Жилеты утепленные", value="Жилеты утепленные"),
                    dmc.Checkbox(label="Сарафаны", value="Сарафаны"),
                    dmc.Checkbox(label="Брюки пижамные", value="Брюки пижамные"),
                    dmc.Checkbox(label="Шорты пижамные", value="Шорты пижамные"),
                    dmc.Checkbox(label="Водолазки", value="Водолазки"),
                    dmc.Checkbox(label="Бермуды", value="Бермуды"),
                    dmc.Checkbox(label="Туники", value="Туники"),
                    # dmc.Checkbox(label="Дождевики", value="Дождевики"),
                    dmc.Checkbox(label="Велосипедки", value="Велосипедки"),
                    dmc.Checkbox(label="Джеггинсы", value="Джеггинсы"),
                    # dmc.Checkbox(label="Парки", value="Парки"),
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
