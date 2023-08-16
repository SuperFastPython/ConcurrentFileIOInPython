# SuperFastPython.com
# list the contents of a directory
from os import listdir

# directory to list
directory = '/'
# report the contents of the directory
for name in listdir(directory):
    print(name)
