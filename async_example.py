import asyncio


async def find_divisible(inrange, div_by):
    print(f'finding nums in range {inrange} divisible by {div_by}')
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    return located


async def main():
    divs1 = loop.create_task(find_divisible(5080000, 34113))
    divs2 = loop.create_task(find_divisible(508023, 33))
    divs3 = loop.create_task(find_divisible(108000, 3413))
    divs4 = loop.create_task(find_divisible(208000, 3))
    await asyncio.wait([divs1, divs2, divs3, divs4])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()