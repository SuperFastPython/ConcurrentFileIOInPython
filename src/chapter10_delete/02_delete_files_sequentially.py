# SuperFastPython.com
# delete files in a directory sequentially
from os import listdir
from os import remove
from os.path import join
from time import time

# delete all files in a directory
def main(path='tmp'):
    # create a list of all files to delete
    files = [
    join(path, filename) for filename in listdir(path)]
    # delete all files
    for filepath in files:
        # delete the file
        remove(filepath)

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = time()
    # run the program
    main()
    # calculate the duration
    time_duration = time() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
