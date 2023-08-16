# SuperFastPython.com
# create a zip file and add files with threads
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from time import time

# load the file and add it to the zip, thread safe
def add_file(lock, handle, filepath):
    # load the data as a string
    with open(filepath, 'r') as file_handle:
        data = file_handle.read()
    # add data to zip
    with lock:
        handle.writestr(filepath, data)

# create a zip file
def main(path='tmp'):
    # list all files to add to the zip
    files = [join(path,f) for f in listdir(path)]
    # create lock for adding files to the zip
    lock = Lock()
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # create the thread pool
        with ThreadPoolExecutor(100) as exe:
            # add all files to the zip archive
            _ = [exe.submit(add_file, lock, handle, f)
                for f in files]

# protect the entry point
if __name__ == '__main__':
    # run 3 times and record the durations
    times = list()
    for _ in range(3):
        # record start time
        time_start = time()
        # run the program
        main()
        # calculate the duration
        time_duration = time() - time_start
        # report the duration
        print(f'>took {time_duration:.3f} seconds')
        # store the duration
        times.append(time_duration)
    # report the average duration
    time_average = sum(times) / 3.0
    print(f'Average time {time_average:.3f} seconds')
