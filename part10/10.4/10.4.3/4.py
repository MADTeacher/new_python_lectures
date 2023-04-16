import asyncio

async def long_operation():
    await asyncio.sleep(10)
    print('Long operation completed')

async def main():
    task = asyncio.create_task(long_operation())
    while not task.done():
        print('Waiting for long operation to complete')
        await asyncio.sleep(1)
    print('Long operation is done')

if __name__ == '__main__':
    asyncio.run(main())
