# SuperFastPython.com
# delete a file
from os import remove

# create a new file in the current working directory
with open('delete_file.txt', 'x', encoding='utf-8') as h:
    pass
# delete the file
remove('delete_file.txt')
