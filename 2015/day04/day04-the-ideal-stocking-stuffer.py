#!/usr/bin/env python

#--- Day 4: The Ideal Stocking Stuffer ---
#Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
#To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
#For example:
#* If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
#* If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
#Your puzzle input is bgvyzdsv.

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
