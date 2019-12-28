#!/usr/bin/env python


puzzle_input = []
with open("day01.txt", "r") as file:
	for line in file:
		puzzle_input.append([int(line.strip())])

fuel_requirements = 0
for i in range(len(puzzle_input)):
	fuel = puzzle_input[i][0]//3-2
	puzzle_input[i].append(fuel)
	fuel_requirements += fuel



### OUTPUT
print("The sum of the fuel requirements is", fuel_requirements)
