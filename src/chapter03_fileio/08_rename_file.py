# SuperFastPython.com
# rename a file
from os import rename

# create a new file in the current working directory
with open('rename_file.txt', 'x', encoding='utf-8') as h:
    pass
# rename the file
rename('rename_file.txt', 'test_file.txt')
