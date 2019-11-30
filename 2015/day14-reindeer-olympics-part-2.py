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

#--- Part Two ---
#Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.
#Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.
#Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.
#After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).
#Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?


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
