# SuperFastPython.com
# move a file
from os import makedirs
from shutil import move

# create a new file in the current working directory
with open('moving_file.txt', 'x', encoding='utf-8') as h:
    pass
# create a new sub-dir in the current working directory
makedirs('tmp', exist_ok=True)
# move the file under the sub-directory
move('moving_file.txt', 'tmp')
