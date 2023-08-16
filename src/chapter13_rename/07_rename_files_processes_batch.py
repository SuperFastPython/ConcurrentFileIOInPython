# SuperFastPython.com
# rename all files in a dir with processes in batch
from os import listdir
from os import rename
from os.path import join
from os.path import splitext
from concurrent.futures import ProcessPoolExecutor
from time import time

# rename a files
def rename_files(filenames, src):
    # rename all files
    for filename in filenames:
        # separate filename into name and extension
        name, extension = splitext(filename)
        # devise new filename
        dest_filename = f'{name}-new{extension}'
        # devise source and destination relative paths
        src_path = join(src, filename)
        dest_path = join(src, dest_filename)
        # rename file
        rename(src_path, dest_path)

# rename files in src
def main(src='tmp'):
    # list of all files to rename
    files = [name for name in listdir(src)]
    # determine chunksize
    n_workers = 8
    chunksize = round(len(files) / n_workers)
    # create the thread pool
    with ProcessPoolExecutor(n_workers) as exe:
        # split the rename operations into chunks
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filenames = files[i:(i + chunksize)]
            # submit file rename tasks
            _ = exe.submit(rename_files, filenames, src)

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
