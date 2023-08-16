# SuperFastPython.com
# example of writing a file as a foreground task

# task to write a file
def write_file(filename, data):
    # open a file for writing text
    with open(filename, 'w', encoding='utf-8') as hdl:
        # write string data to the file
        hdl.write(data)
    # report a message
    print(f'File saved: {filename}')

# protect the entry point
if __name__ == '__main__':
    # report a message
    print('Main is running')
    # save the file
    print('Saving file...')
    write_file('data.txt', 'Hello world')
    # report a message
    print('Main is done.')
