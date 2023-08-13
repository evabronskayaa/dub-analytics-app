import pandas as pd
import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36',
    'sec-ch-ua': 'Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
}


def get_response(url: str):
    response = requests.get(url=url, headers=headers)
    return response.json()


def prepare_items(response):
    products = []
    products_raw = response.get('data', {}).get('products', None)

    if len(products_raw) > 0:
        for product in products_raw:
            product_id = product['id']
            img_urls, orders_count, product_card_info, feedback_response, price_history_response = get_product_info(product_id)
            category_2 = product_card_info['subj_name']
            stop_category_2 = ['Банданы', 'Бейсболки', 'Ботильоны', 'Ботинки', 'Бусы', 'Кольца', 'Комбинезоны рабочие',
                               'Кошельки', 'Кроссовки', 'Лаки для ногтей', 'Панамы', 'Полусапожки', 'Плавки', 'Приправы',
                               'Ремни', 'Рюкзаки', 'Сандалии', 'Сапоги', 'Серьги', 'Лоферы', 'Солнцезащитные очки',
                               'Сумки', 'Туалетная вода', 'Цепочки', 'Чехлы для стилусов', 'Шапки', 'Шарфы', 'Шлепанцы',
                               'Мониторы', 'Бумажные салфетки', ]

            if category_2 not in stop_category_2:
                products.append({
                    'brand_id': product['brandId'],
                    'brand': product['brand'],
                    'category_1': product_card_info['subj_root_name'],
                    'category_2': product_card_info['subj_name'],
                    'product_id': product['id'],
                    'product_img': img_urls,
                    'product_url': f"https://www.wildberries.ru/catalog/{product['id']}/detail.aspx",
                    'name': product['name'],
                    'gender': product_card_info['kinds'][0] if 'kinds' in product_card_info else None,
                    'description': product_card_info['description'] if 'description' in product_card_info else None,
                    'additional_info': product_card_info['grouped_options'][0]['options'],
                    'materials': product_card_info['compositions'] if 'compositions' in product_card_info else None,
                    'season': product_card_info['season'] if 'season' in product_card_info else None,
                    'colors': product_card_info['nm_colors_names'] if 'nm_colors_names' in product_card_info else None,
                    'sizes': product['sizes'],
                    'sale (%)': product['sale'],
                    'price': float(product['priceU']) / 100,
                    'sale_price': float(product['salePriceU']) / 100,
                    'price_history': price_history_response,
                    'rating': product['reviewRating'],
                    'feedbacks_count': product['feedbacks'],
                    'feedbacks_info': feedback_response,
                    'purchases_count': orders_count,
                    'volume': product['volume'],
                })

    return products


def match_basket(short_id: int):
    basket_dict = {
        range(0, 144): '01',
        range(144, 288): '02',
        range(288, 432): '03',
        range(432, 720): '04',
        range(720, 1008): '05',
        range(1008, 1062): '06',
        range(1062, 1116): '07',
        range(1116, 1170): '08',
        range(1170, 1314): '09',
        range(1314, 1602): '10',
        range(1602, 1656): '11',
        range(1656, 1920): '12'
    }

    for key in basket_dict:
        if short_id in key:
            return basket_dict[key]

    return '13'


def get_basket_id(short_id: int) -> str:
    basket = match_basket(short_id=short_id)
    return basket


def generate_image_urls(product_id: int, short_id: int, basket: str) -> list:
    img_urls = []
    for i in range(1, 4):
        url = f'https://basket-{basket}.wb.ru/vol{short_id}/part{product_id // 1000}/{product_id}/images/big/{i}.jpg'
        img_urls.append(url)

    return img_urls


def get_card_info_and_orders_count(product_id: int, short_id: int, basket: str) -> tuple:
    card_info_url = f'https://basket-{basket}.wb.ru/vol{short_id}/part{product_id // 1000}/{product_id}/info/ru/card.json'
    card_info = requests.get(url=card_info_url, headers=headers).json()

    nm_id = card_info['nm_id']
    orders_count = requests.get(url=f'https://product-order-qnt.wildberries.ru/by-nm/?nm={nm_id}').json()[0]['qnt']

    return card_info, orders_count


def get_feedbacks(product_id: int) -> dict or None:
    feedback_url = f'https://feedbacks1.wb.ru/feedbacks/v1/{product_id}'
    feedback_response = requests.get(url=feedback_url, headers=headers)

    return feedback_response.json()['feedbacks'] if feedback_response.status_code == 200 else None


def get_price_history(product_id: int, short_id: int, basket: str) -> dict or None:
    price_history_url = f'https://basket-{basket}.wb.ru/vol{short_id}/part{product_id // 1000}/{product_id}/info/price-history.json'
    price_history_response = requests.get(url=price_history_url, headers=headers)

    return price_history_response.json() if price_history_response.status_code == 200 else None


def get_product_info(product_id: int) -> tuple:
    short_id = product_id // 100000

    basket = get_basket_id(short_id)
    img_urls = generate_image_urls(product_id, short_id, basket)
    card_info, orders_count = get_card_info_and_orders_count(product_id, short_id, basket)
    feedbacks = get_feedbacks(product_id)
    price_history = get_price_history(product_id, short_id, basket)

    return img_urls, orders_count, card_info, feedbacks, price_history


def get_data(brands: list):
    regions = '80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114'
    urls = [
        f'https://catalog.wb.ru/brands/l/catalog?appType=1&brand={brand}&limit=300&curr=rub&dest=-1257786'
        f'&page={i}&regions={regions}&sort=popular&spp=0'
        for brand in brands
        for i in range(1, 2)
    ]

    all_products = []
    for url in urls:
        response = get_response(url=url)
        products = prepare_items(response=response)
        all_products.extend(products)

    df = pd.DataFrame(all_products)

    file_path = '../../data/wb_products.csv'
    df.to_csv(file_path, index=False, header=True)


if __name__ == '__main__':
    brands = {
        'lime': 20246, 'befree': 4126, 'pull&bear': 158986, 'bershka': 106259
    }

    get_data(brands=[*brands.values()])
