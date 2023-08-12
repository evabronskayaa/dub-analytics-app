import pandas as pd
import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://www.lamoda.ru',
    'Referer': 'https://www.lamoda.ru/',
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
    products_raw = response['payload']['products']

    if len(products_raw) > 0:
        for product in response['payload']['products']:
            product_id = product['sku']
            product_response = get_product_info(product=product_id)

            products.append({
                'brand_id': product_response['brand']['id'],
                'brand': product_response['brand']['title'],
                'category_1': product_response['breadcrumbs'][1]['label'],
                'category_2': product_response['breadcrumbs'][2]['label'],
                'product_id': product_response['sku'],
                'product_img': ['https://a.lmcdn.ru/img600x866' + photo for photo in product_response['gallery']],
                'product_url': f"https://www.lamoda.ru/api/v1/product/get?sku={product_response['sku']}&is_hybrid_supported=false",
                'name': product_response['title'],
                'gender': product_response['gender'],
                'description': product_response['seo_title'],
                'season': product_response['attributes'][3]['value'],
                'collection': product_response['collection'],
                'materials': product_response['attributes'][1]['value'],
                'colors': product_response['attributes'][4]['value'],
                'print': product_response['attributes'][5]['value'],
                'sizes': product_response['sizes'][0],
                'sale (%)': product_response['discount'] if 'discount' in response else None,
                'price': product_response['price'],
                'old_price': product_response['old_price'] if 'old_price' in response else None,
                'rating': product_response['average_rating'],
                'feedbacks_count': product_response['counters']['reviews'],
                'feedbacks_info': product_response['reviews'],
                'questions': product_response['counters']['questions'],
                'photo_reviews': product_response['counters']['photoreviews'],
                'buy_per_day': product_response['counters']['buy_per_day'],
                'buy_per_week': product_response['counters']['buy_per_week'],
                'view_per_day': product_response['counters']['view_per_day'],
                'view_per_week': product_response['counters']['view_per_week'],
                'is_in_stock': product_response['is_in_stock'],
            })

    return products


def get_product_info(product: str):
    url = f'https://www.lamoda.ru/api/v1/product/get?sku={product}&is_hybrid_supported=false'
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_data(brands: list):
    all_products = []
    urls = [
        f'https://www.lamoda.ru/b/{brand}/brand-lime/?genders=women&limit=300&json=1'
        for brand in brands
    ]

    for url in urls:
        print(url)
        response = get_response(url=url)
        products = prepare_items(response=response)
        all_products.extend(products)

    df = pd.DataFrame(all_products)

    file_path = '../../data/lamoda_products.csv'
    df.to_csv(file_path, index=False, header=True)


if __name__ == '__main__':
    brands = {
        'lime': 27369,
        'befree': 22318
    }

    get_data(brands=[*brands.values()])
