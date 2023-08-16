# SuperFastPython.com
# append file with asyncio and a shared lock
from random import random
import asyncio
import aiofiles

# task that blocks for a moment and write to a file
async def task(idt, lock, file_handle):
    # block for a moment
    value = random()
    await asyncio.sleep(value)
    # obtain the lock
    async with lock:
        # write to a file
        await file_handle.write(f'Task {idt} ' \
            f'blocked for {value} of a second.\n')

# write to a file from multiple threads
async def main():
    # open a file
    async with aiofiles.open(
        'results.txt', 'a', encoding='utf-8') as hdl:
        # create a lock to protect the file
        lock = asyncio.Lock()
        # create coroutines
        tasks = [task(i, lock, hdl)
            for i in range(10000)]
        # execute tasks and wait for them to finish
        _ = await asyncio.gather(*tasks)
    print('Done.')

# protect the entry point
if __name__ == '__main__':
    asyncio.run(main())
