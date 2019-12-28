#!/usr/bin/env python



# import regex package
import re


# 1) read input into list of integers
with open("day02.txt", "r") as file:
	for entry in file.readlines():
		puzzle_input = re.split(',', entry)

puzzle_input = [int(i) for i in puzzle_input]
goal_output = 19690720



# 2) define function for actions

def opcode_action(program,position):
	opcode = program[position]
	pos1 = program[position+1]
	pos2 = program[position+2]
	pos3 = program[position+3]
	if opcode == 99:
		return False
	elif opcode == 1:
		output = program[pos1] + program[pos2]
		program[pos3] = output
		return True
	elif opcode == 2:
		output = program[pos1] * program[pos2]
		program[pos3] = output
		return True


# 3) run through the input data while varying the input parameters from 0..99

def calc_output(copy_data):
	for pos in range(0,len(copy_data),4):
		try:
			opcode_action(copy_data,pos)
		except:
			if copy_data[0] == goal_output:
				noun = copy_data[1]
				verb = copy_data[2]
				print("Wanted configuration is", noun, "and", verb, "with answer", 100*noun+verb)
			else:
				break



for i in range(100):
	for j in range(100):
		puzzle_input_new = [i for i in puzzle_input]
		puzzle_input_new[1] = i
		puzzle_input_new[2] = j
		calc_output(puzzle_input_new)

