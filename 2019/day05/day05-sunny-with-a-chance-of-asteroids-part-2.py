#!/usr/bin/env python

# modify the Intcode computer from day 2 with
# - opcode 3 => save input to position
# - opcode 4 => output value at position
# - opcode 5 => if pos1==0: next position==pos2
# - opcode 6 => if pos1==0: next position==pos2
# - opcode 7 => if pos1<pos2: pos3 or program[pos3] == 1;
#               else: pos3 or program[pos3] == 0
# - opcode 8 => if pos1==pos2: pos3 or program[pos3] == 1;
#               else: pos3 or program[pos3] == 0

# support for parameter mode


# import regex package
import re
# import sys package for clean exit
import sys


# read input into list of integers
with open("day05.txt", "r") as file:
    for entry in file.readlines():
        puzzle_input = re.split(',', entry)

puzzle_input = [int(i) for i in puzzle_input]

# determine opcode and parameter modes
def calc_mode(parameter):
    opcode = int(str(parameter)[-2:])

    try:
        mode1 = int(str(parameter)[-3])
    except IndexError:
        mode1 = 0
    
    try:
        mode2 = int(str(parameter)[-4])
    except IndexError:
        mode2 = 0

    try:
        mode3 = int(str(parameter)[-5])
    except IndexError:
        mode3 = 0

    return [opcode, mode1, mode2, mode3]

# define actions
def calc_output(program,instruction):
    position = 0
    # just in case: set value for output if output is not reached
    out = "INVALID"
    while True:
        print("current pos: ", position, ", current value:", program[position])
#        print("program at loop start: ", program)

        mode_value = calc_mode(program[position])
        opcode = mode_value[0]
#        print(mode_value)

        if opcode == 99:
            print("HALT, opcode 99 found, last output was: ", out)
            quit()


        pos1 = program[position+1]
        mod_pos1 = mode_value[1]

        pos2 = program[position+2]
        mod_pos2 = mode_value[2]


        if opcode == 8:
            try:
                pos3 = program[position+3]
                mod_pos3 = mode_value[3]

                if mod_pos1 == 0:
                    val1 = program[pos1]
                else:
                    val1 = pos1

                if mod_pos2 == 0:
                    val2 = program[pos2]
                else:
                    val2 = pos2

                if val1 == val2:
                    if mod_pos3 == 0:
                        program[pos3] = 1
                        print("writing 1 to position", pos3)
                    else:
                        program[position+3] = 1
                        print("writing 1 to position", position+3)
                else:
                    if mod_pos3 == 0:
                        program[pos3] = 0
                        print("writing 0 to position", pos3)
                    else:
                        program[position+3] = 0
                        print("writing 0 to position", position+3)
            except IndexError:
                sys.exit("out = something went wrong in opcode 8!")
            position += 4

        if opcode == 7:
            try:
                pos3 = program[position+3]
                mod_pos3 = mode_value[3]
                if mod_pos1 == 0:
                    val1 = program[pos1]
                else:
                    val1 = pos1

                if mod_pos2 == 0:
                    val2 = program[pos2]
                else:
                    val2 = pos2

                if val1 < val2:
                    if mod_pos3 == 0:
                        program[pos3] = 1
                        print("writing 1 to position", pos3)
                    else:
                        program[position+3] = 1
                        print("writing 1 to position", position+3)
                else:
                    if mod_pos3 == 0:
                        program[pos3] = 0
                        print("writing 0 to position", pos3)
                    else:
                        program[position+3] = 0
                        print("writing 0 to position", position+3)
            except IndexError:
                sys.exit("out = something went wrong in opcode 7!")
            position += 4


        if opcode == 6:
            try:
                if mod_pos1 == 0:
                    pos1 = program[pos1]

                if pos1 == 0:
                    if mod_pos2 == 0:
                        position = program[pos2]
                    else:
                        position = pos2
                else:
                    position += 3
                print("jumping to position", position)
            except IndexError:
                sys.exit("out = something went wrong in opcode 6!")

        if opcode == 5:
            try:
                if mod_pos1 == 0:
                    pos1 = program[pos1]

                if pos1 != 0:
                    if mod_pos2 == 0:
                        position = program[pos2]
                    else:
                        position = pos2
                else:
                    position += 3
                print("jumping to position", position)
            except IndexError:
                sys.exit("out = something went wrong in opcode 5!")


        if opcode == 4:
            if mod_pos1 == 0:
                print("out =", program[pos1])
                out = program[pos1]
            else:
                print("out =", pos1)
                out = pos1
            position += 2

        if opcode == 3:
            try:
                program[pos1] = instruction
                print("writing instruction", instruction, "to position",
                        pos1)
            except IndexError:
                sys.exit("out = something went wrong in opcode 3!")
            position += 2

        if opcode == 1 or opcode == 2:
            if mod_pos1 == 0:
                try:
                    val1 = program[pos1]
                except IndexError:
                    sys.exit("out = something went wrong in mode of pos1!")
            else:
                val1 = pos1

            if mod_pos2 == 0:
                try:
                    val2 = program[pos2]
                except IndexError:
                    sys.exit("out = something went wrong in mode of pos2!")
            else:
                val2 = pos2

            if opcode == 1:
                val3 = val1 + val2
                try:
                    pos3 = program[position+3]
                    program[pos3] = val3
                    print("writing ", val3, " to position" , pos3)
                except IndexError:
                    sys.exit("out = something went wrong in opcode 1!")
                position += 4

            if opcode == 2:
                val3 = val1 * val2
                try:
                    pos3 = program[position+3]
                    program[pos3] = val3
                    print("writing ", val3, " to position" , pos3)
                except IndexError:
                    sys.exit("out = something went wrong in opcode 2!")
                position += 4



print(calc_output(puzzle_input,5))

### DEBUG OUTPUT ###
#print(calc_mode(1032))

# position mode:
#print(calc_output([3,9,8,9,10,9,4,9,99,-1,8],8))
#print("if input == 8: out = 1; else: out = 0")

# position mode:
#print(calc_output([3,9,7,9,10,9,4,9,99,-1,8],12))
#print("if input < 8: out = 1; else: out = 0")

# immediate mode:
#print(calc_output([3,3,1108,-1,8,3,4,3,99],-88))
#print("if input == 8: out = 1; else: out = 0")

# immediate mode:
#print(calc_output([3,3,1107,-1,8,3,4,3,99],-66))
#print("if input < 8: out = 1; else: out = 0")

# position mode:
#print(calc_output([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],0))
#print("if input == 0: out = 0; else: out = 1")

# immediate mode:
#input_value = 0
#print("input =", input_value, "; if input == 0: out = 0; else: out = 1")
#print(calc_output([3,3,1105,-1,9,1101,0,0,12,4,12,99,1],input_value))

# larger example using both modes:
"""
print(calc_output([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],4))
"""
