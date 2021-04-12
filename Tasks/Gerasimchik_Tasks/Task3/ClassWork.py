import csv, json, pickle

with open('cars.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    row = list(reader)
    print(row)
with open('cars.json', 'w') as f_j:
    json.dump(row, f_j)
with open('cars.bin', 'wb') as f_p:
    pickle.dump(row, f_p)

with open('cars.json', 'r') as f_j:
    json_file = json.load(f_j)
    print(json_file)
    for i in json_file:
        headers = list(i.keys())
with open('cars_from_json.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')
    writer.writeheader()
    writer.writerows(json_file)
with open('cars_from_json.bin', 'wb') as f_p:
    pickle.dump(json_file, f_p)

with open('cars.bin', 'rb') as f_p:
    pickle_file = pickle.load(f_p)
    print(pickle_file)
for i in pickle_file:
    headers = list(i.keys())
with open('cars_from_pickle.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')
    writer.writeheader()
    writer.writerows(pickle_file)
with open('cars_from_pickle.json', 'w') as f_j:
    json.dump(pickle_file, f_j)
