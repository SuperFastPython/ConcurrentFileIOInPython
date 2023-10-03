# SuperFastPython.com
# unzip a large number of files with asyncio, fixed
from os import makedirs
from os.path import join
from zipfile import ZipFile
from time import perf_counter
import asyncio
import aiofiles

# extract a file from the archive and save to disk
async def extract_and_save(handle, sem, filename, path):
    # decompress data, blocking
    data = handle.read(filename)
    # create a path
    filepath = join(path, filename)
    # acquire the semaphore
    async with sem:
        # write to disk
        async with aiofiles.open(filepath, 'wb') as fd:
            await fd.write(data)

# unzip a large number of files
async def main(path='tmp'):
    # create the target directory
    makedirs(path, exist_ok=True)
    # create the shared semaphore
    sem = asyncio.Semaphore(100)
    # open the zip file
    with ZipFile('testing.zip', 'r') as handle:
        # create coroutines
        tasks = [extract_and_save(
            handle, sem, name, path)
            for name in handle.namelist()]
        # execute all tasks
        _ = await asyncio.gather(*tasks)

# protect the entry point
if __name__ == '__main__':
    # run 3 times and record the durations
    times = list()
    for _ in range(3):
        # record start time
        time_start = perf_counter()
        # run the program
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
