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