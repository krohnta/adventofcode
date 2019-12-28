#!/usr/bin/env python


# 1) read input file from folder, but transfer into array while reading
input = []
with open("day02.txt", "r") as file:
	for line in file:
		input.append(line.rstrip())

# 2) make each present an array within the array and sort ascending (preparation for getting smallest side!)
for i in range(len(input)):
	input[i] = input[i].split("x")
	for j in range(len(input[i])):
		input[i] = [int(x) for x in input[i]]
#	input[i].sort(key=int) # this would keep the list as list of str
	input[i].sort()

# 3) calculate wrapping paper for each present and add it to total amount of needed paper
# 3a) calculate ribbon for each present and add it to total amount of needed ribbon
paper = 0
ribbon = 0
for i in range(len(input)):
	paper += 3 * input[i][0] * input[i][1] + 2 * (input[i][0] * input[i][2] + input[i][1] * input[i][2])
	ribbon += 2 * (input[i][0] + input[i][1]) + input[i][0] * input[i][1] * input[i][2]

# 4) have a nice output
print("The elves have to order ", paper, " square feet of wrapping paper\nand ", ribbon, " feet of ribbon.", sep = "")
