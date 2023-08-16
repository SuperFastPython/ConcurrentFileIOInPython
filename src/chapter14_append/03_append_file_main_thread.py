# SuperFastPython.com
# write to a file from multiple threads from main
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# task that blocks for a moment and write to a file
def task(idt):
    # block for a moment
    value = random()
    sleep(value)
    # return data to write
    return f'Task {idt} blocked for ' \
        f'{value} of a second.\n'

# write to a file from multiple threads
def main():
    # open a file
    with open(
        'results.txt', 'a', encoding='utf-8') as hdl:
        # create the thread pool
        with ThreadPoolExecutor(1000) as exe:
            # dispatch all tasks
            futures = [exe.submit(
                task, i) for i in range(10000)]
            # process results as tasks are completed
            for future in as_completed(futures):
                # retrieve result to write
                result = future.result()
                # write to file
                hdl.write(result)
    # wait for all tasks to complete
    print('Done.')

# protect the entry point
if __name__ == '__main__':
    main()
