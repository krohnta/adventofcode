#!/usr/bin/env python


puzzle_input = []
with open("day01.txt", "r") as file:
	for line in file:
		puzzle_input.append([int(line.strip())])

### DEBUG
#puzzle_input = [[100756]] # results in 50346
fuel_requirements = 0

for i in range(len(puzzle_input)):
	fuel = puzzle_input[i][0]
	while fuel > 0:
		fuel = fuel//3-2
		if fuel < 0:
			break
		fuel_requirements += fuel



### OUTPUT
print("The sum of the fuel requirements is", fuel_requirements)
