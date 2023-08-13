import pandas as pd
from datetime import datetime, date 

def get_pivot_nunique_stats(df:pd.DataFrame,
                            index:str) -> pd.DataFrame:
    
    temp = df.groupby(index)[['product_id']]\
        .nunique()\
        .reset_index()\
        .rename(columns={'product_id':'count_items'})\
        .sort_values(by='count_items', ascending=False)
    
    return temp

def get_price_history_data(current_price:int,
                           price_history:list) -> (list, list):
    
    price_history = [{'dt': datetime.fromtimestamp(pair['dt']),
                 'price': pair['price']['RUB'] / 100} for pair in price_history]
    
    dates_data = [x['dt'] for x in price_history]
    prices_data = [x['price'] for x in price_history]

    dates_data.append(date.today())
    prices_data.append(current_price)

    return dates_data, prices_data