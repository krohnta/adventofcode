#!/usr/bin/env python



# regex package to parse input data
import re

# 1) read puzzle input and parse it for getting name, velocity, duration, resttime, add a 0 for counting points later
puzzle_input = []
with open("day14.txt", "r") as file:
	for line in file:
		reindeer_raw = []
		reindeer = []
		reindeer_raw = re.split('\s', line)
		reindeer.extend([reindeer_raw[0], int(reindeer_raw[3]), int(reindeer_raw[6]), int(reindeer_raw[13]), 0])
		puzzle_input.append(reindeer)
# each reindeer entry looks like this: ['Rudolph', 22, 8, 165, 0]

# 2) create movement array for each reindeer
def calc_movement(reindeer):
	movement = []
	while len(movement) < 2503:
		movement.extend([reindeer[1]] * reindeer[2])
		movement.extend([0] * reindeer[3])
	return movement

# 3) calculate distance at every second
def calc_distance(movement):
	distance = 0
	current_distance = []
	for i in range(2503):
		distance += movement[i]
		current_distance.append(distance)
	return current_distance

# 4) calculate distance array for each reindeer
for reindeer in puzzle_input:
	reindeer.append(calc_distance(calc_movement(reindeer)))
# each reindeer entry now looks like this: ['Rudolph', 22, 8, 165, 0, [22, 44, 66, ...]]

# 5) calculate the max distance at each point of time and award points
max_distance = [0]*2503
for i in range(2503):
	for reindeer in puzzle_input:
		if reindeer[5][i] > max_distance[i]:
			max_distance[i] = reindeer[5][i]

# I somehow get issues if I do not run through my list twice. There should be a better solution for this, but I don't get it right now :(
for i in range(2503):
	for reindeer in puzzle_input:
		if reindeer[5][i] == max_distance[i]:
			reindeer[4] += 1


# 6) get the winner
max_points = 0
winner = ""
for reindeer in puzzle_input:
	if reindeer[4] > max_points:
		max_points = reindeer[4]
		winner = reindeer[0]


# 7) have a nice output
print("The winning reindeer is ", winner, " with ", max_points, " points.", sep="")
