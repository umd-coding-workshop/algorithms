#!/usr/bin/env python3

upper_bound = 200000
primes = []
candidates = set([n for n in range(2, upper_bound)])

while len(primes) < 10001:
    x = min(candidates)
    primes.append(x)
    print(len(primes), len(candidates))
    for multiple in range(2, int(upper_bound/2)):
        deletion = x * multiple
        print(deletion)
        if deletion in candidates:
            candidates.remove(deletion)
    
print(len(primes), primes[-1])
