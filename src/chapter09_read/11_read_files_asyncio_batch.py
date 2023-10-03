# SuperFastPython.com
# load many files concurrently with asyncio in batch
from os import listdir
from os.path import join
import asyncio
import aiofiles
from time import perf_counter

# load and return the contents of a list of file paths
async def load_files(filepaths, semaphore):
    # load all files
    data_list = list()
    for filepath in filepaths:
        # acquire the semaphore
        async with semaphore:
            # open the file
            async with aiofiles.open(
                filepath, 'r') as hdl:
                # load the contents and add to list
                data = await hdl.read()
                # store loaded data
                data_list.append(data)
    return (data_list, filepaths)

# load all files in a directory into memory
async def main(path='tmp'):
    # prepare all of the paths
    paths = [join(
        path, filepath) for filepath in listdir(path)]
    # split up the data
    chunksize = 10
    # create a semaphore to limit open files
    semaphore = asyncio.Semaphore(100)
    # split the operations into chunks
    tasks = list()
    for i in range(0, len(paths), chunksize):
        # select a chunk of filenames
        filepaths = paths[i:(i + chunksize)]
        # define the task
        tasks.append(load_files(filepaths, semaphore))
    # execute tasks and process results as completed
    for task in asyncio.as_completed(tasks):
        # wait for the next task to complete
        _, filepaths = await task

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