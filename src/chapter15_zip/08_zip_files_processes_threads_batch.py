# SuperFastPython.com
# zip files with processes and threads in batch
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from time import perf_counter

# load a file
def load_file(filepath):
    # open the file
    with open(filepath, 'r') as handle:
        # read and return the contents of the file
        return handle.read()

# load files into memory
def load_files(filepaths):
    # create the thread pool
    with ThreadPoolExecutor(10) as executor:
        # submit tasks
        futures = [executor.submit(
            load_file, name) for name in filepaths]
        # get all results
        filedata = [future.result()
            for future in futures]
        # return paths and data
        return (filepaths, filedata)

# create a zip file
def main(path='tmp'):
    # list all files to add to the zip
    files = [join(path,f) for f in listdir(path)]
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # determine chunksize
        chunksize = 10
        # create the process pool
        with ProcessPoolExecutor(8) as exe:
            # split the operations into chunks
            futures = list()
            for i in range(0, len(files), chunksize):
                # select a chunk of filenames
                filepaths = files[i:(i + chunksize)]
                # submit the task
                futures.append(exe.submit(
                    load_files, filepaths))
            # compress batches of files as loaded
            for future in as_completed(futures):
                # get the data
                filepaths, filedata = future.result()
                # add each to the zip file
                for filepath,data in zip(
                    filepaths, filedata):
                    # add to the archive
                    handle.writestr(filepath, data)

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
