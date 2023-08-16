# SuperFastPython.com
# example of deleting a file asyncio and aiofiles
import asyncio
import aiofiles
import aiofiles.os

# delete a file
async def main():
    # create a file with no content
    handle = await aiofiles.open(
        'files_delete.txt', mode='x')
    handle.close()
    # delete the file
    await aiofiles.os.remove('files_delete.txt')

# entry point
asyncio.run(main())
