import asyncio

async def long_operation():
    try:
        await asyncio.sleep(10)
        print('Long operation completed')
    except asyncio.CancelledError:
        print('Long operation cancelled')

async def main():
    task = asyncio.create_task(long_operation())
    await asyncio.sleep(5)
    task.cancel()
    await asyncio.gather(task)

if __name__ == '__main__':
    asyncio.run(main())
