#!/usr/bin/env python


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
