#!/usr/bin/env python


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
