# SuperFastPython.com
# write to a file from multiple threads using a queue
from time import sleep
from random import random
from queue import Queue
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# task that blocks for a moment and write to a file
def task(identifier, queue):
    # block for a moment
    value = random()
    sleep(value)
    # push data into the queue
    queue.put(f'Task {identifier} blocked for ' \
        f'{value} of a second.\n')

# consume messages from the queue and write to the file
def file_writer(queue, file_handle):
    # loop forever
    while True:
        # retrieve a messages from the queue
        message = queue.get()
        # write the message to file
        file_handle.write(message)
        # mark this ask as done
        queue.task_done()

# write to a file from multiple threads
def main():
    # open a file
    with open(
        'results.txt', 'a', encoding='utf-8') as hdl:
        # create a queue for collecting message to write
        queue = Queue()
        # start a daemon thread to write queued messages
        writer = Thread(target=file_writer,
            args=(queue, hdl), daemon=True)
        writer.start()
        # create the thread pool
        with ThreadPoolExecutor(1000) as exe:
            # dispatch all tasks
            _ = [exe.submit(
                task, i, queue) for i in range(10000)]
        # wait for message to be consumed
        queue.join()
    print('Done.')

# protect the entry point
if __name__ == '__main__':
    main()
