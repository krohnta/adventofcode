#!/usr/bin/env python


# 1) read input file from folder
input = open("day01.txt", "r").read()

# 2) count amount of ( and ) in string
# 2a) to get the first time the difference is less than zero, calculate the difference during the iteration
counter_opening_braces = 0
counter_closing_braces = 0
current_floor = 0
position = []
for i in input:
	if i == "(":
		counter_opening_braces += 1
		current_floor += 1
	elif i == ")":
		counter_closing_braces += 1
		current_floor -= 1
	if current_floor < 0:
		position.append(counter_opening_braces + counter_closing_braces)

# 3) calculate difference between amount of ( and ) to get the floor number
floor = counter_opening_braces - counter_closing_braces

# 4) have a nice output
print("Santa will go up ", counter_opening_braces, " floors and down ", counter_closing_braces, " floors in total,\nwhich results in him ending up on floor ", floor,".", sep="")


print("Santa enters the basement at position ", position[0],".", sep="")
