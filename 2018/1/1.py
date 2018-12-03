#!/usr/bin/python

import sys

with open("input.txt", "r") as f:
    changes = f.readlines()
frequency = 0

for val in changes:
    frequency = frequency + int(val)

print frequency
