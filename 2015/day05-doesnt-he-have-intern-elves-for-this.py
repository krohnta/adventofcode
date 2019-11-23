#!/usr/bin/env python

#--- Day 5: Doesn't He Have Intern-Elves For This? ---
#Santa needs help figuring out which strings in his text file are naughty or nice.
#A nice string is one with all of the following properties:
#* It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#* It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#* It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
#For example:
#* ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#* aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#* jchzalrnumimnmhp is naughty because it has no double letter.
#* haegwjzuvuyypxyu is naughty because it contains the string xy.
#* dvszwmarrgswjxmb is naughty because it contains only one vowel.
#How many strings are nice?

# 1) read input file, but transfer into array for easier iteration later
puzzle_input = []
with open("day05.txt", "r") as file:
	for line in file:
		puzzle_input.append(line.rstrip())

# 2) exclude all entries with disallowed substrings (seems more logical to start with exclusion), yes, I can see that this looks awful, however, it seems to work...
disallow1 = "ab"
disallow2 = "cd"
disallow3 = "pq"
disallow4 = "xy"
puzzle1 = []
print(len(puzzle_input))
for i in range(len(puzzle_input)):
	if (disallow1 not in puzzle_input[i]) and (disallow2 not in puzzle_input[i]) and (disallow3 not in puzzle_input[i]) and (disallow4 not in puzzle_input[i]):
		puzzle1.append(puzzle_input[i])

# 3) check for three vowels
def count_in_string(string,char):
	# returns amount of $char in $string
	count_char = 0
	for c in string:
		if c == char:
			count_char += 1
	return count_char

puzzle2 = []
for i in range(len(puzzle1)):
	count_vowel = count_in_string(puzzle1[i],"a") + count_in_string(puzzle1[i],"e") +count_in_string(puzzle1[i],"i") +count_in_string(puzzle1[i],"o") + count_in_string(puzzle1[i],"u")
	if count_vowel > 2:
		puzzle2.append(puzzle1[i])

# 4) check for one letter twice in a row
puzzle3 = []
for i in range(len(puzzle2)):
	for j in range(len(puzzle2[i])-1):
		if puzzle2[i][j] == puzzle2[i][j+1]:
			puzzle3.append(puzzle2[i])
			break

# 5) have a nice output
#print("Strings without disallowed strings:", len(puzzle1))
#print("of these: Strings with at least 3 vowels:", len(puzzle2))
#print("of these: Strings with letters twice in a row:", len(puzzle3))
print("There are", len(puzzle3), "nice strings in the text file.")
