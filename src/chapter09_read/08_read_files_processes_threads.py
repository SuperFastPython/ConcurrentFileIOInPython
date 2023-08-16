# SuperFastPython.com
# load many files with processes and threads in batch
from os import listdir
from os.path import join
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from time import time

# load a file and return the contents
def load_file(filepath):
    # open the file
    with open(filepath, 'r') as handle:
        # return the contents
        handle.read()

# return the contents of many files
def load_files(filepaths):
    # create a thread pool
    with ThreadPoolExecutor(len(filepaths)) as exe:
        # load files
        futures = [exe.submit(
            load_file, name) for name in filepaths]
        # collect data
        data_list = [future.result()
            for future in futures]
        # return data and file paths
        return (data_list, filepaths)

# load all files in a directory into memory
def main(path='tmp'):
    # prepare all of the paths
    paths = [join(
        path, filepath) for filepath in listdir(path)]
    # determine chunksize
    n_workers = 8
    chunksize = round(len(paths) / n_workers)
    # create the process pool
    with ProcessPoolExecutor(n_workers) as executor:
        futures = list()
        # split the load operations into chunks
        for i in range(0, len(paths), chunksize):
            # select a chunk of filenames
            filepaths = paths[i:(i + chunksize)]
            # submit the task
            future = executor.submit(
                load_files, filepaths)
            futures.append(future)
        # process all results
        for future in as_completed(futures):
            # open the file and load the data
            _, filepaths = future.result()

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
