# SuperFastPython.com
# load many files sequentially
from os import listdir
from os.path import join
from time import time

# open a file and return the contents
def load_file(filepath):
    # open the file
    with open(filepath, 'r') as handle:
        # return the contents
        return handle.read()

# load all files in a directory into memory
def main(path='tmp'):
    # prepare all of the paths
    paths = [join(
        path, filepath) for filepath in listdir(path)]
    # load each file in the directory
    for filepath in paths:
         # open the file and load the data
        data = load_file(filepath)

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
