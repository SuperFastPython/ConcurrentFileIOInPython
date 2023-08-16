# SuperFastPython.com
# example of renaming a file asyncio and aiofiles
import asyncio
import aiofiles
import aiofiles.os

# rename a file
async def main():
    # create a file with no content
    handle = await aiofiles.open(
        'files_rename.txt', mode='x')
    handle.close()
    # rename the file
    await aiofiles.os.rename(
        'files_rename.txt', 'files_rename2.txt')

# entry point
asyncio.run(main())
