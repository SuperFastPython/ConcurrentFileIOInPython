# SuperFastPython.com
# create a zip file and add files with processes
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
from time import time

# load file into memory
def load_file(filepath):
    # open the file
    with open(filepath, 'r') as handle:
        # return the contents and the filepath
        return (filepath, handle.read())

# create a zip file
def main(path='tmp'):
    # list all files to add to the zip
    files = [join(path,f) for f in listdir(path)]
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # create the thread pool
        with ProcessPoolExecutor(8) as exe:
            # load all files into memory
            futures = [exe.submit(load_file,
                filepath) for filepath in files]
            # compress files as they are loaded
            for future in as_completed(futures):
                # get the data
                filepath, data = future.result()
                # add to the archive
                handle.writestr(filepath, data)

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
