#!/usr/bin/env python


# 1) Read puzzle input, a string seems fine to be split up in Python
puzzle_input = open("day08.txt", "r").read()

# 2) Image is 25 wide, 6 tall, i.e. a layer contains this many characters
width = 25
height = 6

### DEBUG INPUT
#puzzle_input = "0222112222120000"
#width = 2
#height = 2

size_layer = width * height

# 3) Split image to layers
image = []
for i in range(len(puzzle_input)//size_layer):
	image.append(puzzle_input[i*size_layer:(i+1)*size_layer])

# 4) Determine pixel color by creating a layer equal to the final image and set the corresponding positions according to the rendering
final_image = list(image[0])
# append pseudo boolean t/f to determine whether a pixel has been touched (and therefore must not be changed again), black/white pixels in uppermost layer must not be changed (took me ~2 hours of debugging)
for i in range(len(final_image)):
	if final_image[i] == "2":
		final_image[i] += "f"
	else:
		final_image[i] += "t"


for layer in range(len(image)):
	for i in range(len(image[layer])):
		if final_image[i][1] == "f":
			if image[layer][i] == "2" and image[layer+1][i] == "2":
				final_image[i] = "2f"
			else:
				final_image[i] = image[layer+1][i] + "t"


# 5) Output needs a nice format to read the message
image_output = final_image[:]
for i in range(len(final_image)):
	if final_image[i][0] == "0":
		image_output[i] = " "
	else:
#		image_output[i] = "*"
		image_output[i] = "█"


nice_pic = ''.join(image_output)
for c in range(height):
	print(nice_pic[c*width:(c+1)*width])

