import asyncio
import random

# Задача producer/consumer
# Вариант 1
q = asyncio.Queue()


async def producer():
    while True:
        x = random.randint(a=1, b=10000)
        print(f'Produced: ' + str(x))
        await q.put(x)
        await asyncio.sleep(random.random())

        
async def consumer():
    while True:
        value = await q.get()
        await asyncio.sleep(random.random() * 2)
        print(f'Consumed:', value)

loop = asyncio.get_event_loop()

for _ in range(5):
    loop.create_task(producer())

for _ in range(2):
    loop.create_task(consumer())

loop.run_forever()

# Вариант 2

async def producer(queue):
    while True:
        x = random.randint(a=1, b=10000)
        print(f'Produced: ' + str(x))
        await queue.put(x)
        await asyncio.sleep(random.random() * 2)


async def consumer(queue):
    while True:
        x = await queue.get()
        await asyncio.sleep(random.random() * 2)
        queue.task_done()
        print(f'Consumed {x}')


async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue)) for _ in range(5)]
    consumers = [asyncio.create_task(consumer(queue)) for _ in range(2)]
    await asyncio.gather(*producers)
    await queue.join()
    for consum in consumers:
        consum.cancel()


asyncio.run(main())
