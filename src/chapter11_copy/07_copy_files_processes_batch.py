# SuperFastPython.com
# copy files from a dir with processes in batch
from os import makedirs
from os import listdir
from os.path import join
from shutil import copy
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

# copy files from source to destination
def copy_files(src_paths, dest_dir):
    # process all file paths
    for src_path in src_paths:
        # copy source file to dest file
        dest_path = copy(src_path, dest_dir)

# copy files from src to dest
def main(src='tmp', dest='tmp2'):
    # create the destination directory if needed
    makedirs(dest, exist_ok=True)
    # create full paths for all files we wish to copy
    files = [join(src,name) for name in listdir(src)]
    # determine chunksize
    n_workers = 4
    chunksize = round(len(files) / n_workers)
    # create the process pool
    with ProcessPoolExecutor(n_workers) as exe:
        # split the copy operations into chunks
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filenames = files[i:(i + chunksize)]
            # submit the batch copy task
            _ = exe.submit(copy_files, filenames, dest)

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
