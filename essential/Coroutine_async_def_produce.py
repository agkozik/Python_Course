# --------------вариант реализации (@asyncio.corotine):-----------------------------------------------------------------
import random
import asyncio


async def produce():
    await asyncio.sleep(0.5)
    data = random.randint(1, 100)
    return data


async def consume():
    while True:
        data = await produce()
        print('Data = ', data)
        print('---------------------------------------------------------------------------------')


# для наглядности еще один метод вывода:
async def another_task():
    while True:
        print('---Another method---')
        print()
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [consume(), another_task()]
    loop.run_until_complete(asyncio.wait(tasks))