# SuperFastPython.com
# delete all files from a dir with asyncio in batch
from os import listdir
from os.path import join
from time import perf_counter
import asyncio
from aiofiles.os import remove

# delete files and report progress
async def delete_files(filepaths):
    # process all file names
    for filepath in filepaths:
        # delete the file
        await remove(filepath)

# delete all files in a directory
async def main(path='tmp'):
    # create a list of all files to delete
    filepaths = [join(
        path, filename) for filename in listdir(path)]
    # determine chunksize
    n_workers = 100
    chunksize = round(len(filepaths) / n_workers)
    # split the remove operations into chunks
    tasks = list()
    for i in range(0, len(filepaths), chunksize):
        # select a chunk of filenames
        filenames = filepaths[i:(i + chunksize)]
        # submit the batch remove task
        tasks.append(delete_files(filenames))
    # execute all coroutines concurrently and wait
    await asyncio.gather(*tasks)

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = perf_counter()
    # execute the asyncio run loop
    asyncio.run(main())
    # calculate the duration
    time_duration = perf_counter() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
