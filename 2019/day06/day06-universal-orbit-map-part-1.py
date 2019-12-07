#!/usr/bin/env python

#--- Day 6: Universal Orbit Map ---
#You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).
#Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object. An orbit looks roughly like this:
#                  \
#                   \
#                    |
#                    |
#AAA--> o            o <--BBB
#                    |
#                    |
#                   /
#                  /
#In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA (drawn with lines) is only partly shown. In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".
#Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses orbit count checksums - the total number of direct orbits (like the one shown above) and indirect orbits.
#Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.
#For example, suppose you have the following map:
#COM)B
#B)C
#C)D
#D)E
#E)F
#B)G
#G)H
#D)I
#E)J
#J)K
#K)L
#Visually, the above map of orbits looks like this:
#        G - H       J - K - L
#       /           /
#COM - B - C - D - E - F
#               \
#                I
#In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.
#Here, we can count the total number of orbits as follows:
#* D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
#* L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
#* COM orbits nothing.
#The total number of direct and indirect orbits in this example is 42.
#What is the total number of direct and indirect orbits in your map data?

puzzle_input = []
# 1) read input
with open("day06.txt", "r") as file:
### DEBUG INPUT
#with open("day06-test.txt", "r") as file:
	for entry in file.readlines():
		puzzle_input.append(entry.rstrip().split(")"))

# 1.1) check whether it would be a binary tree or not
#checklist = [x[0] for x in split_input]
#for x in checklist:
#	if checklist.count(x) > 2:
#		print("not binary,", x, "contained more than twice!")
## damn it: not binary, 7LD contained more than twice!
## okay. Let's build a ternary tree...

# 2) build a tree from the input data
# After having read through some reddit posts looking for help on this one (Python has no native tree structure, I was not able to get anytree do what I wanted it to do, I was not able to get my input into any reasonable structure, ...), I'm afraid I have to take a look at dictionaries again. At least, I already was at the right way of counting things, but without knowledge about how dictionaries work, I couldn't possibly figure out how to set it up properly (and my trials with doing it with lists of lists of lists of lists etc. etc. failed).

# every object is key with value being the object that they orbit
orbit_dict = {key: value for value, key in puzzle_input}

# now, for every object=key, count how many "parents" there are, i.e. look-up the key's value in the keys until COM is reached - and COM is no key, so this will stop the while loop
calc_orbits = 0
for obj in orbit_dict.keys():
	obj_tmp = obj
	while obj_tmp in orbit_dict:
		calc_orbits += 1
		obj_tmp = orbit_dict[obj_tmp]
print(calc_orbits)

### DEBUG OUTPUT
print(puzzle_input[0:5])
#print(orbit_dict)

