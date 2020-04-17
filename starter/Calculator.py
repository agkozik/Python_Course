x = float(input('Input first number: '))
y = float(input('Input Second number: '))
operation = input('Input Operation: (+, -, *, /): ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print('Wrong Operation')

if result is not None:
    print('Result: = ', result)
