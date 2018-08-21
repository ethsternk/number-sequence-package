def is_prime(m):
    for i in range(2, m):
        if (m % i) == 0:
            return False
            break
    return True


def primes(n):
    return [x for x in range(1, n) if is_prime(x)]
