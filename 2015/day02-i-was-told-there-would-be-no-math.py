#!/usr/bin/env python

#--- Day 2: I Was Told There Would Be No Math ---
#The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
#
#Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
#
#For example:
#
#* A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
#* A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
#All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

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
paper = 0
for i in range(len(input)):
	paper += 3 * input[i][0] * input[i][1] + 2 * (input[i][0] * input[i][2] + input[i][1] * input[i][2])

# 4) have a nice output
print("The elves have to order ", paper, " square feet of wrapping paper.", sep = "")
