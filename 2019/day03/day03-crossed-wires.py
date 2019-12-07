#!/usr/bin/env python

# I found a nice solution for 2015/day03 which does not require the whole grid but only appends "visited" coordinates. Maybe I can get that one to work for this problem?!?


# import regex package
import re

# 1) read input into list of integers
puzzle_input = []
with open("day03.txt", "r") as file:
	for line in file:
		puzzle_input.append(re.split(",", line.rstrip()))

movement = []
for i in puzzle_input:
	movement_raw = []
	for j in i:
		move = int(j[1:])
		if j[0] == "U":
			movement_raw.append("U"*move)
		elif j[0] == "D":
			movement_raw.append("D"*move)
		elif j[0] == "L":
			movement_raw.append("L"*move)
		elif j[0] == "R":
			movement_raw.append("R"*move)
	movement.append([''.join(movement_raw)])

# Derived from a solution to 2015/day03 - I understand the math behind it but I would never have come up with such an idea. Too much thinking about the whole matrix instead of just a sparse one I guess.

coords_a = [0,0,0]
coord_list_a = ["0,0"]
dist_list_a = ["0,0;0"]
for i in movement[0][0]:
	if i == "U":
		coords_a[1] += 1
		coords_a[2] += 1
	elif i == "D":
		coords_a[1] -= 1
		coords_a[2] += 1
	elif i == "R":
		coords_a[0] += 1
		coords_a[2] += 1
	elif i == "L":
		coords_a[0] -= 1
		coords_a[2] += 1
	coord_list_a.append(str(coords_a[0])+","+str(coords_a[1]))
	dist_list_a.append(str(coords_a[0])+","+str(coords_a[1])+";"+str(coords_a[2]))

coords_b = [0,0,0]
coord_list_b = ["0,0"]
dist_list_b = ["0,0;0"]
for i in movement[1][0]:
	if i == "U":
		coords_b[1] += 1
		coords_b[2] += 1
	elif i == "D":
		coords_b[1] -= 1
		coords_b[2] += 1
	elif i == "R":
		coords_b[0] += 1
		coords_b[2] += 1
	elif i == "L":
		coords_b[0] -= 1
		coords_b[2] += 1
	coord_list_b.append(str(coords_b[0])+","+str(coords_b[1]))
	dist_list_b.append(str(coords_b[0])+","+str(coords_b[1])+";"+str(coords_b[2]))

# Now, I have two arrays with lots of coordinates in which I have to
# a) identify the ones which appear in both lists (=crossings)
# b) of those identify the one which is closest to ["0,0"] by Manhattan distance
# Part b) should be easy as the coordinates all contain the distance

# After 2 min googling: of course, there's a method for that in Python m)
crossings = list(set(coord_list_a).intersection(coord_list_b))
#print(crossings[0:5])
# looks like: ['-540,276', '-1134,-1659', '-1134,-1602', '2402,-649', '2538,-488']
crossings.sort()

#print(dist_list_a[0:5])
# looks like: ['0,0,0', '1,0,1', '2,0,2', '3,0,3', '4,0,4']


# part b) via brute-force: calculate all Manhattan distances and take the minimum of them.
distances = []
for location in crossings:
	distances.append(location.split(","))


# solution for Part I: find minimum Manhattan distance
min_dist = []
for i in distances:
	i[0] = int(i[0])
	i[1] = int(i[1])
	manhattan_dist = abs(i[0])+abs(i[1])
	min_dist.append(manhattan_dist)

min_dist.sort()
print("Minimal Manhattan distance is", min_dist[1])

# solution for Part II: find minimum common steps
# This is no longer brute force but more like nuclear warfare in O(holy fuck) - but it works. I'm sorry.
split_dist_a = []
for location in dist_list_a:
	split_dist_a.append(location.split(";"))

split_dist_b = []
for location in dist_list_b:
	split_dist_b.append(location.split(";"))

	
store_steps = distances[:]
for location in range(len(crossings)):
	for dist in split_dist_a:
		if crossings[location] == dist[0]:
			store_steps[location].append(int(dist[1]))
	for dist in split_dist_b:
		if crossings[location] == dist[0]:
			store_steps[location][2] += int(dist[1])

store_steps.sort(key = lambda x: x[2])

print("Minimal combined steps are", store_steps[1][2])

### DEBUG OUTPUT
#print(crossings[0:4])
#print(distances[0:3])
#print(split_dist_a[0:5])
#print(split_dist_b[0:5])
#print(store_steps[0:5])

#print(len(set(coord_list_a)))
#print(len(set(coord_list_b)))
#print(len(set(crossings)))
#print(crossings[0:5])
#print(distances[0:5])
#steps_a_raw = []
#for location in dist_list_a:
#	steps_a_raw.append(location.split(","))
#steps_a = []
#for steps in steps_a_raw:
#	for i in steps:
#		steps_a.append(i.split(","))
#
#steps_b_raw = []
#for location in dist_list_b:
#	steps_b_raw.append(location.split(","))
#steps_b = []
#for steps in steps_b_raw:
#	for i in steps:
#		steps_b.append(i.split(","))
