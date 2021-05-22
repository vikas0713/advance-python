import asyncio
from time import sleep


async def counter(n):
    while n > 1:
        print(f'{n} is the state')
        n -= 1
        sleep(0.5)
    return n


async def simple_counter(n):
    while n > 1:
        print(f'simple {n}')
        n -= 1
        sleep(0.5)
    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(counter(100))
    task2 = asyncio.create_task(simple_counter(100))
    value = await task1, task2
    print(value)

asyncio.run(main())
