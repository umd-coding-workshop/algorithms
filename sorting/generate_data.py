#!/usr/bin/env python3

'''Print random integers using the following arguments:
    (1) lowest possible integer
    (2) highest possible integer
    (3) number of integers to print
  Use redirection to send the output to a file for use in testing.'''

from random import randint as randint
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])
num = int(sys.argv[3])

result = []

while len(result) < num:
    result.append(randint(min,max))

print('\n'.join([str(n) for n in result]))
