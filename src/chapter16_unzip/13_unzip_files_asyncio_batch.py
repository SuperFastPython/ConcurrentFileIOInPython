# SuperFastPython.com
# unzip a large number of files with asyncio in batch
from os import makedirs
from os.path import join
from zipfile import ZipFile
from time import time
import asyncio
import aiofiles

# extract files from the archive and save to disk
async def extract_and_save(handle, filenames, path):
    # extract each file
    for filename in filenames:
        # decompress data, blocking
        data = handle.read(filename)
        # create a path
        filepath = join(path, filename)
        # write to disk
        async with aiofiles.open(filepath, 'wb') as fd:
            await fd.write(data)

# unzip a large number of files
async def main(path='tmp'):
    # create the target directory
    makedirs(path, exist_ok=True)
    # open the zip file
    with ZipFile('testing.zip', 'r') as handle:
        # determine all of the files to extract
        files = handle.namelist()
        # determine chunksize
        n_workers = 100
        chunksize = round(len(files) / n_workers)
        # split the move operations into chunks
        tasks = list()
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filenames = files[i:(i + chunksize)]
            # add coroutine to list of tasks
            tasks.append(extract_and_save(
                handle, filenames, path))
        # execute and wait for all coroutines
        await asyncio.gather(*tasks)

# protect the entry point
if __name__ == '__main__':
    # run 3 times and record the durations
    times = list()
    for _ in range(3):
        # record start time
        time_start = time()
        # run the program
        asyncio.run(main())
        # calculate the duration
        time_duration = time() - time_start
        # report the duration
        print(f'>took {time_duration:.3f} seconds')
        # store the duration
        times.append(time_duration)
    # report the average duration
    time_average = sum(times) / 3.0
    print(f'Average time {time_average:.3f} seconds')
