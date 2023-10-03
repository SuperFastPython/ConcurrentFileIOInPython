# SuperFastPython.com
# move files from one dir to another with 100 threads
from os import makedirs
from os import listdir
from os.path import join
from shutil import move
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

# move a file from source to destination
def move_file(filename, src, dest):
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
    # create the thread pool
    with ThreadPoolExecutor(100) as exe:
        # submit all file move tasks
        _ = [exe.submit(move_file, name, src, dest)
            for name in listdir(src)]

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
