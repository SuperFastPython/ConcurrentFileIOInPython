# SuperFastPython.com
# append file from multiple threads unexpected behavior
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor

# task that blocks for a moment and write to a file
def task(idt, file_handle):
    # block for a moment
    value = random()
    sleep(value)
    # write to a file
    file_handle.write(
        f'Task {idt} blocked for {value} of a second.\n')

# write to a file from multiple threads
def main():
    # open a file
    with open(
        'results.txt', 'a', encoding='utf-8') as hdl:
        # create the thread pool
        with ThreadPoolExecutor(1000) as exe:
            # dispatch all tasks
            _ = [exe.submit(
                task, i, hdl) for i in range(10000)]
    # wait for all tasks to complete
    print('Done.')

# protect the entry point
if __name__ == '__main__':
    main()
