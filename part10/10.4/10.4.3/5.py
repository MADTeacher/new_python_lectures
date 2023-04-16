import asyncio
from asyncio import CancelledError

async def main():
    long_task = asyncio.create_task(asyncio.sleep(7))
    count = 0
    while not long_task.done():
        print(f'Count value = {count}')
        await asyncio.sleep(1)
        count += 1
        if count == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print('Task was cancelled')

if __name__ == '__main__':
    asyncio.run(main())
