import asyncio

async def task1():
    print("Task1 start")
    await asyncio.sleep(1)
    print("Task1 end")

async def task2():
    print("Task2 start")
    await asyncio.sleep(2)
    print("Task2 end")

async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(t1, t2)

if __name__ == "__main__":
    asyncio.run(main())
