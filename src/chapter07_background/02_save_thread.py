# SuperFastPython.com
# example of writing a file using a new thread
from threading import Thread

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
    # create and configure the new thread
    thread = Thread(target=write_file,
        args=('data.txt', 'Hello world'))
    # start running the new thread in the background
    thread.start()
    # report a message
    print('Main is done.')
