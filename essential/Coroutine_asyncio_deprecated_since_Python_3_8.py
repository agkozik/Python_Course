# --------------вариант реализации (@asyncio.corotine):-----------------------------------------------------------------
import random
import asyncio


@asyncio.coroutine
def produce():
    yield from asyncio.sleep(0.5)
    data = random.randint(1, 100)
    return data


@asyncio.coroutine
def consume():
    summa = 0
    count = 0

    while True:
        data = yield from produce()
        print('Data = ', data)
        summa += data
        count += 1
        print('Sum: ', summa)
        print('Average: ', summa / count)
        print('---------------------------------------------------------------------------------')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [consume()]
    loop.run_until_complete(asyncio.wait(tasks))
# ---------------------------------------------------------------------------------------------------------------------
