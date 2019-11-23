#!/usr/bin/env python

#--- Day 5: Doesn't He Have Intern-Elves For This? ---
# As Part Two cannot be amended easily, this will be done in a separate program.
#--- Part Two ---
#Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
#
#Now, a nice string is one with all of the following properties:
#
#* It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#* It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
#For example:
#* qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#* xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#* uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#* ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
#How many strings are nice under these new rules?


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
