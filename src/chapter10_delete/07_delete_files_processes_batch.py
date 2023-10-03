# SuperFastPython.com
# delete files in a directory with processes in batch
from os import listdir
from os import remove
from os.path import join
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

# delete a file and report progress
def delete_file(filepaths):
    # process all file names
    for filepath in filepaths:
        # delete the file
        remove(filepath)

# delete all files in a directory
def main(path='tmp'):
    # create a list of all files to delete
    files = [join(
        path, filename) for filename in listdir(path)]
    # determine chunksize
    n_workers = 8
    chunksize = round(len(files) / n_workers)
    # create the process pool
    with ProcessPoolExecutor(n_workers) as exe:
        # split the remove operations into chunks
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filenames = files[i:(i + chunksize)]
            # submit the batch remove task
            _ = exe.submit(delete_file, filenames)

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = perf_counter()
    # run the program
    main()
    # calculate the duration
    time_duration = perf_counter() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
