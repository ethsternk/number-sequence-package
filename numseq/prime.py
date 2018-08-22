"""A collection prime-related functions."""


def is_prime(m):
    """returns a boolean indicating whether (m) is prime"""
    for i in range(2, m):
        if (m % i) == 0:
            return False
            break
    return True


def primes(n):
    """returns a list of primes less than (n)"""
    return [x for x in range(1, n) if is_prime(x)]
