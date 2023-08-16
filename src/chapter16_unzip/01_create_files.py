# SuperFastPython.com
# create a zip file containing many files
from random import random
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

# generate a line of mock data of 10 random data points
def generate_line():
    return ','.join([str(random()) for _ in range(10)])

# generate file data of 10K lines each with 10 values
def generate_file_data():
    # generate many lines of data
    lines = [generate_line() for _ in range(10000)]
    # convert to a single ascii doc with new lines
    return '\n'.join(lines)

# create a zip file
def main(num_files=1000):
    # create the zip file
    with ZipFile('testing.zip', 'w',
        compression=ZIP_DEFLATED) as handle:
        # create some files
        for i in range(num_files):
            # generate data
            data = generate_file_data()
            # create filenames
            filename = f'data-{i:04d}.csv'
            # save data file
            handle.writestr(filename, data)
            # report progress
            print(f'.added {filename}')
    print('Done')

# protect the entry point
if __name__ == '__main__':
    main()
