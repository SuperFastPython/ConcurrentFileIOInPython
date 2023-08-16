# SuperFastPython.com
# example of reading to a file with asyncio and aiofiles
import asyncio
import aiofiles

# read a file
async def main():
    # open the file
    async with aiofiles.open(
        '/etc/services', mode='r') as handle:
        # read the contents of the file
        data = await handle.read()
    print(f'Read {len(data)} bytes')

# entry point
asyncio.run(main())
