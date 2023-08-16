# SuperFastPython.com
# unzip a large number of files with threads
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor
from time import time

# unzip a large number of files
def main(path='tmp'):
    # open the zip file
    with ZipFile('testing.zip', 'r') as handle:
        # start the thread pool
        with ThreadPoolExecutor(100) as exe:
            # unzip each file from the archive
            _ = [exe.submit(handle.extract, m, path)
                for m in handle.namelist()]

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
