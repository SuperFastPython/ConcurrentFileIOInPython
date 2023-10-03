# SuperFastPython.com
# rename all files in a dir with asyncio in batch
from os import listdir
from os.path import join
from os.path import splitext
from time import perf_counter
import asyncio
from aiofiles.os import rename

# rename a files
async def rename_files(filenames, src):
    # rename all files
    for filename in filenames:
        # separate filename into name and extension
        name, extension = splitext(filename)
        # devise new filename
        dest_filename = f'{name}-new{extension}'
        # devise source and destination relative paths
        src_path = join(src, filename)
        dest_path = join(src, dest_filename)
        # rename file
        await rename(src_path, dest_path)

# rename files in src
async def main(src='tmp'):
    # list of all files to rename
    files = [name for name in listdir(src)]
    # determine chunksize
    n_workers = 100
    chunksize = round(len(files) / n_workers)
    # split the rename operations into chunks
    tasks = list()
    for i in range(0, len(files), chunksize):
        # select a chunk of filenames
        filenames = files[i:(i + chunksize)]
        # add coroutine to list of tasks
        tasks.append(rename_files(filenames, src))
    # execute and wait for all coroutines
    await asyncio.gather(*tasks)

# protect the entry point
if __name__ == '__main__':
    # run 3 times and record the durations
    times = list()
    for _ in range(3):
        # record start time
        time_start = perf_counter()
        # execute the asyncio run loop
        asyncio.run(main())
        # calculate the duration
        time_duration = perf_counter() - time_start
        # report the duration
        print(f'>took {time_duration:.3f} seconds')
        # store the duration
        times.append(time_duration)
    # report the average duration
    time_average = sum(times) / 3.0
    print(f'Average time {time_average:.3f} seconds')
