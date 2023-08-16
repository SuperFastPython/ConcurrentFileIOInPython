# SuperFastPython.com
# add files to a zip file
from zipfile import ZipFile

# open a file for writing text
with open('new_file.txt', 'w', encoding='utf-8') as hdl:
    # write string data to the file
    hdl.write('We are writing to file')
# create a zip file in the current directory
with ZipFile('file_archive.zip', 'w') as hdl:
    # add a text file to the archive
    hdl.write('new_file.txt')
