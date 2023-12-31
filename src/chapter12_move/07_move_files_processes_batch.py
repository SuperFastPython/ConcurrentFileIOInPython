# SuperFastPython.com
# move files from one dir with processes in batch
from os import makedirs
from os import listdir
from os.path import join
from shutil import move
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

# move files from source to destination
def move_files(filenames, src, dest):
    # process all file names
    for filename in filenames:
        # create the path for the source
        src_path = join(src, filename)
        # create the path for the destination
        dest_path = join(dest, filename)
        # move source file to destination file
        move(src_path, dest_path)

# move files from src to dest
def main(src='tmp', dest='tmp2'):
    # create the destination directory if needed
    makedirs(dest, exist_ok=True)
    # list of all files to move
    files = [name for name in listdir(src)]
    # determine chunksize
    n_workers = 8
    chunksize = round(len(files) / n_workers)
    # create the process pool
    with ProcessPoolExecutor(n_workers) as exe:
        # split the move operations into chunks
        for i in range(0, len(files), chunksize):
            # select a chunk of filenames
            filenames = files[i:(i + chunksize)]
            # submit the batch move task
            _ = exe.submit(
                move_files, filenames, src, dest)

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
