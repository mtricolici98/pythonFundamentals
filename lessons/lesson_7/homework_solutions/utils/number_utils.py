def is_number_prime(number):
    # No number above number / 2 will be divisible, so we don't have to check them
    for a in range(2, (number // 2) + 1):
        if number % a == 0:
            # Number has a divisor, not prime
            return False
    # No divisors found above, number is prime
    return True


def number_is_perfect(nr_to_check):
    sum = 0
    for nr in range(1, (nr_to_check // 2) + 1):
        if nr_to_check % nr == 0:
            # Adding the sum of divisors
            sum += nr
    return sum == nr_to_check  # Sum is equal to the number, this means number is perfect
