# SuperFastPython.com
# unzip a large number of files with asyncio
from os import makedirs
from os.path import join
from zipfile import ZipFile
import asyncio
import aiofiles

# extract a file from the archive and save to disk
async def extract_and_save(handle, filename, path):
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
        # create coroutines
        tasks = [extract_and_save(handle, name, path)
            for name in handle.namelist()]
        # execute all tasks
        _ = await asyncio.gather(*tasks)

# protect the entry point
if __name__ == '__main__':
    # run the program
    asyncio.run(main())
