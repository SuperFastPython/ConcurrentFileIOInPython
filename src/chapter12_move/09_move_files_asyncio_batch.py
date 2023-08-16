# SuperFastPython.com
# move files from one dir with asyncio in batch
from os import makedirs
from os import listdir
from os.path import join
from time import time
import asyncio
from aiofiles.os import rename

# move files from source to destination
async def move_files(filenames, src, dest):
    # rename all files
    for filename in filenames:
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
    # determine chunksize
    n_workers = 100
    chunksize = round(len(files) / n_workers)
    # split the move operations into chunks
    tasks = list()
    for i in range(0, len(files), chunksize):
        # select a chunk of filenames
        filenames = files[i:(i + chunksize)]
        # add coroutine to list of tasks
        tasks.append(move_files(filenames, src, dest))
    # execute and wait for all coroutines
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
