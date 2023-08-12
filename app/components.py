from dash import html, dash, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

header_accordion = dmc.Accordion(
    children=[
        dmc.AccordionItem([
            dmc.AccordionControl('FAQ'),
            dmc.AccordionPanel([
                dmc.Accordion([
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl('Для чего это приложение?'),
                            dmc.AccordionPanel(
                                'Это приложение разработано для компании DUB, '
                                'чтобы исследовать тенденции в одежде и '
                                'анализировать продукты конкурентов'
                            ),
                        ],
                        value="for-what",
                    ),
                    dmc.AccordionItem(
                        [
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
        dmc.AccordionItem(
            [
                dmc.AccordionControl('Developers'),
                dmc.AccordionPanel([
                    dmc.Accordion([
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl('Elena Gibina'),
                                dmc.AccordionPanel(
                                    'Web-developer, Data Analyst'
                                ),
                            ],
                            value="elena",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl('Eva Bronskaya'),
                                dmc.AccordionPanel(
                                    'Web-developer, Data Analyst'
                                ),
                            ],
                            value="eva",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl('Denis Nikitin'),
                                dmc.AccordionPanel(
                                    'Data Analyst'
                                ),
                            ],
                            value="denis",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl('Artur Fattakhov'),
                                dmc.AccordionPanel(
                                    'Data Analyst'
                                ),
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


