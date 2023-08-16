# SuperFastPython.com
# load many files concurrently with processes
from os import listdir
from os.path import join
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
from time import time

# open a file and return the contents
def load_file(filepath):
    # open the file
    with open(filepath, 'r') as handle:
        # return the contents
        return handle.read(), filepath

# load all files in a directory into memory
def main(path='tmp'):
    # prepare all of the paths
    paths = [join(
        path, filepath) for filepath in listdir(path)]
    # create the process pool
    with ProcessPoolExecutor(4) as executor:
        # submit all tasks
        futures = [executor.submit(
            load_file, p) for p in paths]
        # process all results
        for future in as_completed(futures):
            # open the file and load the data
            data, filepath = future.result()

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
