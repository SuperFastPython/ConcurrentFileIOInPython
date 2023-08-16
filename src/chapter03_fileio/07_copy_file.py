# SuperFastPython.com
# copy a file
from shutil import copy

# create a new file in the current working directory
with open('copy_file.txt', 'x', encoding='utf-8') as h:
    pass
# copy the file
copy('copy_file.txt', 'copy_file2.txt')
