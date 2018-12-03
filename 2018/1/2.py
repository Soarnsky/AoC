#!/usr/bin/python

import sys

frequencies = {0:""}
with open("input.txt", "r") as f:
    changes = f.readlines()
frequency = 0
repeated = False

while not repeated:
    for val in changes:
        frequency = frequency + int(val)
        if frequency in frequencies:
            repeated = True
            break
        else:
            frequencies[frequency] = ""
print frequency
