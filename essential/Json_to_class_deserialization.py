import json


class Person(object):
    def __init__(self, name, lastname):
        self.username = name
        self.userlastname = lastname

    def to_json(self):
        return self.__dict__

    @classmethod
    def get_from_json(cls, js_object):
        return cls(js_object['username'], js_object['userlastname'])

    def __repr__(self):
        return 'Person({!r}, {!r})'.format(self.username, self.userlastname)


with open('../resources/persons.json') as data:
    persons = json.load(data, object_hook=Person.get_from_json)

print(persons)
