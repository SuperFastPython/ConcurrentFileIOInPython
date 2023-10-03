# SuperFastPython.com
# load many files concurrently with processes in batch
from os import listdir
from os.path import join
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
from time import perf_counter

# open a file and return the contents
def load_files(filepaths):
    data_list = list()
    # load each file
    for filepath in filepaths:
        # open the file
        with open(filepath, 'r') as handle:
            # return the contents
            data_list.append(handle.read())
    return data_list, filepaths

# load all files in a directory into memory
def main(path='tmp'):
    # prepare all of the paths
    paths = [join(
        path, filepath) for filepath in listdir(path)]
    # determine chunksize
    chunksize = 20
    # create the process pool
    with ProcessPoolExecutor(4) as executor:
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
