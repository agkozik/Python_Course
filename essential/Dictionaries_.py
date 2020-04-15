phonebook = {'Aaa': '111-11-11', 'Bbb': '222-22-22', 'Ccc': '333-33-33'}
print(len(phonebook))

print('Bbb' in phonebook)
print(phonebook['Bbb'])
print('fdsbd' in phonebook)

# print(phonebook['df']) - Error
print('--------------------------------')
print(phonebook.get('Aaa'))
print(phonebook.get('Roma'))  # None
print(phonebook.get('Roma', '000-00-00'))  # 000-00-00

phonebook.setdefault('Ddd', '4444-44-44')  # если такого ключа нет, тогда добавляется
print(phonebook)

phonebook.setdefault('Aaa', '123-45-67')  # если указанный ключ есть, тогда значение не меняется
print(phonebook)

phonebook['Aaa'] = '000-00-00'
print(phonebook)

del phonebook['Ddd']
print(phonebook)

temp = phonebook.copy()
print(temp)

book = dict.fromkeys(['Max', 'Katya', 'Olga'], 'default value')
print(book)

b_item = phonebook.pop('Bbb')  # pop удаление с возратом значения, которое было удалено
print(b_item)
print(phonebook)

book.update({'Max': '111-11-11', 'Katya': '222-22-22', 'dsgasfgas': '7777777'})
print(book)

book.update([('Sasha ', 'fhshfd'), ('Tanya ', 'sdagfh')])
print(book)

book.clear()
print(book)

phonebook = {'A': '1', 'B': '2', 'C': '3'}
print(phonebook.keys()) #dict_keys(['A', 'B', 'C'])

print(phonebook.values()) #dict_values(['1', '2', '3'])
print(phonebook.items()) #dict_items([('A', '1'), ('B', '2'), ('C', '3')])

print(list(phonebook.keys()))

# ----------------------------------------- Iterator ------------------------------------------------------------------
for name, value in phonebook.items():
    print(name, '=', value)

my_names = phonebook.keys()
print(my_names)
phonebook['Y'] = '777'

print(phonebook)
print(my_names)

print(my_names & {'A', 'D', 'Z', 'B', 'E'})

second_phonebook = {'B': ' 23', 'age': 21, 'city': 'NY'}
print(phonebook.keys() & second_phonebook.keys())

