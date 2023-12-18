#
# Day 18
# Solution 1: 49578
# Solution 2:
#
#

data = open("input.txt").read().splitlines()

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
dirmap = {
	'U': UP,
	'R': RIGHT,
	'D': DOWN,
	'L': LEFT,
}

def add_vec(a, b):
	return (a[0] + b[0], a[1] + b[1])

def calc_nodes():
	nodes = []
	last_node = (0, 0)
	for line in data:
		dir, count, color = line.split(" ")
		dir = dirmap[dir]
		count = int(count)
		for i in range(count):
			last_node = add_vec(last_node, dir)
			nodes.append(last_node)

	return nodes

def calc_bounds(nodes):
	xmin = ymin = 100000000
	xmax = ymax = -100000000
	for node in nodes:
		x, y = node
		if x < xmin: xmin = x
		if x > xmax: xmax = x
		if y < ymin: ymin = y
		if y > ymax: ymax = y

	return (xmin, ymin, xmax, ymax)

def shift_nodes_positive(nodes):
	xmin, ymin, xmax, ymax = calc_bounds(nodes)
	offset = (abs(xmin), abs(ymin))
	print(xmin, ymin, xmax, ymax, "offset:", offset)
	for i, node in enumerate(nodes):
		nodes[i] = add_vec(node, offset)

	# return new bounds
	return xmax + abs(xmin) + 1, ymax + abs(ymin) + 1

def create_2d_array(w, h, fill):
	return [[fill for _ in range(w)] for _ in range(h)]

def sides(pos, width, height):
	x, y = pos
	if x > 0: yield (x - 1, y)
	if x < width - 1: yield (x + 1, y)
	if y > 0: yield (x, y - 1)
	if y < height - 1: yield (x, y + 1)

def flood_fill(grid, start, fill):
	width, height = len(grid[0]), len(grid)
	queue = [start]

	count = 0
	while len(queue) > 0:
		x, y = queue.pop()
		if grid[y][x] == fill:
			continue

		grid[y][x] = fill
		count += 1

		for side in sides((x, y), width, height):
			queue.append(side)

	print(count)

SEED = (40, 10)

def solve_1():
	nodes = calc_nodes()
	width, height = shift_nodes_positive(nodes)
	grid = create_2d_array(width, height, ".")
	for node in nodes:
		x, y = node
		grid[y][x] = "#"

	flood_fill(grid, SEED, "#")

	total = 0
	for line in grid:
		total += line.count("#")

	return total
	# f=open("test.txt", 'wt')
	# for line in grid:
	# 	f.write("".join(line))
	# 	f.write("\n")

solution_1 = solve_1()
print(solution_1)
