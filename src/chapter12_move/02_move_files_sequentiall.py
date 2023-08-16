# SuperFastPython.com
# move files from one directory to another sequentially
from os import makedirs
from os import listdir
from os.path import join
from shutil import move
from time import time

# move files from src to dest
def main(src='tmp', dest='tmp2'):
    # create the destination directory if needed
    makedirs(dest, exist_ok=True)
    # move all files from src to dest
    for filename in listdir(src):
        # create the path for the source
        src_path = join(src, filename)
        # create the path for the destination
        dest_path = join(dest, filename)
        # move source file to destination file
        move(src_path, dest_path)

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = time()
    # run the program
    main()
    # calculate the duration
    time_duration = time() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
