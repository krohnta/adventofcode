#!/usr/bin/env python


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
