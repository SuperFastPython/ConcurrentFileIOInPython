# SuperFastPython.com
# example of moving a file asyncio and aiofiles
import asyncio
import aiofiles
import aiofiles.os

# move a file
async def main():
    # create a file with no content
    handle = await aiofiles.open('files_move.txt', mode='x')
    handle.close()
    # create a directory
    await aiofiles.os.makedirs('tmp', exist_ok=True)
    # move the file into the directory
    await aiofiles.os.replace('files_move.txt', 'tmp/files_move.txt')

# entry point
asyncio.run(main())
