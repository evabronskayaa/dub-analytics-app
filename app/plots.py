import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def draw_indicator(dates_data: list, prices_data: list):
    current_price = prices_data[-1]
    ref_price = prices_data[-2]
    max_price = int(max(prices_data) * 1.3)

    plot_width = 400
    plot_height = 300

    number_font_size = int(0.00052 * plot_width * plot_height)
    delta_font_size = int(0.00012 * plot_width * plot_height)
    title_font_size = int(0.00016 * plot_width * plot_height)
    tick_font_size = int(0.00011 * plot_width * plot_height)

    font_family = 'https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100&display=swap'
    font_color = '#585858'
    line_color = "#F69F97"

    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=current_price,
        number={'suffix': " р",
                'font_size': number_font_size},
        delta={'reference': ref_price,
               'font_size': delta_font_size},
        title={"text": "цена",
               'font_size': title_font_size},
    ))
    fig.add_trace(go.Scatter(
        y=prices_data,
        x=dates_data,
        mode='lines',
        line=dict(color=line_color),
        fill='tozeroy',
        fillcolor='rgba(255, 0, 0, 0.1)',
        hovertemplate='<br>Дата: %{x} <br>Цена: %{y} р<extra></extra>',
    ))
    fig.update_xaxes(
        mirror=True,
        showline=True,
        gridcolor='white',
        tickfont=dict(size=tick_font_size),
        showticklabels=True
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        gridcolor='white',
        tickfont=dict(size=tick_font_size),
        range=[0, max_price],
    )
    fig.update_layout(
        # width=plot_width,
        height=plot_height,
        font_color=font_color,
        font_family=font_family,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig


def draw_piechart(gender_stats: pd.DataFrame):
    plot_height = 300
    plot_width = 500

    font_family = 'https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100&display=swap'
    font_color = '#000000'
    title_font_size = 17
    legend_font_size = 12

    fig = px.pie(
        gender_stats,
        values='count_items',
        names='gender',
        color_discrete_sequence=['#F69F97', '#E04F4F'],
        title='Доля каждого пола во всех SKU'
    )

    fig.update_layout(
        width=plot_width,
        height=plot_height,
        legend_traceorder="reversed",
        title={'font_size': title_font_size, 
               'xanchor': 'center', 
               'x': 0.5, },
        legend={
            'y': 0.99,
            'x': 0.01,
            'xanchor': 'left',
            'yanchor': 'top',
            'font_size': legend_font_size
        },
        font_family=font_family,
        font_color=font_color,
        margin=dict(l=20, r=20, b=20)
    )
    return fig


def draw_barchart(df: pd.DataFrame, index: str, title=None):
    plot_height = 300

    font_family = 'https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100&display=swap'
    font_color = '#000000'
    bar_colors = ['#E04F4F', 
                  '#FB625E', 
                  '#F1937A', 
                  '#F69F97', 
                  '#FACBC7', 
                  '#FBDEDA', 
                  '#D8F931']
    title_font_size = 17

    fig = px.bar(
        df,
        x=index,
        y='count_items',
        color=index,
        color_discrete_sequence=bar_colors,
        title=title,
        text_auto=True,
        width=500,
        height=350
    )

    fig.update_traces(
        textfont_color='white'
    )

    fig.update_layout(
        height=plot_height,
        showlegend=False,
        yaxis={'visible': False},
        xaxis={'title': None,
               'visible': True,
               'showticklabels': True},
        title={'font_size': title_font_size, 'xanchor': 'center', 'x': 0.5},
        font_family=font_family,
        font_color=font_color,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=20, r=20, b=20),
    )

    return fig
