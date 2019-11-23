#!/usr/bin/env python

#--- Day 8: Matchsticks ---
# Once again, part 2 is not an easy transformation out of part 1, therefore a new file for part 2:
#--- Part Two ---
#Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.
#For example:
#* "" encodes to "\"\"", an increase from 2 characters to 6.
#* "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
#* "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
#* "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
#Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.


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
