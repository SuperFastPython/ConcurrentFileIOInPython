# SuperFastPython.com
# write many data files concurrently with processes
from os import makedirs
from os.path import join
from concurrent.futures import ProcessPoolExecutor
from time import time

# save data to a file
def save_file(filepath, data):
    # open the file
    with open(filepath, 'w') as handle:
        # save the data
        handle.write(data)

# generate a csv with 10 values per line and 5k lines
def generate_file(ident, n_values=10, n_lines=5000):
    # generate many lines of data
    data = list()
    for i in range(n_lines):
        # generate a list of numeric values as strings
        line = [str(ident+i+j) for j in range(n_values)]
        # convert list to string, separated by commas
        data.append(','.join(line))
    # convert list of lines to a string, add new lines
    return '\n'.join(data)

# generate and save a file
def generate_and_save(path, identifier):
    # generate data
    data = generate_file(identifier)
    # create a unique filename
    filepath = join(path, f'data-{identifier:04d}.csv')
    # save data file to disk
    save_file(filepath, data)

# generate many data files in a directory
def main(path='tmp', n_files=5000):
    # create a local directory to save files
    makedirs(path, exist_ok=True)
    # create the process pool
    with ProcessPoolExecutor(8) as exe:
        # submit tasks to generate files
        _ = [exe.submit(
            generate_and_save, path, i) for i in range(
            n_files)]

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
