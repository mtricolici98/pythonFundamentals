import threading
import time


def add_1(result, lock=None):
    result += '1'
    try:
        if lock:
            lock.acquire()
    finally:
        if lock:
            lock.release()


def main_single():
    start_time = time.time()
    result = [1]
    for a in range(5):
        add_1(result)
    print(result)


def main_multiple():
    start_time = time.time()

    threads = []
    lock = threading.Lock()
    result = '1'
    for a in range(5):
        threads.append(threading.Thread(target=add_1, args=(result,)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(result)


if __name__ == '__main__':
    main_single()
    main_multiple()
