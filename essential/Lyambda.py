# Calculator
# создаем словарь с методом вместо значения
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: pow(x, y)
}

try:
    first = float(input('Enter first number: '))
    sign = input('Enter operation: ')
    second = float(input('Enter second number'))
    result = operations[sign](first, second) #обращаемся к словарю по значению и передаем в метод (first, second)
except ValueError as er:
    print('Incorrect input: ', er)
except KeyError as ker:
    print('Unsupported operation: ', ker)
except ZeroDivisionError as der:
    print('Division by zero', der)
else:
    print('Result: ', result)