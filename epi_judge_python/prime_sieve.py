from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    ret = [False for i in range(n+1)]
    ret[0] = True
    ret[1] = True
    for i in range(n+1):
        if not ret[i]:
            ct = 2
            while ct * i <= n:
                ret[ct*i] = True
                ct += 1
    return [idx for idx, i in enumerate(ret) if not i]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
