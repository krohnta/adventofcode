#!/usr/bin/env python


# import regex package
import re


# 1) read input into list of integers
with open("day02.txt", "r") as file:
	for entry in file.readlines():
		puzzle_input = re.split(',', entry)

puzzle_input = [int(i) for i in puzzle_input]


# 2) replace position 1 with 12 and position 2 with 2

puzzle_input[1] = 12
puzzle_input[2] = 2


# 3) define function for actions

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


# 4) run through the input data

for pos in range(0,len(puzzle_input),4):
	#print(puzzle_input[pos])
	try:
		opcode_action(puzzle_input,pos)
	except:
		print("The final value at position 0 is", puzzle_input[0])



### DEBUG OUTPUT
#print(puzzle_input)
#print(opcode_action([1,0,0,0,99],0))
#print("[2,0,0,0,99]")
#print(opcode_action([2,3,0,3,99],0))
#print("[2,3,0,6,99]")
#print(opcode_action([2,4,4,5,99,0],0))
#print("[2,4,4,5,99,9801]")
#print(opcode_action([1,9,10,3,2,3,11,0,99,30,40,50],0))
#print("[1,9,10,70,2,3,11,0,99,30,40,50]")
