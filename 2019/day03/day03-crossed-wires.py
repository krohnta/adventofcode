#!/usr/bin/env python

# I found a nice solution for 2015/day03 which does not require the whole grid but only appends "visited" coordinates. Maybe I can get that one to work for this problem?!?


# import regex package
import re

# 1) read input into list of integers
puzzle_input = []
with open("day03.txt", "r") as file:
### DEBUG INPUT
#with open("day03-test1.txt", "r") as file:
	for line in file:
		puzzle_input.append(re.split(",", line.rstrip()))

# 2) get size of grid (similar to 2015/day03), but as no two movements go to the same direction, I need a max instead of a sum
min_ud_counter = 0
max_ud_counter = 0
min_lr_counter = 0
max_lr_counter = 0
movement = []


# FIXME my grid is too small :( I need a better method for calculating the dimension, max is wrong
for i in puzzle_input:
	movement_raw = []
	for j in i:
		move = int(j[1:])
		if j[0] == "U":
			movement_raw.append("U"*move)
			if move > max_ud_counter:
				max_ud_counter += move
		elif j[0] == "D":
			movement_raw.append("D"*move)
			if -move < min_ud_counter:
				min_ud_counter -= move
		elif j[0] == "L":
			movement_raw.append("L"*move)
			if -move < min_lr_counter:
				min_lr_counter -= move
		elif j[0] == "R":
			movement_raw.append("R"*move)
			if move > max_lr_counter:
				max_lr_counter += move
	movement.append([''.join(movement_raw)])

# Derived from a solution to 2015/day03 - I understand the math behind it but I would never have come up with such an idea. Too much thinking about the whole matrix instead of just a sparse one I guess.

coords_a = [0,0]
coord_list_a = ["0,0"]
for i in movement[0][0]:
	if i == "U":
		coords_a[1] += 1
	elif i == "D":
		coords_a[1] -= 1
	elif i == "R":
		coords_a[0] += 1
	elif i == "L":
		coords_a[0] -= 1
	coord_list_a.append(str(coords_a[0])+","+str(coords_a[1]))

coords_b = [0,0]
coord_list_b = ["0,0"]
for i in movement[1][0]:
	if i == "U":
		coords_b[1] += 1
	elif i == "D":
		coords_b[1] -= 1
	elif i == "R":
		coords_b[0] += 1
	elif i == "L":
		coords_b[0] -= 1
	coord_list_b.append(str(coords_b[0])+","+str(coords_b[1]))

# Now, I have two arrays with lots of coordinates in which I have to
# a) identify the ones which appear in both lists (=crossings)
# b) of those identify the one which is closest to ["0,0"] by Manhattan distance
# Part b) should be easy as the coordinates all contain the distance

# After 2 min googling: of course, there's a method for that in Python m)
crossings = list(set(coord_list_a).intersection(coord_list_b))

# part b) via brute-force: calculate all Manhattan distances and take the minimum of them.
distances = []
for location in crossings:
	distances.append(location.split(","))

min_dist = []
for i in distances:
	i[0] = int(i[0])
	i[1] = int(i[1])
	manhattan_dist = abs(i[0])+abs(i[1])
	min_dist.append(manhattan_dist)

min_dist.sort()


### DEBUG OUTPUT
#print(len(set(coord_list_a)))
#print(len(set(coord_list_b)))
#print(len(set(crossings)))
#print(crossings[0:5])
#print(distances[0:5])
print(min_dist[1])
