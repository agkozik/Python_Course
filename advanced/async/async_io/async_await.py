import asyncio


async def async_worker(number, divider):
    print('Worker {} started'.format(number))
    await asyncio.sleep(1)
    print(number / divider)
    return number / divider


async def gather_worker():
    # запланированный вызов функций: собирает ряд задач, дожидается выполнения их всех, собирает в виде списка
    # и сохраняет в переменную result
    result = await asyncio.gather(
        async_worker(50, 10),
        async_worker(60, 10),
        async_worker(70, 10),
        async_worker(80, 10),
        async_worker(90, 10),
        async_worker(100, 10),
    )
    print(result)


event_loop = asyncio.get_event_loop()
# создаем список задач, которые хотим выполнить:
task_list = [
    async_worker(30, 10),
    # ensure_future можно использовать для совместимости, обертка добавляет проверки
    asyncio.ensure_future(async_worker(30, 10)),
    event_loop.create_task(gather_worker())
]
# оборачиваем в ожидание
tasks = asyncio.wait(task_list)
# передаем сопрограмму tasks в наш event_loop
event_loop.run_until_complete(tasks)
event_loop.close()