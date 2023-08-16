# SuperFastPython.com
# example of creating a directory asyncio and aiofiles
import asyncio
import aiofiles
import aiofiles.os

# create a directory
async def main():
    # create a directory
    await aiofiles.os.makedirs('tmp', exist_ok=True)

# entry point
asyncio.run(main())
