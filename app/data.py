import pandas as pd

from data_preprocessing import get_materials

wb_data = pd.read_csv('../data/wb_products.csv')

wb_data = wb_data[wb_data.category1 == 'Одежда'].reset_index(drop=True)

wb_data['materials'] = wb_data.materials.apply(lambda x: get_materials(x))
wb_data['size_letter'] = wb_data.sizes.apply(lambda x: eval(x)[0].get('origName').upper())
wb_data['size_name'] = wb_data.sizes.apply(lambda x: eval(x)[0].get('name').upper())

wb_data['feedback_complete_info'] = wb_data.feedbacks_info.apply(lambda x: [{'createDate': i.get('createDate'),
                                                                             'rank': i.get('rank'),
                                                                             'size': i.get('size'),
                                                                             'color': i.get('color'),
                                                                             'text': i.get('text')} 
                                                                             for i in eval(x)] 
                                                                             if x == x else None)



