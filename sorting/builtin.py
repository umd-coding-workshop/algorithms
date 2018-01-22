#!/usr/bin/env python3

''' Use the python built-in sort for comparison 
    against other implementations.'''

import sys

def merge(a, b):
    sorted = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            sorted.append(a.pop(0))
        else:
            sorted.append(b.pop(0))
    if len(a) > 0:
        sorted.extend(a)
    elif len(b) > 0:
        sorted.extend(b)
    return sorted


with open(sys.argv[1], 'r') as datafile:
    data = [int(line.split('\t')[0].strip()) for line in datafile.readlines()]

result = sorted(data)
print(len(result), result)
