#!/usr/bin/env python



# 1) read input file, but transfer into array for easier iteration later
puzzle_input = []
with open("day05.txt", "r") as file:
	for line in file:
		puzzle_input.append(line.rstrip())

# 2) check for a pair of any two letters that appear twice, I'm quite sure that my indices catch the overlapping part...
puzzle1 = []
for i in range(len(puzzle_input)):
	for j in range(len(puzzle_input[i])-3):
		if puzzle_input[i][j:j+2] in puzzle_input[i][j+2:]:
			puzzle1.append(puzzle_input[i])
#			print(puzzle_input[i], puzzle_input[i][j:j+2], puzzle_input[i][j+2:])
#			offsets are hard -.-
			break

# 3) check for one letter repeated with exactly one letter in between
puzzle2 = []
for i in range(len(puzzle1)):
	for j in range(len(puzzle1[i])-2):
		if puzzle1[i][j] == puzzle1[i][j+2]:
			puzzle2.append(puzzle1[i])
#			print(puzzle1[i], puzzle1[i][j], puzzle1[i][j+2])
			break


# n) have a nice output
print("Starting with", len(puzzle_input), "strings.")
print("Strings containing a pair of two letters:", len(puzzle1))
print("Of these: Strings repeated with exactly one character in between:", len(puzzle2))
#print("Examples:", puzzle2[0:5])
print("There are", len(puzzle2), "nice strings in the text file.")
