#!/usr/bin/env python


#import regex package
import re
# import permutation function
from itertools import permutations

# 1) read input data, create valid value for length of shortest route (or is there something like infty??)
puzzle_input = []
min_route_length = 0
with open("day09.txt", "r") as file:
	for line in file:
		vector_raw = []
		vector = []
		vector_raw = re.split('\s', line)
		vector.extend([vector_raw[0], vector_raw[2], int(vector_raw[4])])
		min_route_length += int(vector_raw[4])
		puzzle_input.append(vector)

# 2) get a set of all locations (uniqueness), prepare all permutations
locations = set()
possible_routes = []
for i in puzzle_input:
	locations.add(i[0])
	locations.add(i[1])
possible_routes = list(permutations(locations))
possible_routes = [list(element) for element in possible_routes]


# 3) calculate distance for each possible route and get minimum (same loop, saves at least a little bit)
# 3a) add solution for part 2 / longest path also within the same loop
def find_distance(start,end):
	for i in range(len(puzzle_input)):
		if (start == puzzle_input[i][0] and end == puzzle_input[i][1]) or (start == puzzle_input[i][1] and end == puzzle_input[i][0]):
			return puzzle_input[i][2]

max_route_length = 0

for route in possible_routes:
	distance = 0
	for location in range(len(route)-1):
		distance += find_distance(route[location],route[location+1])
	route.append(distance)
	if distance < min_route_length:
		min_route_length = distance
		shortest_route = route
	if distance > max_route_length:
		max_route_length = distance
		longest_route = route

# 4) have a nice output
print("The shortest route is\n", *shortest_route, sep = ":")
print("The longest route is\n", *longest_route, sep = ":")
