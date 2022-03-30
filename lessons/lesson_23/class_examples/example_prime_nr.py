import queue
import threading
import time


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def count_prime(from_nr, to_nr):
    temp_storage = []
    for a in range(from_nr, to_nr):
        if is_prime(a):
            temp_storage.append(a)
    return len(temp_storage)


def process_request(number, lock):
    count = count_prime(0, number)
    lock.acquire()
    print(F"Prime numbers till {number} are: {count}")
    lock.release()


def main():
    threads = []
    lock = threading.Lock()
    while True:
        val = input("Stuff")
        if val == '-1':
            break
        thread = threading.Thread(target=process_request, args=(int(val), lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


main()
