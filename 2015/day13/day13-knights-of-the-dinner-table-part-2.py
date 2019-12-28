#!/usr/bin/env python


# regex package to parse input data
import re
# import permutation function
from itertools import permutations

# 1) read puzzle input and parse it to [name1, name2, (-)unit]
puzzle_input = []
# FIXME using brute-force by manipulating the input file yields the correct solution:
#with open("day13plusme.txt", "r") as file:
# solving the issue withing the program:
with open("day13.txt", "r") as file:
	for line in file:
		knight_raw = []
		knight = []
		knight_raw = re.split('[\s.]', line)
		if knight_raw[2] == "lose":
			knight.extend([knight_raw[0], knight_raw[10], -int(knight_raw[3])])
		else:
			knight.extend([knight_raw[0], knight_raw[10], int(knight_raw[3])])
		puzzle_input.append(knight)
		# a knight entry looks like ['Alice', 'Bob', -2] or ['Alice', 'David', 65]

# 2) prepare a list of all knights and their sitting permutations
knights = set()
possible_seatings = []
for i in puzzle_input:
	knights.add(i[0])
knights.add('me')

possible_seatings = list(permutations(knights))
possible_seatings = [list(element) for element in possible_seatings]
for seating in possible_seatings:
	# I have no clue how to do circular lists in Python, so this is my awful substitution...
	seating.append(seating[0])

# 3) calculate happiness for each seating
def calculate_happiness_between_two(knight1,knight2):
	if (knight1 == "me") or (knight2 == "me"):
		return 0
	for i in puzzle_input:
		if (knight1 == i[0]) and (knight2 == i[1]):
			return i[2]

def calculate_happiness(seating):
	happiness = 0
	for i in range(len(seating)-1):
		happiness += calculate_happiness_between_two(seating[i],seating[i+1])
		happiness += calculate_happiness_between_two(seating[i+1],seating[i])
	return happiness


# 4) calculate happiness for all seatings and get maximum
max_happiness = 0

for seating in possible_seatings:
	current_happiness = 0
	current_happiness += calculate_happiness(seating)
	seating.append(current_happiness)
	if current_happiness > max_happiness:
		max_happiness = current_happiness
		happiest_seating = seating

# 5) have a nice output
print(knights)
print("The total change in happiness is", max_happiness)
print("The corresponding seating is", ', '.join(happiest_seating[1:-2]))
