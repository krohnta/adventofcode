#!/usr/bin/env python

#--- Day 13: Knights of the Dinner Table ---
#In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.
#You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.
#For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:
#Alice would gain 54 happiness units by sitting next to Bob.
#Alice would lose 79 happiness units by sitting next to Carol.
#Alice would lose 2 happiness units by sitting next to David.
#Bob would gain 83 happiness units by sitting next to Alice.
#Bob would lose 7 happiness units by sitting next to Carol.
#Bob would lose 63 happiness units by sitting next to David.
#Carol would lose 62 happiness units by sitting next to Alice.
#Carol would gain 60 happiness units by sitting next to Bob.
#Carol would gain 55 happiness units by sitting next to David.
#David would gain 46 happiness units by sitting next to Alice.
#David would lose 7 happiness units by sitting next to Bob.
#David would gain 41 happiness units by sitting next to Carol.
#Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.
#If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:
#     +41 +46
#+55   David    -2
#Carol       Alice
#+60    Bob    +54
#     -7  +83
#After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.
#What is the total change in happiness for the optimal seating arrangement of the actual guest list?

# regex package to parse input data
import re
# import permutation function
from itertools import permutations

# 1) read puzzle input and parse it to [name1, name2, (-)unit]
puzzle_input = []
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
possible_seatings = list(permutations(knights))
possible_seatings = [list(element) for element in possible_seatings]
for seating in possible_seatings:
	# I have no clue how to do circular lists in Python, so this is my awful substitution...
	seating.append(seating[0])

# 3) calculate happiness for each seating
def calculate_happiness_between_two(knight1,knight2):
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
print("The total change in happiness is", max_happiness)
print("The corresponding seating is", ', '.join(happiest_seating[1:-2]))
