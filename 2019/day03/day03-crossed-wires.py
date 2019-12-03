#!/usr/bin/env python
# FIXME This is broken. I tend to start from scratch again after having learned how to use numpy. I think this would be easier to do with Matlab. After ~15 years not having used Matlab.


# import regex package
import re

# 1) read input into list of integers
puzzle_input = []
#with open("day03.txt", "r") as file:
### DEBUG INPUT
#with open("day03-test2.txt", "r") as file:
with open("day03-test1.txt", "r") as file:
	for line in file:
		puzzle_input.append(re.split(",", line.rstrip()))

# 2) get size of grid (similar to 2015/day03), but as no two movements go to the same direction, I need a max instead of a sum
min_ud_counter = 0
max_ud_counter = 0
min_lr_counter = 0
max_lr_counter = 0
movement = []


# FIXME my grid is too small :( I need a better method for calculating the dimension, max is wrong
for i in puzzle_input:
	movement_raw = []
	for j in i:
		move = int(j[1:])
		if j[0] == "U":
			movement_raw.append("U"*move)
			if move > max_ud_counter:
				max_ud_counter += move
		elif j[0] == "D":
			movement_raw.append("D"*move)
			if -move < min_ud_counter:
				min_ud_counter -= move
		elif j[0] == "L":
			movement_raw.append("L"*move)
			if -move < min_lr_counter:
				min_lr_counter -= move
		elif j[0] == "R":
			movement_raw.append("R"*move)
			if move > max_lr_counter:
				max_lr_counter += move
	movement.append([''.join(movement_raw)])

#oneline = left_counter + right_counter
oneline = -min_lr_counter + max_lr_counter

# create a grid with [False, False] as coordinate for both lines not having "visited" the coordinate yet
# visit_tracker = [False, False]*(up_counter+down_counter)*(left_counter+right_counter)
# again, in terms of cartesian coordinates, the mapping should be:
# oneline = dimenson in left-right direction
# visit_tracker[0] is corner left-down == (-left_counter, -down_counter)
# visit_tracker[left_counter] is "middle" ground == (0, -down_counter)
# visit_tracker[oneline] is corner right-down == (right_counter,-down_counter)
# visit_tracker[2*oneline] is (right_counter,-down_counter+1)
# visit_tracker[down_counter*oneline+left_counter] middle of system == (0,0)

#visit_tracker = [[0, 0]]*(up_counter+down_counter)*(left_counter+right_counter)
visit_tracker = [[0, 0]]*(max_ud_counter-min_ud_counter)*(max_lr_counter-min_lr_counter)

# FIXME I don't understand why this function seems to change EVERY entry in visit_tracker while it should only change the one in current_location :(
def run_along(input_string,nr):
	current_location = (-min_ud_counter) * oneline + max_lr_counter
	# this equals (0,0) in my grid!
	print(visit_tracker[current_location])
	visit_tracker[current_location][nr] = 5
	print(visit_tracker[current_location])
	for i in input_string:
		if i == "U":
			visit_tracker[current_location][nr] = 1
			current_location += oneline
			print(visit_tracker[0:5])
		elif i == "D":
			visit_tracker[current_location][nr] = 2
			current_location -= oneline
			print(visit_tracker[0:5])
		elif i == "R":
#			print(visit_tracker[down_counter * oneline + left_counter+1])
			visit_tracker[current_location][nr] = 3
			current_location += 1
			print(visit_tracker[0:5])
		elif i == "L":
			visit_tracker[current_location][nr] = 4
			current_location -= 1
			print(visit_tracker[0:5])

run_along(movement[0][0],0)
#run_along(movement[1][0],1)

current_location = (-min_ud_counter) * oneline + max_lr_counter
# this equals (0,0) in my grid!
print(visit_tracker[current_location])
print(visit_tracker[current_location+1])
visit_tracker[current_location][0] = 5
print(visit_tracker[current_location])
print(visit_tracker[current_location+1])

### DEBUG OUTPUT
#print(puzzle_input)
#print(puzzle_input[0][1][0])
#print(puzzle_input[0][1][1:])
print(max_ud_counter, min_ud_counter, min_lr_counter, max_lr_counter)
print(oneline)
print(len(visit_tracker))
print(visit_tracker[0:5])
#print(len(movement))
#print(movement[0])
#print(len(movement[1]))

#print(visit_tracker[down_counter * oneline + left_counter+1])
