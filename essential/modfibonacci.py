# модуль по работе с числами фибоначчи:
# генерирует числа


def fibonacci_sequence():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second


# выдает за n количество раз число фибоначи
def fibonacci(limit):
    generator = fibonacci_sequence()
    for _ in range(limit):
        yield next(generator)


# получение числа по номеру
def n_fibonacci(number):
    result = None
    for current in fibonacci(number):
        result = current
    return result

print('Running fibonacci test:')
assert n_fibonacci(1) == 1
assert n_fibonacci(2) == 1
assert n_fibonacci(3) == 2
assert n_fibonacci(4) == 3
assert n_fibonacci(5) == 5
print('End fibonacci test')
