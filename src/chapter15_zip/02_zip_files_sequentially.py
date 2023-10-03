# SuperFastPython.com
# create a zip file and add files sequentially
from os import listdir
from os.path import join
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from time import perf_counter

# create a zip file
def main(path='tmp'):
    # list all files to add to the zip
    files = [join(path,f) for f in listdir(path)]
    # open the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # add all files to the zip
        for filepath in files:
            # add file to the archive
            handle.write(filepath)

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
