# SuperFastPython.com
# example of writing a file using a coroutine
import asyncio
import aiofiles

# coroutine to write a file
async def write_file(filename, data):
    # open a file for writing text
    async with aiofiles.open(
        filename, 'w', encoding='utf-8') as hdl:
        # write string data to the file
        await hdl.write(data)
    # report a message
    print(f'File saved: {filename}')

# main coroutine
async def main():
    # report a message
    print('Main is running')
    # save the file
    print('Saving file...')
    # save the file in a new background task
    _ = asyncio.create_task(
        write_file('data.txt', 'Hello world'))
    # carry on with other activities (sleep)
    await asyncio.sleep(1)
    # report a message
    print('Main is done.')

# protect the entry point
if __name__ == '__main__':
    # start the asyncio runtime
    asyncio.run(main())
