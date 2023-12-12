#
# Day 10
# Solution 1: 6800
# Solution 2:
#
#

data = open("input.txt").read().splitlines()

UP = 'N'
RIGHT = 'E'
DOWN = 'S'
LEFT = 'W'

WIDTH = len(data[0])
HEIGHT = len(data)

def search(x, y, origin=None):
	sym = data[y][x]
	#print(sym, x, y, origin)
	if origin != (x,y-1) and y > 0 and can_path(sym, UP) and can_path(data[y - 1][x], DOWN):
		return (x, y - 1)
	if origin != (x+1, y) and x < WIDTH - 1 and can_path(sym, RIGHT) and can_path(data[y][x + 1], LEFT):
		return (x + 1, y)
	if origin != (x,y+1) and y < HEIGHT - 1 and can_path(sym, DOWN) and can_path(data[y + 1][x], UP):
		return (x, y + 1)
	if origin != (x-1,y) and x > 0 and can_path(sym, LEFT) and can_path(data[y][x - 1], RIGHT):
		return (x - 1, y)
	raise Exception(f"not found ({x}, {y})")

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
def can_path(sym, dir):
	if dir == UP and sym in ['L', 'J', '|']:
		return True
	if dir == RIGHT and sym in ['-', 'L', 'F']:
		return True
	if dir == DOWN and sym in ['7', 'F', '|']:
		return True
	if dir == LEFT and sym in ['-', 'J', '7']:
		return True
	if sym == 'S':
		return True
	return False

def solve_1():
	S = ()
	for y, line in enumerate(data):
		index = line.find('S')
		if index != -1:
			S = (index, y)

	#print(S)

	points = []
	prev_pos = S
	origin = S
	next_pos = search(*S)
	while next_pos != S:
		#print(next_pos)
		points.append(next_pos)

		prev_pos = next_pos
		next_pos = search(*next_pos, origin)
		origin = prev_pos
	#print(points)
	print("num points", len(points))
	print((len(points) + 1) // 2)

solution_1 = solve_1()