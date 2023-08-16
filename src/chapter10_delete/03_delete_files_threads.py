# SuperFastPython.com
# delete files in a directory concurrently with threads
from os import listdir
from os import remove
from os.path import join
from concurrent.futures import ThreadPoolExecutor
from time import time

# delete a file and report progress
def delete_file(filepath):
    # delete the file
    remove(filepath)

# delete all files in a directory
def main(path='tmp'):
    # create a list of all files to delete
    files = [join(
        path, filename) for filename in listdir(path)]
    # create a thread pool
    with ThreadPoolExecutor(10) as exe:
        # delete all files
        _ = [exe.submit(
            delete_file, filepath) for filepath in files]

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
