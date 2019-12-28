#!/usr/bin/env python

# With a lot of help from Wikipedia on how I can calculate the number at a certain entry without the need to create the whole grid...

def pairing(x,y):
	return y + (x+y-2)*(x+y-1)//2
code_starter = pairing(2947,3029)

# calculating the remainders
def calc_code(grid_entry):
	code = 20151125
	for i in range(1,grid_entry):
#		print(code)
		code = (code * 252533) % 33554393
	return code

print("The number at row 2947, column 3029 is", code_starter)
print("The code at this place is", calc_code(code_starter))
