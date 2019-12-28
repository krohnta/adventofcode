#!/usr/bin/env python



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

