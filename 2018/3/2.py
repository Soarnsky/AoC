#!/usr/bin/python

import sys
import re

with open("input.txt", "r") as f:
    claims = f.readlines()

fabric = [['.' for i in range(1000)] for j in range(1000)]

nonoverlap = {}
for claim in claims:
    p = "^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$"
    claim_num = int(re.match(p, claim).group(1))
    dist_x = int(re.match(p, claim).group(2))
    dist_y = int(re.match(p, claim).group(3))
    size_x = int(re.match(p, claim).group(4))
    size_y = int(re.match(p, claim).group(5))
    overlap = False
    for i in range (0, size_x):
        for j in range (0, size_y):
            x = dist_x + i
            y = dist_y + j
            if fabric[x][y] == '.':
                fabric[x][y] = claim_num
            else:
                nonoverlap.pop(fabric[x][y], None)
                fabric[x][y] = 'X'
                overlap = True
    if not overlap:
        nonoverlap[claim_num] = ''
print nonoverlap.keys()[0]
