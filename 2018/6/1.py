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

areas = {i:0 for i in range(len(coordinates))}
grid = [['.' for i in range(max_x)] for j in range(max_y)]

for y, _ in enumerate(grid):
    for x, _ in enumerate(grid[y]):
        distance = max(max_x, max_y)
        closest_coord = -1
        for c, coordinate in enumerate(coordinates):
            new_distance = manhattan_distance(coordinate, [x, y])
            if new_distance < distance:
                distance = new_distance
                closest_coord = c
            elif new_distance == distance:
                closest_coord = -1

        if closest_coord != -1:
            grid[y][x] = closest_coord
            areas[closest_coord] += 1

infinite_area = []
for y, _ in enumerate(grid):
    for x, coord in enumerate(grid[y]):
        if x == 0 or x == max_x-1 or y == 0 or y == max_y-1:
            if coord not in infinite_area:
                infinite_area.append(coord)

non_infinite_areas = areas.copy()
for coord in areas:
    if coord in infinite_area:
        non_infinite_areas.pop(coord)

print max(non_infinite_areas.values())
