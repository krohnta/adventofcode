#!/usr/bin/env python

#--- Day 14: Reindeer Olympics ---
#This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.
#Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.
#For example, suppose you have the following Reindeer:
#* Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
#* Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
#After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.
#In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).
#Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

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
