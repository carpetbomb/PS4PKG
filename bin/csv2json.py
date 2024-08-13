import csv
import json
 
def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Title']
            data[key] = rows
 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

def make_json2(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Title ID']
            data[key] = rows
 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))         
 

make_json("./bin/cache/list.csv", "./bin/cache/list.json")
print('converted /bin/cache/list.csv to bin/cache/list.json')

make_json2("./bin/cache/list_cid.csv", "./bin/cache/list_cid.json")
print('converted /bin/cache/list_cid.csv to bin/cache/list_cid.json')