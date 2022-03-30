import time
from threading import Thread


def write_soemthign():
    while True:
        print('Something')
        time.sleep(5)


def main():
    a = Thread(target=write_soemthign)
    a.start()
    while True:
        print(input())
    a.join()


main()
