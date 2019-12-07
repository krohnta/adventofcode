#!/usr/bin/env python

#--- Day 6: Universal Orbit Map ---

puzzle_input = []
# 1) read input
with open("day06.txt", "r") as file:
### DEBUG INPUT
#with open("day06-test.txt", "r") as file:
	for entry in file.readlines():
		puzzle_input.append(entry.rstrip().split(")"))

# 2) build a tree from the input data
# After having read through some reddit posts looking for help on this one (Python has no native tree structure, I was not able to get anytree do what I wanted it to do, I was not able to get my input into any reasonable structure, ...), I'm afraid I have to take a look at dictionaries again. At least, I already was at the right way of counting things, but without knowledge about how dictionaries work, I couldn't possibly figure out how to set it up properly (and my trials with doing it with lists of lists of lists of lists etc. etc. failed).

# every object is key with value being the object that they orbit
orbit_dict = {key: value for value, key in puzzle_input}

# now, for every object=key, count how many "parents" there are, i.e. look-up the key's value in the keys until COM is reached - and COM is no key, so this will stop the while loop

# For part 2, I need to find the common ancestor with max distance from COM. Building the complete ancestry line, and then delete everything that's in both lists should work (because objects in both ancestry lines don't have to be traversed for the transfer, they're further up).

calc_orbits = 0
san_ancestry = ["SAN"]
you_ancestry = ["YOU"]
for obj in orbit_dict.keys():
	obj_tmp = obj
	while obj_tmp in orbit_dict:
		if obj_tmp == san_ancestry[-1]:
			san_ancestry.append(orbit_dict[obj_tmp])
		elif obj_tmp == you_ancestry[-1]:
			you_ancestry.append(orbit_dict[obj_tmp])
		calc_orbits += 1
		obj_tmp = orbit_dict[obj_tmp]
#print(calc_orbits)

# Now, the ancestry lines are complete. Instead of intersection, the wanted "unionizing method" is symmetric_difference:
uncommon_ancestry = list(set(san_ancestry).symmetric_difference(you_ancestry))
# subtract 2 because YOU and SAN should not be counted according to the puzzle:
print("Needed transfers from YOU to SAN:", len(uncommon_ancestry)-2)

### DEBUG OUTPUT
#print(puzzle_input[0:5])
#print(orbit_dict)
#print(san_ancestry)
#print(you_ancestry)
#print(uncommon_ancestry)
