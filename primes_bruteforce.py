#!/usr/bin/env python3

primes = [2,3]
candidate = 5

def is_prime(n):
    for x in range(2, int(n/2)):
        if n%x == 0:
            return False
    return True

while len(primes) < 10001:
    if is_prime(candidate):
        primes.append(candidate)
        print(len(primes), candidate)
    candidate += 1

print(len(primes), primes[-1])
