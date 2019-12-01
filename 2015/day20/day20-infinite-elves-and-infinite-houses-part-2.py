#!/usr/bin/env python

#--- Day 20: Infinite Elves and Infinite Houses ---
#To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.
#Each Elf is assigned a number, too, and delivers presents to houses based on that number:
#The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
#The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
#Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
#There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.
#So, the first nine houses on the street end up like this:
#House 1 got 10 presents.
#House 2 got 30 presents.
#House 3 got 40 presents.
#House 4 got 70 presents.
#House 5 got 60 presents.
#House 6 got 120 presents.
#House 7 got 80 presents.
#House 8 got 150 presents.
#House 9 got 130 presents.
#The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.
#What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

#--- Part Two ---
#The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.
#With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?


puzzle_input = 36000000
# I'm afraid I cannot use the idea from Part One and will have to implement the delivery process...

# After a bit of research (and an awful solution that did not reach the end...) I found that I can go through an array with a fixed step width, so I can skip all the modulo calculation and just deliver presents at every elfnumberth house.
# And after even more research I finally got rid of my list out of range error when the elves start visiting houses with numbers beyond the puzzle input.


houses = [0]*puzzle_input
result = []

for elf in range(len(houses)):
	for house_nr in range(elf+1, min((elf+1)*50,len(houses)-1), elf+1):
		houses[house_nr] += 11*(elf+1)
		if houses[house_nr] >= puzzle_input:
			result.append([house_nr,houses[house_nr]])
			break

#min_result = len(houses)
#for i in range(len(result)):
#	if result[i][0] < min_result:
#		min_result = result[i][0]

result.sort(key=lambda x: x[0])

print(result[0][0], "for part 2")

