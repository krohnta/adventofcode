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

# 3) remove quotation marks at beginning and end of each line
puzzle1 = []
for i in range(len(puzzle_input)):
	puzzle1.append(puzzle_input[i][1:-1])

# 4) longest substring to be replaced would be the ASCII, so start with those; use regex; as I don't care about the text's meaning, just replace each ASCII character with a dash (-)
puzzle2 = []
for i in range(len(puzzle1)):
	puzzle2.append(re.sub("\\\\[x]{1}[0-9a-f]{2}", "-", puzzle1[i]))

# 5) replace \\ and \x; use regex; again, I don't care about any meaning of text, so replace them with a dash (-)
puzzle3 = []
for i in range(len(puzzle2)):
	puzzle3.append(re.sub('\\\\[\\\\"]{1}', '-', puzzle2[i]))

# 6) count the number of characters again
total_number_memory = 0
for i in puzzle3:
	total_number_memory += len(i)

# 7) have a nice output
print("The number of characters of code for string literals is", total_number_code, "\nand the number of characters in memory for the values of the strings is", total_number_memory, "\nwhich results in a difference of", total_number_code - total_number_memory)

### DEBUG OUTPUT
#print("Total number of characters of code for string literals:", total_number_code)
#print("Raw data:", puzzle_input[0:3])
#print("Strip double-quotes from each entry:", puzzle1[0:3])
#print("Replace ASCII encoding with A:", puzzle2[0:3])
#print("Replace escaped backslashes and double-quotes:", puzzle3[0:3])
