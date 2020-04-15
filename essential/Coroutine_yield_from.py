# -------------- вариант реализации до v3.4(yield from):---------------------------------------------------------------
# консьюмер забирает данные из продюсера и выдает их сумму и среднее значение
import random
import time


def sleep(wait_seconds):
    start = time.time()
    while time.time() - start < wait_seconds:
        yield


def producer():
    yield from sleep(0.5)
    data = random.randint(1, 100)
    return data


def consume():
    summa = 0
    count = 0

    while True:
        data = yield from producer()
        print('Data = ', data)
        summa += data
        count += 1
        print('Sum: ', summa)
        print('Average: ', summa / count)
        print('---------------------------------------------------------------------------------')


if __name__ == '__main__':
    consumer = consume()
    while True:
        next(consumer)
# ---------------------------------------------------------------------------------------------------------------------