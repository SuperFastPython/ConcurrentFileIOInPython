# SuperFastPython.com
# unzip files with processes and threads in batch
from os import makedirs
from os.path import join
from zipfile import ZipFile
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from time import time

# save file to disk
def save_file(data, filename, path):
    # create a path
    filepath = join(path, filename)
    # write to disk
    with open(filepath, 'wb') as file:
        file.write(data)

# unzip files from an archive
def unzip_files(zip_filename, filenames, path):
    # open the zip file
    with ZipFile(zip_filename, 'r') as handle:
        # create a thread pool
        with ThreadPoolExecutor(100) as exe:
            # unzip each file
            for filename in filenames:
                # decompress data
                data = handle.read(filename)
                # save to disk
                _ = exe.submit(
                    save_file, data, filename, path)

# unzip a large number of files
def main(path='tmp', zip_filename='testing.zip'):
    # create the target directory
    makedirs(path, exist_ok=True)
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
