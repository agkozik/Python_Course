import json

data = {
    'name': 'Alex',
    'type': 'Animal',
    'age': 5,
    'hobbies': [
        'guitar',
        'cars',
        'girls'
    ]
}
# dumps: 'dump to string' возвращает строку
json_data = json.dumps(data)
print(json_data)

with open('json_data/output.json', 'w') as json_file:
# data - какие данные, json_file - куда отправить, indent - количество пробелов слева (отступы)
    json.dump(data, json_file, indent=4)