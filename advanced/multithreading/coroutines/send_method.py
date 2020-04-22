import functools


def is_divider(number):
    print('Coroutine started:')
    while True:
        # ожидаем число, которое должно прийти через метод send
        value = yield
        # если число является делителем числа number, тогда печатаем число
        if number % value == 0:
            print(value)


cor = is_divider(100)
# запуск через передачу None
cor.send(None)
cor.send(10)
cor.send(11)
cor.send(20)
cor.close()


# для того, чтобы каждый раз не писать cor.send(None), пишут декоратор:
def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res.send(None)
        return res

    return wrapper


@coroutine
def is_divider_cor(number):
    print("Coroutine started:")
    while True:
        value = yield
        if number % value == 0:
            print(value)


cor = is_divider_cor(100)
cor.send(10)
