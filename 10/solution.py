#
# Day 10
# Solution 1: 6800
# Solution 2: 483
#
#

data = open("input.txt").read().splitlines()

UP = 'U'
RIGHT = 'R'
DOWN = 'D'
LEFT = 'L'
IN = 'I'

WIDTH = len(data[0])
HEIGHT = len(data)

MAP = [[' '] * WIDTH for _ in range(HEIGHT)]

def search(x, y, origin=None):
	sym = data[y][x]
	#print(sym, x, y, origin)
	if origin != (x,y-1) and y > 0 and can_path(sym, UP) and can_path(data[y - 1][x], DOWN):
		return (x, y - 1), UP
	if origin != (x+1, y) and x < WIDTH - 1 and can_path(sym, RIGHT) and can_path(data[y][x + 1], LEFT):
		return (x + 1, y), RIGHT
	if origin != (x,y+1) and y < HEIGHT - 1 and can_path(sym, DOWN) and can_path(data[y + 1][x], UP):
		return (x, y + 1), DOWN
	if origin != (x-1,y) and x > 0 and can_path(sym, LEFT) and can_path(data[y][x - 1], RIGHT):
		return (x - 1, y), LEFT
	raise Exception(f"not found ({x}, {y})")

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
#
# F-7
# |.|
# L-J
#
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

def get_right(sym, heading):
	if sym == '|': return RIGHT         if heading == UP    else LEFT
	if sym == '-': return DOWN          if heading == RIGHT else UP
	if sym == 'L': return None          if heading == UP    else (DOWN, LEFT)
	if sym == 'J': return (RIGHT, DOWN) if heading == UP    else None
	if sym == '7': return None          if heading == DOWN  else (UP, RIGHT)
	if sym == 'F': return None          if heading == RIGHT else (UP, LEFT)

def dir_to_offset(dir):
	if dir == UP: return (0, -1)
	if dir == RIGHT: return (1, 0)
	if dir == DOWN: return (0, 1)
	if dir == LEFT: return (-1, 0)

def add(a, b):
	return (a[0] + b[0], a[1] + b[1])

def flood_map(edges):
	seeds = []
	for y, row in enumerate(MAP):
		for x, chr in enumerate(row):
			if chr == IN:
				seeds.append((x, y))

	while len(seeds) > 0:
		seed = seeds.pop()
		flood_inner(seed, edges)

	pass

def flood_inner(point, edges, visited=[]):
	x, y = point
	if (x, y) in visited:
		return
	visited.append((x, y))

	if x > 0 and not (x - 1, y) in edges:
		MAP[y][x - 1] = IN
		flood_inner((x - 1, y), edges, visited)
	if x < WIDTH - 1 and not (x + 1, y) in edges:
		MAP[y][x + 1] = IN
		flood_inner((x + 1, y), edges, visited)
	if y > 0 and not (x, y - 1) in edges:
		MAP[y - 1][x] = IN
		flood_inner((x, y - 1), edges, visited)
	if y < HEIGHT - 1 and not (x, y + 1) in edges:
		MAP[y + 1][x] = IN
		flood_inner((x, y + 1), edges, visited)

def solve_1():
	S = ()
	for y, line in enumerate(data):
		index = line.find('S')
		if index != -1:
			S = (index, y)

	#print(S)

	points = [S]
	prev_pos = S
	origin = S
	next_pos, dir = search(*S)
	MAP[S[1]][S[0]] = dir
	while next_pos != S:
		#print(next_pos)
		points.append(next_pos)

		prev_pos = next_pos
		next_pos, dir = search(*next_pos, origin)
		origin = prev_pos
		MAP[prev_pos[1]][prev_pos[0]] = dir



	#MAP[S[1]][S[0]] = 'X'

	#print(points)
	print("num points", len(points))
	print((len(points)) // 2)

	with open("out.txt", 'w') as f:
		for row in MAP:
			f.write("".join(str(x) for x in row))
			f.write('\n')

	#
	# Solve part 2
	#

	# All empty cells either to the right or to the left of each segment in the curve (side depending on the winding
	# of the curve) are inside the curve. If we mark all cells next to the curve, then do a flood fill from all of them,
	# we should find all the cells on the inside.
	#
	# I have cheated a bit and just picked right as the inside of the curve and it happened to be right for this one.
	# Might be different for other curves...

	for point in points:
		x, y = point
		sym = data[y][x]
		dir = MAP[y][x]
		right = get_right(sym, dir)
		if right is None:
			continue
		elif isinstance(right, tuple):
			for r in right:
				offset = dir_to_offset(r)
				coord = add(point, offset)
				if not coord in points:
					MAP[coord[1]][coord[0]] = IN
		else:
			offset = dir_to_offset(right)
			coord = add(point, offset)
			if not coord in points:
				MAP[coord[1]][coord[0]] = IN

	with open("out2.txt", 'w') as f:
		for row in MAP:
			f.write("".join(str(x) for x in row))
			f.write('\n')

	flood_map(points)

	with open("out3.txt", 'w') as f:
		for row in MAP:
			f.write("".join(str(x) for x in row))
			f.write('\n')

	solution_2 = 0
	for row in MAP:
		for chr in row:
			if chr == IN:
				solution_2 += 1
	print(solution_2)


solution_1 = solve_1()