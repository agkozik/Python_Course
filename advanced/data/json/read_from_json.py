import json

# json_data = '{"name": "Alex", "type": "Animal", "age": 5, "hobbies": ["guitar", "cars", "girls"]}'
json_data = """{
    "name": "Alex",
    "type": "Animal",
    "age": 5,
    "hobbies": [
        "guitar",
        "cars",
        "girls"
    ]
}"""

# загрузить json из строки и получить словарь
print('# загрузить json из строки и получить словарь')
data = json.loads(json_data)
print(data)

# запись в файл json
print('# запись в файл json')
with open('json_data/newfile.json', 'w') as file:
    data = json.dump(data, file, indent=4)

# чтение из файла json
print('# чтение из файла json')
with open('json_data/newfile.json', 'r') as file:
    print(json.load(file))

# для того чтобы сериализовать дату необходимо использовать hook

