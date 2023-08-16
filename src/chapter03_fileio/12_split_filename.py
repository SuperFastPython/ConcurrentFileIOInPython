# SuperFastPython.com
# separate a filename into name and extension
from os.path import splitext

# separate into name and extension
name, ext = splitext('filename.ext')
print(name, ext)
