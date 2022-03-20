from constants import SKIP_RANGE


def calculate_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n):
            primes.append(n)
    return primes


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if num % n != 0 and num not in SKIP_RANGE:
                continue
            else:
                return False
    return True

