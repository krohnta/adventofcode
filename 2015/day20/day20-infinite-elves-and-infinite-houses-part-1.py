#!/usr/bin/env python


# divide by 10, so no need for elves to deliver 10 presents
puzzle_input = 3600000

# First idea: implement the puzzle delivery
# Second idea: calculate divisors for each house's number and add them

def sum_of_divisors(number):
	list_of_divisors = []
	for i in range(1,int(number/2)+1):
		if number%i == 0:
			list_of_divisors.append(i)
	list_of_divisors.append(number)
	sum = 0
	for i in list_of_divisors:
		sum += i
	return sum

presents = 0
i = 1

while presents < puzzle_input:
	presents = sum_of_divisors(i)
	i += 1


print(presents)
print(i-1)

