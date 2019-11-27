#!/usr/bin/env python

#--- Day 10: Elves Look, Elves Say ---
#Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).
#
#Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).
#
#For example:
#
#1 becomes 11 (1 copy of digit 1).
#11 becomes 21 (2 copies of digit 1).
#21 becomes 1211 (one 2 followed by one 1).
#1211 becomes 111221 (one 1, one 2, and two 1s).
#111221 becomes 312211 (three 1s, two 2s, and one 1).
#Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

# 1) no read for the few digits today ;)
puzzle_input = 1321131112

# 2) get next sequence
puzzle_input = [int(i) for i in str(1321131112)]
puzzle_input.append(0)

def calculate_next_seq(start_seq):
	next_seq = []
	cnt = 1
	for j in range(len(start_seq)-1):
		if start_seq[j] == start_seq[j+1]:
			cnt += 1
		else:
			next_seq.append(cnt)
			next_seq.append(start_seq[j])
			cnt = 1
	next_seq.append(0)
	return next_seq

result = calculate_next_seq(puzzle_input)

for i in range(39):
	result = calculate_next_seq(result)

solution_part1 = len(result)-1

for i in range(10):
	result = calculate_next_seq(result)

solution_part2 = len(result)-1

# 4) have a nice output

print("Length of result after 40 iterations:", solution_part1)
print("Length of result after 50 iterations:", solution_part2)
