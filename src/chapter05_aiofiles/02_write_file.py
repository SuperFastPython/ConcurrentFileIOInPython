# SuperFastPython.com
# example of writing to file with asyncio and aiofiles
import asyncio
import aiofiles

# write a file
async def main():
    # open the file
    async with aiofiles.open(
        'test_write.txt', mode='w') as handle:
        # write to the file
        await handle.write('Hello world')

# entry point
asyncio.run(main())
