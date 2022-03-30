import queue
import threading
import time


def process_queue(queue_to_process):
    while True:
        next_in_queue = queue_to_process.get()
        if next_in_queue == 'stop':
            break
        print('From queue', next_in_queue)
        time.sleep(0.1)


def main():
    my_queue = queue.Queue()
    thread = threading.Thread(target=process_queue, args=(my_queue,))
    thread.start()
    for a in range(1, 10):
        my_queue.put(input('Queue item:'))
    my_queue.put('stop')
    thread.join()


main()
