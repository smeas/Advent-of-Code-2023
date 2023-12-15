#
# Day 14
# Solution 1: 107430
# Solution 2:
#
#

data = open("input.txt").read().splitlines()

def find_free_spot_up(grid, x, y):
	ytest = y
	while ytest > 0:
		ytest -= 1
		if grid[ytest][x] != ".":
			return ytest + 1

	if ytest == 0:
		return 0
	else:
		return y

def tilt_north(grid):
	width = len(grid[0])
	height = len(grid)

	# clone grid
	dest = []
	for row in grid:
		dest.append(list(row))

	# move rocks
	for row in range(height):
		for col in range(width):
			if grid[row][col] == "O":
				dest_y = find_free_spot_up(dest, col, row)
				dest[row][col] = "."
				dest[dest_y][col] = "O"

	# for row in dest:
	# 	print(row)

	# count score
	total = 0
	for row in range(height):
		for col in range(width):
			if dest[row][col] == "O":
				total += height - row

	return total


def solve_1():
	total = tilt_north([*map(list, data)])
	return total

print(solve_1())
