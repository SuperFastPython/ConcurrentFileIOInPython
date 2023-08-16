# SuperFastPython.com
# example of creating a file with asyncio and aiofiles
import asyncio
import aiofiles

# create a file
async def main():
    # create a file with no content
    handle = await aiofiles.open(
        'test_create.txt', mode='x')
    # close the file
    handle.close()

# entry point
asyncio.run(main())
