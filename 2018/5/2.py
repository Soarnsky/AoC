#!/usr/bin/python

import sys


units = []
with open("input.txt", "r") as f:
    fd = f.read().strip('\n')
    units.extend(fd)

polarity = {chr(i):chr(i-32) for i in range(97, 123)}
polarity.update({chr(i):chr(i+32) for i in range(65, 91)})

bad_units = [[chr(i), chr(i+32)] for i in range(65, 91)]

shortest_length = len(units)
for bad_unit in bad_units:
    polymer = [u for u in units if u not in bad_unit]

    loc = 0
    last_unit = len(units) - 1
    while loc != last_unit:
        if polarity[polymer[loc]] == polymer[loc+1]:
            del polymer[loc:loc+2]
            if loc != 0:
                loc -= 1
        else:
            loc += 1
        last_unit = len(polymer) - 1
    if len(polymer) < shortest_length:
        shortest_length = len(polymer)
print shortest_length
