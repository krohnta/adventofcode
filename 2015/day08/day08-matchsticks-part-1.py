#!/usr/bin/env python

#--- Day 8: Matchsticks ---
#Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.
#It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.
#However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.
#For example:
#* "" is 2 characters of code (the two double quotes), but the string contains zero characters.
#* "abc" is 5 characters of code, but 3 characters in the string data.
#* "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
#* "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
#Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).
#Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?
#For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

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
