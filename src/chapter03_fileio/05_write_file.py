# SuperFastPython.com
# write a string to a file

# open a file for writing text
with open('new_file.txt', 'w', encoding='utf-8') as hdl:
    # write string data to the file
    hdl.write('We are writing to file')
