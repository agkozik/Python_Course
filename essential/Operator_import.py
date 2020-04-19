# замена знака числа на противоположный
from operator import neg

values = [5, 2, 1, 3, -7]
# print(list(map(lambda x: -x, values)))
print(list(map(neg, values)))

from operator import add, sub, mul, truediv
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

def calculator():
    first = float(input('Enter first number: '))
    operator = input('Enter an operator (a sign): ')
    second = float(input('Enter a second number: '))

    result = operations[operator](first, second)
    print(result)

calculator()