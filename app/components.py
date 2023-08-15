from dash import html, dash, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from data import wb_data

header_accordion = dmc.Accordion(
    children=[
        dmc.AccordionItem([
            dmc.AccordionControl('FAQ'),
            dmc.AccordionPanel([
                dmc.Accordion([
                    dmc.AccordionItem([
                        dmc.AccordionControl('Для чего это приложение?'),
                        dmc.AccordionPanel(
                            'Это приложение разработано для компании DUB, '
                            'чтобы исследовать тенденции в одежде и '
                            'анализировать продукты конкурентов'
                        ),
                    ],
                        value="for-what",
                    ),
                    dmc.AccordionItem([
                        dmc.AccordionControl('Второй вопрос я не придумала'),
                        dmc.AccordionPanel('пук'),
                    ],
                        value="none",
                    ),
                ],
                    variant='filled',
                )
            ]),
        ],
            value="faq",
        ),
        dmc.AccordionItem([
            dmc.AccordionControl('Developers'),
            dmc.AccordionPanel([
                dmc.Accordion([
                    dmc.AccordionItem([
                        dmc.AccordionControl('Elena Gibina'),
                        dmc.AccordionPanel('Web-developer, Data Analyst'),
                    ],
                        value="elena",
                    ),
                    dmc.AccordionItem([
                        dmc.AccordionControl('Eva Bronskaya'),
                        dmc.AccordionPanel('Web-developer, Data Analyst'),
                    ],
                        value="eva",
                    ),
                    dmc.AccordionItem([
                        dmc.AccordionControl('Denis Nikitin'),
                        dmc.AccordionPanel('Data Analyst'),
                    ],
                        value="denis",
                    ),
                    dmc.AccordionItem([
                        dmc.AccordionControl('Artur Fattakhov'),
                        dmc.AccordionPanel('Data Analyst'),
                    ],
                        value="artur",
                    ),
                ],
                    variant='filled',
                )
            ]),
        ],
            value="developers",
        ),
    ],
    variant='filled',
)

header = html.Header([
    dmc.Burger(id='menu', opened=False, className='burger'),
    dmc.Drawer(
        [header_accordion],
        id='drawer-menu',
        title='Меню',
        padding='md',
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
        dmc.Image(
            src=wb_data.product_img.iloc[0],
            width=250,
            height=400,
        )],
        className='img'
    ),
    html.Div([
        html.Div([
            dmc.Text(wb_data.brand.iloc[0], weight=700, className='card-text'),
            dmc.Text(wb_data.name.iloc[0], weight=500, className='card-text'),
            dmc.Text(
                wb_data.materials.iloc[0],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                wb_data.description.iloc[0][:200] + '...',
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
        dmc.Image(
            src=wb_data.product_img.iloc[2],
            width=250,
            height=400,
            className=''
        )],
        className='img'
    ),
    html.Div([
        html.Div([
            dmc.Text(wb_data.brand.iloc[2], weight=700, className='card-text'),
            dmc.Text(wb_data.name.iloc[2], weight=500, className='card-text'),
            dmc.Text(
                wb_data.materials.iloc[2],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                wb_data.description.iloc[2][:200] + '...',
                size="sm",
                color="dimmed",
                className='card-text'
            ),
        ],
            className='card-section'
        ),
        dmc.Button("Подробнее", id="modal-demo-button2"),
    ],
        className='card-section2'
    ),

    dmc.Modal(
        title="New Modal",
        id="modal-simple2",
        zIndex=10000,
        children=[
            dmc.Text("I am in a modal component."),
            dmc.Space(h=20),
            dmc.Group([
                dmc.Button(
                    "Close",
                    color="red",
                    variant="outline",
                    id="modal-close-button2",
                ),
            ],
                position="right",
            ),
        ],
    ),
],
    withBorder=True,
    className='card center-block',
)

card3 = dmc.Card([
    dmc.CardSection([
        dmc.Image(
            src=wb_data.product_img.iloc[3],
            width=250,
            height=400,
            className=''
        )],
        className='img'
    ),
    html.Div([
        html.Div([
            dmc.Text(wb_data.brand.iloc[3], weight=700, className='card-text'),
            dmc.Text(wb_data.name.iloc[3], weight=500, className='card-text'),
            dmc.Text(
                wb_data.materials.iloc[3],
                size="sm",
                color="dimmed",
                className='card-text'
            ),
            dmc.Text(
                wb_data.description.iloc[3][:200] + '...',
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
    card, card2, card3
],
    className='container'
)

competitors_offers = html.Div([
    dmc.Text('Топ-10 предложений конкурентов', className='block-title'),
    cards,
    dmc.Pagination(total=5, siblings=1, page=1, radius=0, color='#000000', withControls=True, withEdges=True,
                   style={'float': 'right'}),
],
    className='offers'
)
