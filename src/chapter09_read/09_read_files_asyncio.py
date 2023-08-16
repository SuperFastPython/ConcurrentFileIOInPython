# SuperFastPython.com
# load many files concurrently with asyncio
# NOTE: this example will fail with an exception!
from os import listdir
from os.path import join
import asyncio
import aiofiles

# open a file and return the contents
async def load_file(filepath):
    # open the file
    async with aiofiles.open(filepath, 'r') as handle:
        # return the contents
        return (await handle.read(), filepath)

# load all files in a directory into memory
async def main(path='tmp'):
    # prepare all of the paths
    paths = [join(
        path, filepath) for filepath in listdir(path)]
    # create coroutines
    tasks = [load_file(filepath) for filepath in paths]
    # execute tasks and process results as completed
    for task in asyncio.as_completed(tasks):
        # open the file and load the data
        data, filepath = await task

# protect the entry point
if __name__ == '__main__':
    asyncio.run(main()) # fails with error
