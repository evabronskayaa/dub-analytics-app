import pandas as pd

from data_preprocessing import get_materials

wb_data = pd.read_csv('../data/wb_products.csv')

wb_data['materials_'] = wb_data.materials.apply(lambda x: get_materials(x))

