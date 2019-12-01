#!/usr/bin/env python

#--- Day 3: Perfectly Spherical Houses in a Vacuum ---
#Santa is delivering presents to an infinite two-dimensional grid of houses.
#He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
#However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
#For example:
#* > delivers presents to 2 houses: one at the starting location, and one to the east.
#* ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
#
#--- Part Two ---
#The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
#
#Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
#
#This year, how many houses receive at least one present?
#
#For example:
#
#^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

# 1) read input into string for iteration
input = open("day03.txt", "r").read()

# 2) calculate the amount of each character to get the upper limit for the grid border (yes, it is far too big, however, at least it is not infinite)
north_counter = 0
south_counter = 0
east_counter = 0
west_counter = 0

for i in input:
	if i == "^":
		north_counter += 1
	elif i == "v":
		south_counter += 1
	elif i == ">":
		east_counter += 1
	elif i == "<":
		west_counter += 1
# nsew = 1981 -2068 2092 -2051

# 2) create a "grid" with 0 visits for each "coordinate" (which equals a house each)
#visit_counter = [0]*(north_counter+south_counter)*(east_counter+west_counter)
one_line = east_counter+west_counter
# in terms of (x,y) in cartesian coordinates, the mapping should be:
# one line == east_counter+west_counter
# visit_counter[0] is corner left-down == (-west_counter,-south_counter)
# visit_counter[west_counter] == (0,-south_counter)
# visit_counter[one_line] is corner right-down == (east_counter,-south_counter)
# visit_counter[2*one_line] == (east_counter,-south_counter+1)
# visit_counter[south_counter*one_line+east_counter] == (0,0)
visit_counter = []
for i in range(-south_counter,north_counter):
	for j in range(-west_counter,east_counter):
		visit_counter.append(0)

# 3) split input between Santa and Robo-Santa
visited_by_santa = ""
visited_by_robo = ""
for i in range(len(input)):
	if i%2 == 0:
		visited_by_santa += input[i]
	else:
		visited_by_robo += input[i]


# 3a) visit houses with Santa and Robo-Santa, both starting at (0,0)
current_location_santa = south_counter*one_line+east_counter
current_location_robo = south_counter*one_line+east_counter
for i in visited_by_santa:
	# Santa delivers a present
	if i == "^":
		visit_counter[current_location_santa] += 1
		current_location_santa += one_line
	elif i == "v":
		visit_counter[current_location_santa] += 1
		current_location_santa -= one_line
	elif i == ">":
		# if I'm not mistaken, I do not have to take care of running over the borders of the cartesian coordinates!
		visit_counter[current_location_santa] += 1
		current_location_santa += 1
	elif i == "<":
		visit_counter[current_location_santa] += 1
		current_location_santa -= 1

for i in visited_by_robo:
	# Robo-Santa delivers a present
	if i == "^":
		visit_counter[current_location_robo] += 1
		current_location_robo += one_line
	elif i == "v":
		visit_counter[current_location_robo] += 1
		current_location_robo -= one_line
	elif i == ">":
		# if I'm not mistaken, I do not have to take care of running over the borders of the cartesian coordinates!
		visit_counter[current_location_robo] += 1
		current_location_robo += 1
	elif i == "<":
		visit_counter[current_location_robo] += 1
		current_location_robo -= 1

# 4) find houses with at least one visit
present_counter = 0
for i in range(len(visit_counter)):
	if visit_counter[i] > 0:
		present_counter += 1

# 5) have a nice output
print("Santa and Robo-Santa visit", present_counter, "houses.")
### DEBUG INFORMATION
#print(north_counter, south_counter, east_counter, west_counter)
#print(visit_counter[south_counter*one_line+east_counter])
#print(visit_counter[current_location])
#print(present_counter)
