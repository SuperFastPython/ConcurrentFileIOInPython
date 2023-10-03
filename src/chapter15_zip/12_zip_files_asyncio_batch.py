# SuperFastPython.com
# create a zip and add files with asyncio in batch
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from time import perf_counter
import asyncio
import aiofiles

# load a file as a string, add to zip, thread safe
async def add_files(lock, handle, filepaths):
    # add all files
    filedata = list()
    for filepath in filepaths:
        # load the data as a string
        async with aiofiles.open(filepath, 'r') as fd:
            data = await fd.read()
            filedata.append(data)
    # lock on the zip file
    async with lock:
        # write all files to zip
        for filepath, data in zip(filepaths, filedata):
            handle.writestr(filepath, data)

# create a zip file
async def main(path='tmp'):
    # list all files to add to the zip
    files = [join(path,f) for f in listdir(path)]
    # create lock for adding files to the zip
    lock = asyncio.Lock()
    # determine chunksize
    n_workers = 100
    chunksize = round(len(files) / n_workers)
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # split the operations into chunks
        tasks = list()
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filepaths = files[i:(i + chunksize)]
            # add the coroutine to the list
            tasks.append(add_files(
                lock, handle, filepaths))
        # execute and wait for all coroutines
        await asyncio.gather(*tasks)

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
