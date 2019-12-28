#!/usr/bin/env python


# regex package to parse input data
import re

# 1) read puzzle input and parse it for getting name, velocity, duration, resttime
puzzle_input = []
with open("day14.txt", "r") as file:
	for line in file:
		reindeer_raw = []
		reindeer = []
		reindeer_raw = re.split('\s', line)
		reindeer.extend([reindeer_raw[0], int(reindeer_raw[3]), int(reindeer_raw[6]), int(reindeer_raw[13])])
		puzzle_input.append(reindeer)
# each reindeer entry looks like this: ['Rudolph', 22, 8, 165]

# 2)create movement array for each reindeer and calculate distance during 2503 seconds
def calculate_distance(reindeer):
	movement = []
	while len(movement) < 2503:
		movement.extend([reindeer[1]] * reindeer[2])
		movement.extend([0] * reindeer[3])
	distance = 0
	for i in range(2503):
		distance += movement[i]
	return distance

for reindeer in puzzle_input:
	reindeer.append(calculate_distance(reindeer))

# 3) find maximum distance over all reindeers
max_distance = 0
winner = ""
for reindeer in puzzle_input:
	if reindeer[4] > max_distance:
		max_distance = reindeer[4]
		winner = reindeer[0]

# 4) have a nice output
print("The winning reindeer is ", winner, ", and it traveled a distance of ", max_distance, "km.", sep="")
