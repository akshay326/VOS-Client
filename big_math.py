from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def primes_till(n):
    """ Returns  a list of primes < n """
    sieve = []

    for i in range(int(sqrt(n))):
        sieve.append(True)

    for i in range(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n/2) if sieve[i]]
