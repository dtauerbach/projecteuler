#!/usr/bin/env python
# author: dtauerbach

"""
Problem 204

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?
"""

def getPrimesLessThan(num):
    """
    >>> getPrimesLessThan(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    primes = [2]
    for i in range(2, num):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    return primes

def get_new_hammings(prime, new_hammings, hammings, max_num):
    return set(map(lambda x: prime*x if prime*x <= max_num else 1, new_hammings)).difference(hammings)

def computeLenHammings(prime_list, max_num):
    """
    >>> computeLenHammings([2,3,5], 10**8)
    1105
    """
    hammings = [1]
    new_hammings = [1]
    while True:
        old_hammings = set(hammings)
        cur_hammings = set([])
        for prime in prime_list:
            cur_hammings = get_new_hammings(prime, new_hammings, old_hammings, max_num).union(cur_hammings)
        if len(cur_hammings) == 0:
            return len(hammings)
        new_hammings = list(cur_hammings)
        hammings = old_hammings.union(cur_hammings)

hamming_primes = getPrimesLessThan(100)
print computeLenHammings(hamming_primes, 10**9)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
