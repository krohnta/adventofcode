#!/usr/bin/env python

#In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:
#children: 3
#cats: 7
#samoyeds: 2
#pomeranians: 3
#akitas: 0
#vizslas: 0
#goldfish: 5
#trees: 3
#cars: 2
#perfumes: 1

# import regex package
import re


# 1) read input into list for further transformation into dictionary
puzzle_input = []
full_list = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]
with open("day16.txt", "r") as file:
	for line in file:
		aunt_raw = []
		aunt = []
		aunt_raw = re.split('[\s:,]', line)
		puzzle_input.append(["".join(aunt_raw[0:2]), "".join(aunt_raw[3:6])])
		puzzle_input.append(["".join(aunt_raw[0:2]), "".join(aunt_raw[7:10])])
		puzzle_input.append(["".join(aunt_raw[0:2]), "".join(aunt_raw[11:])])

# append those entries for which no number of possessions is known
extended_list = puzzle_input[:]
for entry in range(0, len(puzzle_input), 3):
	tmp_list = [puzzle_input[entry][1][:-1],puzzle_input[entry+1][1][:-1],puzzle_input[entry+2][1][:-1]]
	diff_list = list(set(full_list).difference(tmp_list))
	for i in diff_list:
		extended_list.append([puzzle_input[entry][0],i+"x"])


# 2) make an inverted dictionary (learned in 2019/day 6)
#aunt_dict = {key: value for value, key in puzzle_input}
# won't work as there are more than one possible aunt for each possession+number!
aunt_dict = dict()
for entry in extended_list:
	if entry[1] in aunt_dict:
		aunt_dict[entry[1]].append(entry[0])
	else:
		aunt_dict[entry[1]] = [entry[0]]

#print(aunt_dict["childrenx"])
# 3) find the correct aunt (this will be ugly)
correct_aunt = []
intersection_aunt = []
tmp_aunt = []
if "children3" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["children3"])
if "childrenx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["childrenx"])
correct_aunt.append(tmp_aunt)

tmp_aunt = []
if "cats7" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["cats7"])
if "catsx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["catsx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[0]).intersection(correct_aunt[1]))

tmp_aunt = []
if "samoyeds2" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["samoyeds2"])
if "samoyedsx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["samoyedsx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[2]).intersection(intersection_aunt[0]))

tmp_aunt = []
if "pomeranians3" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["pomeranians3"])
if "pomeraniansx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["pomeraniansx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[3]).intersection(intersection_aunt[1]))

tmp_aunt = []
if "akitas0" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["akitas0"])
if "akitasx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["akitasx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[4]).intersection(intersection_aunt[2]))

tmp_aunt = []
if "vizslas0" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["vizslas0"])
if "vizslasx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["vizslasx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[5]).intersection(intersection_aunt[3]))

tmp_aunt = []
if "goldfish5" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["goldfish5"])
if "goldfishx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["goldfishx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[6]).intersection(intersection_aunt[4]))

tmp_aunt = []
if "trees3" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["trees3"])
if "treesx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["treesx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[7]).intersection(intersection_aunt[5]))

tmp_aunt = []
if "cars2" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["cars2"])
if "carsx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["carsx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[8]).intersection(intersection_aunt[6]))

tmp_aunt = []
if "perfumes1" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["perfumes1"])
if "perfumesx" in aunt_dict.keys():
	tmp_aunt.extend(aunt_dict["perfumesx"])
correct_aunt.append(tmp_aunt)
intersection_aunt.append(set(correct_aunt[9]).intersection(intersection_aunt[7]))

for i in intersection_aunt:
	print(len(i))
print(intersection_aunt[-1])
# Thanks to stackoverflow: the * at correct_aunt provides the elements of correct_aunt to the intersection, so saving a 'for i in correct_aunt' loop. Unfortunately, the result is incorrect and does not contain the correct aunt...
first_iteration = list(set(correct_aunt[0]).intersection(*correct_aunt[:]))


### DEBUG OUTPUT
#print(puzzle_input[0:7])
#print(tmp_aunt)
#print(correct_aunt[0])
#print(len(tmp_aunt))
#print(len(correct_aunt[0]))
#print(len(correct_aunt))
#print(len(correct_aunt[2]))
print(first_iteration)
#print(len(first_iteration))
