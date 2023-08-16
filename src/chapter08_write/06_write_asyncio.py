# SuperFastPython.com
# write many data files concurrently with asyncio
# NOTE: this example will fail with an exception!
from os import makedirs
from os.path import join
import asyncio
import aiofiles

# save data to a file
async def save_file(filepath, data):
    # open the file
    async with aiofiles.open(filepath, 'w') as handle:
        # save the data
        await handle.write(data)

# generate a csv with 10 values per line and 5k lines
def generate_file(ident, n_values=10, n_lines=5000):
    # generate many lines of data
    data = list()
    for i in range(n_lines):
        # generate a list of numeric values as strings
        line = [str(ident+i+j) for j in range(n_values)]
        # convert list to string, separated by commas
        data.append(','.join(line))
    # convert list of lines to a string, add new lines
    return '\n'.join(data)

# generate and save a file
async def generate_and_save(path, identifier):
    # generate data
    data = generate_file(identifier)
    # create a unique filename
    filepath = join(path, f'data-{identifier:04d}.csv')
    # save data file to disk
    await save_file(filepath, data)

# generate many data files in a directory
async def main(path='tmp', n_files=5000):
    # create a local directory to save files
    makedirs(path, exist_ok=True)
    # create one coroutine for each file to rename
    tasks = [generate_and_save(
        path, i) for i in range(n_files)]
    # execute and wait for all coroutines
    await asyncio.gather(*tasks)

# entry point
if __name__ == '__main__':
    # execute the asyncio run loop
    asyncio.run(main()) # fails with error
