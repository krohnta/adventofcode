#!/usr/bin/env python


import hashlib

# 1) split to be hashed input in fixed part (given by exercise) and variable part (over which will be iterated)
fixed_input = "bgvyzdsv"
variable_input = 1

# 2) calculate first hash to have a start value for the loop
answer = fixed_input + str(variable_input)
first_five_of_hashed_answer = hashlib.md5(answer.encode()).hexdigest()[:5]

# 3) loop over the hash and increment the variable part until the first five digits equal 0 (comparison as string to avoid another conversion)
while first_five_of_hashed_answer != "00000":
	variable_input += 1
	answer = fixed_input + str(variable_input)
	first_five_of_hashed_answer = hashlib.md5(answer.encode()).hexdigest()[:5]

# 4) have a nice output

print("The lowest positive number appended to", fixed_input, "resulting \nin an MD5 hash starting with five zeros is", variable_input)

# 5) do the same for 6 zeroes

while first_five_of_hashed_answer != "000000":
	variable_input += 1
	answer = fixed_input + str(variable_input)
	first_five_of_hashed_answer = hashlib.md5(answer.encode()).hexdigest()[:6]

# 4) have a nice output

print("The lowest positive number appended to", fixed_input, "resulting \nin an MD5 hash starting with six zeros is", variable_input)
