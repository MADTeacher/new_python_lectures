import asyncio

async def task1() -> int:
    await asyncio.sleep(3)
    return 2

async def task2() -> list[int]:
    await asyncio.sleep(2)
    return [1, 2, 3]

async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    answer = await asyncio.gather(t1, t2)
    print(answer)

if __name__ == "__main__":
    asyncio.run(main())
