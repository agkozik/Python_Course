# --------------старый вариант реализации (yield-send):-----------------------------------------------------------------
# генератор выжидает wait_seconds и гененирует случайные числа от 1 до 100,
# а консьюмер получает эти данные и выдает их сумму и среднее значение
import random
import time


def sleep(wait_seconds):
    start = time.time()
    while time.time() - start < wait_seconds:
        yield


def producer(consumer):
    while True:
        yield from sleep(0.5)
        data = random.randint(1, 100)
        consumer.send(data)


def consume():
    summa = 0
    count = 0

    while True:
        data = yield
        print('Data = ', data)
        summa += data
        count += 1
        print('Sum: ', summa)
        print('Average: ', summa / count)
        print('---------------------------------------------------------------------------------')


if __name__ == '__main__':
    consumer = consume()
    next(consumer)

    producer = producer(consumer)
    while True:
        next(producer)
# ---------------------------------------------------------------------------------------------------------------------