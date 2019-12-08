#!/usr/bin/env python

#--- Day 8: Space Image Format ---
#The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.
#When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.
#Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.
#Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.
#Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.
#For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:
#Layer 1: 123
#         456
#Layer 2: 789
#         012
#The image you received is 25 pixels wide and 6 pixels tall.
#To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?

# 1) Read puzzle input, a string seems fine to be split up in Python
puzzle_input = open("day08.txt", "r").read()

# 2) Image is 25 wide, 6 tall, i.e. a layer contains this many characters
size_layer = 25*6

### DEBUG INPUT
#puzzle_input = "120116712112"
#size_layer = 3*2
# 3) Split image to layers
image = []
for i in range(len(puzzle_input)//size_layer):
	image.append(puzzle_input[i*size_layer:(i+1)*size_layer])

# 4) count 0,1,2 (could probably be done within the previous loop?!)
global_zero = size_layer
global_counter = []
for layer in image:
	local_zero = 0
	local_one = 0
	local_two = 0
	for char in layer:
		if char == "0":
			local_zero += 1
		elif char == "1":
			local_one += 1
		elif char == "2":
			local_two += 1
	if local_zero < global_zero:
		global_zero = local_zero
	global_counter.append([global_zero,local_zero,local_one,local_two])
global_counter.sort()

### DEBUG OUTPUT
print(image[0:2])
#print(global_counter)
print(global_counter[0][2]*global_counter[0][3])

