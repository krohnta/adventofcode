#!/usr/bin/env python

# Due to my try-except abomination in my initial solution to this puzzle, I cannot use it for the following puzzles which rely on the Intcode Computer from day 2. So this needs to be refactored (probably more than once...).

# import regex package
import re


# read input into list of integers
with open("day02.txt", "r") as file:
	for entry in file.readlines():
		puzzle_input = re.split(',', entry)

puzzle_input = [int(i) for i in puzzle_input]
copy_input = puzzle_input[:]

# replace position 1 with 12 and position 2 with 2

puzzle_input[1] = 12
puzzle_input[2] = 2


### DEBUG INPUT ###
#puzzle_input = [1,1,1,4,99,5,6,0,99]

# define actions
def calc_output(program):
	position = 0

	while True:
		opcode = program[position]

		if opcode == 99:
#			print(program[0])
			return program[0]
			break
		
		pos1 = program[position+1]
		pos2 = program[position+2]
		pos3 = program[position+3]


		if opcode == 1:
			try:
				program[pos3] = program[pos1] + program[pos2]
			except IndexError:
				break

		if opcode == 2:
			try:
				program[pos3] = program[pos1] * program[pos2]
			except IndexError:
				break

		position += 4



print("Solution for part 1:", calc_output(puzzle_input))

for i in range(100):
	for j in range(100):
		copy = copy_input[:]
		copy[1] = i
		copy[2] = j
#		print(calc_output(copy))
		if calc_output(copy) == 19690720:
			print("Solution for part 2: ", i, j, sep="")
