import pandas as pd

from data_preprocessing import get_materials, get_sizes, get_manufacturer, get_color

outerwear = ['Ветровки', 'Дождевики', 'Дубленки', 
             'Жилеты утепленные', 'Куртки', 'Пальто', 
             'Парки', 'Плащи', 'Пуховики', 'Тренчкоты']

wb_data = pd.read_csv('../data/wb_products.csv')

wb_data = wb_data[wb_data.category1 == 'Одежда'].reset_index(drop=True)
wb_data.loc[wb_data.category2.isin(outerwear), 'category2'] = 'Верхняя одежда'
wb_data.rename(columns={'name': 'product_name'}, inplace=True)

wb_data['product_url'] = wb_data.product_id.apply(lambda x: f'https://www.wildberries.ru/catalog/{x}/detail.aspx')
wb_data['orders_count_str'] = wb_data.orders_count.apply(lambda x: f'Купили более {x} раз')
wb_data['feedbacks_count_str'] = wb_data.feedbacks_count.apply(lambda x: f'Количество отзывов: {x if x == x else "0"}')
wb_data['rating_str'] = wb_data.rating.apply(lambda x: f'Рейтинг: {str(x)+"☆" if x == x else "отсутствует"}')
wb_data['volume_str'] = wb_data.volume.apply(lambda x: f'Осталось товаров на складе: {x} шт.' if x == x else 'Остатки не указаны')
wb_data['description'] = wb_data.description.apply(lambda x: f'Описание: {x}' if x == x else 'Описание отсутствует')
wb_data['materials'] = wb_data.materials.apply(get_materials)
wb_data['sizes_str'] = wb_data.sizes.apply(get_sizes)
wb_data['manufacturer_country'] = wb_data.additional_info.apply(get_manufacturer)
wb_data['colors'] = wb_data.colors.apply(get_color)

wb_data['feedback_complete_info'] = wb_data.feedbacks_info.apply(lambda x: [{'createDate': i.get('createDate'),
                                                                             'rank': i.get('rank'),
                                                                             'size': i.get('size'),
                                                                             'color': i.get('color'),
                                                                             'text': i.get('text')} 
                                                                             for i in eval(x)] 
                                                                             if x == x else None)


