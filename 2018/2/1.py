#!/usr/bin/python

import sys

counts = {2:0, 3:0}
repetitions = {}
checksum = 0
with open("input.txt", "r") as f:
    ids = f.readlines()


for id in ids:
    repetitions = {}
    for letter in id:
        if letter in repetitions:
            repetitions[letter] += 1
        else:
            repetitions[letter] = 1
    if 2 in repetitions.values():
        counts[2] += 1
    if 3 in repetitions.values():
        counts[3] += 1
    checksum = counts[2] * counts[3]
print checksum
