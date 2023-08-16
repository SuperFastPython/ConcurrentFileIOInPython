# SuperFastPython.com
# read a file into memory

# the file to open
path = '/etc/services'
# open a file for writing text
with open(path, 'r', encoding='utf-8') as handle:
    # read the contents of the file as string
    data = handle.read()
    # report details about the content
    print(f'{path} has {len(data)} characters')
