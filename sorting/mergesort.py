#!/usr/bin/env python3

import sys
import random

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
    
print(len(data))

lists = [[item] for item in data]

while len(lists) > 1:
    new_lists = []
    if len(lists)%2 != 0:
        new_lists.append(lists.pop())
    for n in range(0, len(lists)-1, 2):
        a = lists[n]
        b = lists[n+1]
        new_lists.append(merge(a,b))
    lists = new_lists

result = lists[0]

print(len(result), result)
