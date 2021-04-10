import csv
import json
import pickle
import pandas as pd
from IPython.display import display

############################## Вывод pandas dataframe
"""
df = pd.read_csv('audi_a4_csv.csv', sep=';', error_bad_lines=False) # для просмотра данных в виде таблицы
display(df)
df.columns
df.shape
df.to_json('pandas_json.json')
"""
########################### Чтение и запись из csv в json
"""
with open('audi_a4.csv', 'r') as f:
    reader = csv.DictReader( f, fieldnames = ( "Model","Year","Horsepower","Engine size" ) )
    out = [ row for row in reader ]
with open('dic_js.json', 'w') as ff:
    json.dump( out , ff)
"""
########################### конвертировать из json в pd
"""
# with open("pandas_json.json") as datafile: 
#     data = json.load(datafile)
    
# #print(data)
# print(data["Model"]) 
# dataframe = pd.DataFrame(data)
# print(dataframe)
"""
########################### Формирование словаря из пар ключ-значение, запись в json и pickle
with open('audi_a4.csv', "r") as f: 
    reader = csv.reader(f)
    res = {}
    for row in reader:
        key = row[0]
        res[key] = row[1:]
    # print(type(res)) 
    # print(res)
with open("audi_a4_____.json", "w") as f_js:
    json.dump(res, f_js)
with open("audi_a4.pick_____", "wb") as f_pick:
    pickle.dump(res, f_pick) 

print(res["80 1.9 E Quattro Specs"]) # вызов по ключу   
 
