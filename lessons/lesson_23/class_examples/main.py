import os
from multiprocessing import Process, Manager


def add_items(f, t, to_list):
    for a in range(f, t):
        to_list.append(a)
    print(f"From child {os.getpid()} {to_list}")


def main():
    with Manager() as manager:
        # Creating a list inside our shared storage
        results = manager.list()
        # Creating processes
        p1 = Process(target=add_items, args=(0, 10, results))
        p2 = Process(target=add_items, args=(10, 20, results))
        # Starting processes
        p1.start()
        p2.start()
        # Waiting for processes to finish
        p1.join()
        p2.join()
        print(f"From main {os.getpid()} {results}")


if __name__ == '__main__':
    main()
