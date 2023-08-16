# SuperFastPython.com
# example of copying a file asyncio and aiofiles
import asyncio
import aiofiles
import aiofiles.os

# copy a file
async def main():
    # create a file with some content
    async with aiofiles.open(
        'files_copy.txt', mode='w') as handle:
        # write some content
        await handle.write('hello world')
    # create file objects for the source and destination
    handle_src = await aiofiles.open(
        'files_copy.txt', mode='r')
    handle_dst = await aiofiles.open(
        'files_copy2.txt', mode='w')
    # get the number of bytes for the source
    stat_src = await aiofiles.os.stat('files_copy.txt')
    n_bytes = stat_src.st_size
    # get the file descriptors
    fd_src = handle_src.fileno()
    fd_dst = handle_dst.fileno()
    # copy the file
    await aiofiles.os.sendfile(
        fd_dst, fd_src, 0, n_bytes)

# entry point
asyncio.run(main())
