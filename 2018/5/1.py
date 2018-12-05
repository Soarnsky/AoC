#!/usr/bin/python

import sys


units = []
with open("input.txt", "r") as f:
    fd = f.read().strip('\n')
    units.extend(fd)

polarity = {chr(i):chr(i-32) for i in range(97, 123)}
polarity.update({chr(i):chr(i+32) for i in range(65, 91)})

loc = 0
last_unit = len(units) - 1
while loc != last_unit:
    if polarity[units[loc]] == units[loc+1]:
        del units[loc:loc+2]
        if loc != 0:
            loc -= 1
    else:
        loc += 1
    last_unit = len(units) - 1
print len(units)
