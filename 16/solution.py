#
# Day 16
# Solution 1: 7210
# Solution 2:
#
#

data = open("input.txt").read().splitlines()

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

WIDTH = len(data[0])
HEIGHT = len(data)

def reflect(op, in_dir):
	if op == "/":
		if in_dir == UP: return RIGHT
		if in_dir == RIGHT: return UP
		if in_dir == DOWN: return LEFT
		if in_dir == LEFT: return DOWN
	elif op == "\\":
		if in_dir == UP: return LEFT
		if in_dir == RIGHT: return DOWN
		if in_dir == DOWN: return RIGHT
		if in_dir == LEFT: return UP

def split(op, in_dir):
	if op == "|":
		if in_dir == UP: return UP
		if in_dir == RIGHT: return [UP, DOWN]
		if in_dir == LEFT: return [UP, DOWN]
		if in_dir == DOWN: return DOWN
	elif op == "-":
		if in_dir == UP: return [LEFT, RIGHT]
		if in_dir == RIGHT: return RIGHT
		if in_dir == LEFT: return LEFT
		if in_dir == DOWN: return [LEFT, RIGHT]

def is_in_bounds(pos):
	if pos[0] < 0 or pos[0] >= WIDTH:
		return False
	if pos[1] < 0 or pos[1] >= HEIGHT:
		return False
	return True

def add_vec(a, b):
	return (a[0] + b[0], a[1] + b[1])

def search(marked, pos, dir, loop_guard=set()):
	while True:
		if not is_in_bounds(pos):
			break
		if (pos, dir) in loop_guard:
			break

		marked.add(pos)
		loop_guard.add((pos, dir))
		sym = data[pos[1]][pos[0]]
		if sym == ".":
			pos = add_vec(pos, dir)
		elif sym in ("/", "\\"):
			dir = reflect(sym, dir)
			pos = add_vec(pos, dir)
		elif sym in ("-", "|"):
			new_dirs = split(sym, dir)
			if isinstance(new_dirs, list):
				# Split into second laser
				split_dir = new_dirs[0]
				split_pos = add_vec(pos, split_dir)
				search(marked, split_pos, split_dir, loop_guard)

				# Keep going in the other direction
				dir = new_dirs[1]
				pos = add_vec(pos, dir)
			else:
				dir = new_dirs
				pos = add_vec(pos, dir)


def solve_1():
	marked = set()
	pos = (0, 0)
	dir = RIGHT
	search(marked, pos, dir)

	#print(marked)
	return len(marked)

print(solve_1())
