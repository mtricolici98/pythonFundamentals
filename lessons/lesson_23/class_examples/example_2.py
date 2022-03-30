import multiprocessing
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


def count_prime(from_nr, to_nr, storage):
    temp_storage = []
    for a in range(from_nr, to_nr):
        if is_prime(a):
            temp_storage.append(a)
    storage.extend(temp_storage)
    print(f'Process from {from_nr} to {to_nr} finished')


def main_multiple():
    with multiprocessing.Manager() as manager:
        start_time = time.time()
        list_of_prime = manager.list()
        # Creating the processes
        process_to_100000 = multiprocessing.Process(target=count_prime, args=(0, 1000000, list_of_prime))
        process_from_100000 = multiprocessing.Process(target=count_prime, args=(1000000, 2000000, list_of_prime))
        process_from_200000 = multiprocessing.Process(target=count_prime, args=(2000000, 3000000, list_of_prime))
        # Starting each process
        process_to_100000.start()
        process_from_100000.start()
        process_from_200000.start()
        # waiting for each process to finish
        process_to_100000.join()
        process_from_100000.join()
        process_from_200000.join()
        print(len(list_of_prime))
        print('Elapsed for multiprocess', time.time() - start_time)


if __name__ == '__main__':
    main_multiple()
