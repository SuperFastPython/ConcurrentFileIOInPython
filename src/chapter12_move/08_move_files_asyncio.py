# SuperFastPython.com
# move files from one dir with asyncio
from os import makedirs
from os import listdir
from os.path import join
from time import time
import asyncio
from aiofiles.os import rename

# move a file from source to destination
async def move_file(filename, src, dest):
    # create the path for the source
    src_path = join(src, filename)
    # create the path for the destination
    dest_path = join(dest, filename)
    # move source file to destination file
    await rename(src_path, dest_path)

# move files from src to dest
async def main(src='tmp', dest='tmp2'):
    # create the destination directory if needed
    makedirs(dest, exist_ok=True)
    # list of all files to move
    files = [name for name in listdir(src)]
    # create a list of coroutines for moving files
    tasks = [move_file(name, src, dest) for name in files]
    # execute and wait for all tasks to complete
    await asyncio.gather(*tasks)

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = time()
    # execute the asyncio run loop
    asyncio.run(main())
    # calculate the duration
    time_duration = time() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
