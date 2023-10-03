# SuperFastPython.com
# add many files to a zip archive with threads in batch
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

# load the file and add it to the zip, thread safe
def add_files(lock, handle, filepaths):
    # load files first
    filedata = list()
    for filepath in filepaths:
        # load the data as a string
        with open(filepath, 'r') as file_handle:
            filedata.append(file_handle.read())
    # add all data to zip
    with lock:
        for filepath,data in zip(filepaths, filedata):
            handle.writestr(filepath, data)

# create a zip file
def main(path='tmp'):
    # list all files to add to the zip
    files = [join(path,f) for f in listdir(path)]
    # create lock for adding files to the zip
    lock = Lock()
    # determine chunksize
    n_workers = 100
    chunksize = round(len(files) / n_workers)
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # create the thread pool
        with ThreadPoolExecutor(n_workers) as exe:
            # split the operations into chunks
            for i in range(0, len(files), chunksize):
                # select a chunk of filenames
                filepaths = files[i:(i + chunksize)]
                # submit the task
                _ = exe.submit(
                    add_files, lock, handle, filepaths)

# protect the entry point
if __name__ == '__main__':
    # run 3 times and record the durations
    times = list()
    for _ in range(3):
        # record start time
        time_start = perf_counter()
        # run the program
        main()
        # calculate the duration
        time_duration = perf_counter() - time_start
        # report the duration
        print(f'>took {time_duration:.3f} seconds')
        # store the duration
        times.append(time_duration)
    # report the average duration
    time_average = sum(times) / 3.0
    print(f'Average time {time_average:.3f} seconds')
