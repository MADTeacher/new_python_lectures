import asyncio

async def long_operation():
    await asyncio.sleep(5)
    return 'Long operation completed'

async def main():
    task = asyncio.create_task(long_operation())
    try:
        result = await asyncio.wait_for(task, timeout=3)
    except asyncio.TimeoutError:
        print('Long operation timed out')
    else:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
