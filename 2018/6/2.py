#!/usr/bin/python

import sys

def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

with open("input.txt", "r") as f:
    coordinates = map(lambda x: map(int, x.strip('\n').split(', ')), f.readlines())

x_coords = []
y_coords = []
for coordinate in coordinates:
    x_coords.append(coordinate[0])
    y_coords.append(coordinate[1])

max_x = max(x_coords)
max_y = max(y_coords)

region = 0
grid = [['.' for i in range(max_x)] for j in range(max_y)]

for y, _ in enumerate(grid):
    for x, _ in enumerate(grid[y]):
        distances = []
        for coordinate in coordinates:
            distances.append(manhattan_distance(coordinate, [x, y]))
        if sum(distances) < 10000:
            region += 1

print region
