#!/usr/bin/env python



# regex package:
import re

# 1) read puzzle input file, use an array, otherwise line-endings will interfere with proper association
puzzle_input = []
with open("day08.txt", "r") as file:
	for line in file:
		puzzle_input.append(line.rstrip())

# 2) get total number of characters of code for string literals (before doing anything with the data)
total_number_code = 0
for i in puzzle_input:
	total_number_code += len(i)

# 3) no need for splitting as in part 1, so just replace ALL THE BACKSLASHES AND DOUBLE-QUOTES \o/ \o/ \o/ (...with dashes (--) of course...)
puzzle1 = []
for i in range(len(puzzle_input)):
	puzzle1.append(re.sub('[\\\\"]{1}', '--', puzzle_input[i]))

# 4) count the number of characters again, add 2 for the non-replaced double-quotes at the beginning and end of each array element (...still don't care about the text itself, just counting)
total_number_memory = 0
for i in puzzle1:
	total_number_memory += len(i)+2

# 7) have a nice output
print("The number of characters of code for string literals is", total_number_code, "\nand the number of characters in memory for the values of the strings is", total_number_memory, "\nwhich results in a difference of", total_number_memory - total_number_code)
