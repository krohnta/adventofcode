#!/usr/bin/env python

#--- Day 1: Not Quite Lisp ---
#Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.
#Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#Here's an easy puzzle to warm you up.
#Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
#An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
#The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
#For example:
#* (()) and ()() both result in floor 0.
#* ((( and (()(()( both result in floor 3.
#* ))((((( also results in floor 3.
#* ()) and ))( both result in floor -1 (the first basement level).
#* ))) and )())()) both result in floor -3.
#To what floor do the instructions take Santa?
#
#--- Part Two ---
#Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
#
#For example:
#
#* ) causes him to enter the basement at character position 1.
#* ()()) causes him to enter the basement at character position 5.
#What is the position of the character that causes Santa to first enter the basement?


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
