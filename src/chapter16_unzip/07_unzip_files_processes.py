# SuperFastPython.com
# unzip a large number of files with processes
from zipfile import ZipFile
from concurrent.futures import ProcessPoolExecutor
from time import time

# unzip a file from an archive
def unzip_file(zip_filename, filename, path):
    # open the zip file
    with ZipFile(zip_filename, 'r') as handle:
        # unzip the file
        handle.extract(filename, path)

# unzip a large number of files
def main(path='tmp', zip_filename='testing.zip'):
    # open the zip file
    with ZipFile(zip_filename, 'r') as handle:
        # get a list of files to unzip
        files = handle.namelist()
    # start the process pool
    with ProcessPoolExecutor(8) as exe:
        # unzip each file from the archive
        _ = [exe.submit(unzip_file, zip_filename,
            name, path) for name in files]

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
