value1 = 'Smith'
value2 = input("What is your name?")
print("Welcome ", value2, value1)

# строковые литералы, экранирование (\s) перенос строки (\n) и объединение строк (\)
string = "String\'s 1.\n" \
         "String\'s 1 next"
print(string)

# многострочные строки с сохранением форматирования
multiline_string = """
Set. Multi String
as Json example.
With different lines"""
print(multiline_string)

print('\' \' ')
multiline_string2 = '''
Set. Multi String
as Json example.
With different lines'''
print(multiline_string)

# Форматированный ввод
string1 = 'Number = %d' % 1
print(string1)

string2 = 'Number = %f' % 2
print(string2)

string3 = '%s = %d' % ('number', 3)
print(string3)

string4 = 'Number ={}'.format(4)
print(string4)

string5 = 'Number ={}'.format(5.0)
print(string5)

string6 = 'Number ={:5.2f}'.format(6)
print(string6)

string7 = '{}={}'.format('number', 7)
print(string7)

string8 = '{0}={1}'.format('number', 8)
print(string8)

string9= '{1}={0}'.format('number', 9)
print(string9)