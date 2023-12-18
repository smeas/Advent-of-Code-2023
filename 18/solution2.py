#
# Day 18
# Solution 1: 49578
# Solution 2: 52885384955882
#
#

data = open("input.txt").read().splitlines()

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

dirmap = {'U': UP, 'R': RIGHT, 'D': DOWN, 'L': LEFT}
dirs = [RIGHT, DOWN, LEFT, UP]

def add_vec(a, b):
	return (a[0] + b[0], a[1] + b[1])

def mul_vec(a, b):
	return (a[0] * b[0], a[1] * b[1])

def calc_nodes(part):
	nodes = []
	last_node = (0, 0)
	circumference = 0
	for line in data:
		dir, count, color = line.split(" ")
		if part == 1:
			dir = dirmap[dir]
			count = int(count)
		else: # part 2
			color = color[2:] # strip away '(#'
			dir = dirs[int(color[5])]
			count = int(color[:5], base=16)

		last_node = add_vec(last_node, mul_vec(dir, (count, count)))
		nodes.append(last_node)
		circumference += count

	return nodes, circumference

# Calculate the area of a non-intersecting 2D polygon.
# https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])


def solve(part):
	nodes, circumference = calc_nodes(part)
	return area(nodes) + (1 + circumference / 2)

print(solve(1))
print(solve(2))
