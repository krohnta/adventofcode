#!/usr/bin/env python

# modify the Intcode computer from day 2 with
# - opcode 3 => save input to position
# - opcode 4 => output value at position

# support for parameter mode


# import regex package
import re


# read input into list of integers
#with open("../day02/day02.txt", "r") as file:
with open("day05.txt", "r") as file:
	for entry in file.readlines():
		puzzle_input = re.split(',', entry)

puzzle_input = [int(i) for i in puzzle_input]
copy_input = puzzle_input[:]


# parameter mode
def calc_mode(parameter):
	opcode = int(str(parameter)[-2:])

	try:
		mode1 = int(str(parameter)[-3])
	except IndexError:
		mode1 = 0
	
	try:
		mode2 = int(str(parameter)[-4])
	except IndexError:
		mode2 = 0

	try:
		mode3 = int(str(parameter)[-5])
	except IndexError:
		mode3 = 0

	return [opcode, mode1, mode2, mode3]

# define actions
def calc_output(program,instruction):
	position = 0
	while True:
#		print("pos at loop start: ", position)
		opcode = calc_mode(program[position])[0]

		if opcode == 99:
			print("HALT")
#			return program
			break
		
		mode_value = calc_mode(program[position])

		pos1 = program[position+1]
		mod_pos1 = mode_value[1]

		pos2 = program[position+2]
		mod_pos2 = mode_value[2]

		if opcode == 3:
			try:
				program[pos1] = instruction
			except IndexError:
				break
			position += 2

		if opcode == 4:
			if mod_pos1 == 0:
				print("out =", program[pos1])
			else:
				print("out =", pos1)
			position += 2

		if opcode == 1 or opcode == 2:
			if mod_pos1 == 0:
				try:
					val1 = program[pos1]
				except IndexError:
					break
			else:
				val1 = pos1

			if mod_pos2 == 0:
				try:
					val2 = program[pos2]
				except IndexError:
					break
			else:
				val2 = pos2

			if opcode == 1:
				val3 = val1 + val2
				try:
					pos3 = program[position+3]
					program[pos3] = val3
				except IndexError:
					break
				position += 4

			if opcode == 2:
				val3 = val1 * val2
				try:
					pos3 = program[position+3]
					program[pos3] = val3
				except IndexError:
					break
				position += 4



### DEBUG OUTPUT ###
#print(calc_mode(1032))
#print(calc_output(puzzle_input))
#print(calc_output([1002,4,3,4,33]))
#print(calc_output([1101,100,-1,4,0],1))
#print(calc_output([3,0,4,0,99],1))
print(calc_output(puzzle_input,1))
# ORIGINAL OUTPUT FROM DAY2 STILL VALID??
puzzle_input[1] = 12
puzzle_input[2] = 2
#print(calc_output(puzzle_input,1)[0])
