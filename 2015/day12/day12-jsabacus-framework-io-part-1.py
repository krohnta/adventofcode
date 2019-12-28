#!/usr/bin/env python


# import regex package
import re

# 1) read puzzle input and make it one long string
puzzle_input = open("day12.txt", "r").read()
puzzle_string = ''.join(puzzle_input)

# 2a) replace everything except 0-9 and dash (for minus) with a plus-sign
puzzle1 = ""
# unfortunately, \D for non-digits does not work due to the minus
puzzle1 = re.sub('[a-zA-Z,:\{\}\"\[\]]', ' ', puzzle_string)

# 2b) replace more than one plus-sign with one plus-sign only
puzzle2 = ""
puzzle2 = re.sub(' +', '+', puzzle1)

# 2c) replace occurrences of plus-minus with just the minus
puzzle3 = ""
puzzle3 = re.sub('\+-', '-', puzzle2)


# 3) I hope the result can be evaluated easily
result = eval(puzzle3[0:-2])

# 4) print a nice result
print("The sum of all numbers in the document is", result, "(and I know that this does not look nice...).")
