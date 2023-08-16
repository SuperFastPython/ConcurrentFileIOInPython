# SuperFastPython.com
# unzip a large number of files with processes in batch
from zipfile import ZipFile
from concurrent.futures import ProcessPoolExecutor
from time import time

# unzip files from an archive
def unzip_files(zip_filename, filenames, path):
    # open the zip file
    with ZipFile(zip_filename, 'r') as handle:
        # unzip multiple files
        for filename in filenames:
            # unzip the file
            handle.extract(filename, path)

# unzip a large number of files
def main(path='tmp', zip_filename='testing.zip'):
    # open the zip file
    with ZipFile(zip_filename, 'r') as handle:
        # list of all files to unzip
        files = handle.namelist()
    # determine chunksize
    n_workers = 8
    chunksize = round(len(files) / n_workers)
    # start the thread pool
    with ProcessPoolExecutor(n_workers) as exe:
        # split the unzip operations into chunks
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filenames = files[i:(i + chunksize)]
            # submit the batch unzip task
            _ = exe.submit(unzip_files, zip_filename,
                filenames, path)

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
