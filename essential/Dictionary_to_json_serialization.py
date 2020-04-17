import json

persons = [
    {
        'username': 'Rick',
        'userlastname': 'Smith'
    },
    {
        'username': 'Bet',
        'userlastname': 'Smith'
    },
    {
        'username': 'Morty',
        'userlastname': 'Smith'
    },
    {
        'username': 'Jerry',
        'userlastname': 'Smith'
    }
]

with open('../resources/persons.json', 'w') as file:
    json.dump(persons, file, indent=2)
