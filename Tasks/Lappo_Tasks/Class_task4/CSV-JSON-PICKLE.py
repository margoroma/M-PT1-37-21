import csv
import os
import json
import pickle

os.chdir("d:\\PYTHON-IT-AK\\GitHub\\M-PT1-37-21\\Tasks\\Lappo_Tasks\\Class_task4\\")
print(os.getcwd())


with open("d:\\PYTHON-IT-AK\\GitHub\\M-PT1-37-21\\Tasks\\Lappo_Tasks\\Class_task4\\cars.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Model", "Year", "Horsepower", "Engine size"])
    writer.writerow(["80 1.6 Specs", "1989", "69", "1595 cm3 (97.3 cu-in)"])
    writer.writerow(["80 1.9 E Specs", "1986", "113", "1847 cm3 (112.7 cu-in)"])
    writer.writerow(["80 2.0 16v Quatro Specs", "1990", "140", "1984 cm3 (121.1 cu-in)"])

count=0
csv_rows=list()
csv_header=list()

# with open("cars.csv", "r", newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     for x in reader:
#         if count == 0:
#             csv_header=x
#             #csv_header.append(x)
#         else:
#             csv_rows.append(x)
#         count += 1

super_dic=dict()

with open('cars.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    for x in reader:                                     
        for key in x:                               
            try:
               super_dic[key] = super_dic[key] + ', '+ x[key]       
            except KeyError:                                   
                super_dic[key] = x[key]   

print(super_dic)


with open('cars.json', 'w') as f:
    json.dump(super_dic, f)


with open('cars.json', "r") as f:
    json_load=json.load(f)

with open("pickle_file.txt", "wb") as f:
    pickle.dump(json_load, f)