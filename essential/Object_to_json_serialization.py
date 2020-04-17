import json


class Person(object):
    def __init__(self, name, lastname):
        self.username = name
        self.userlastname = lastname

    def to_json(self):
        #return {'username': self.username, 'userlastname': self.userlastname}
        return self.__dict__


persons = [Person('john', 'Sigal'), Person('kate', 'snifferson')]

with open('../resources/users.json', 'w') as file:
    json.dump(persons, file, indent=2, default=Person.to_json)
