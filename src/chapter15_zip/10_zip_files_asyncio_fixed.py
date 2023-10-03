# SuperFastPython.com
# create a zip file and add files with asyncio
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from time import perf_counter
import asyncio
import aiofiles

# open a file and return the contents
async def load_file(filepath, semaphore):
    # acquire the semaphore
    async with semaphore:
        # open the file
        async with aiofiles.open(filepath, 'r') as hdl:
            # return the contents
            return (await hdl.read(), filepath)

# load all files in a directory into memory
async def main(path='tmp'):
    # prepare all of the paths
    paths = [join(path, filepath)
        for filepath in listdir(path)]
    # create a semaphore to limit open files
    semaphore = asyncio.Semaphore(100)
    # create coroutines
    tasks = [load_file(filepath, semaphore)
        for filepath in paths]
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # execute tasks and process results as completed
        for task in asyncio.as_completed(tasks):
            # open the file and load the data
            data, filepath = await task
            # add to the archive
            handle.writestr(filepath, data)

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
