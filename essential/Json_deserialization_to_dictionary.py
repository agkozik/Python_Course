import json
with open('../resources/persons.json') as data:
    persons = json.load(data)

print(persons)