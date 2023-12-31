#
# Day 08
# Solution 1: 24253
# Solution 2:
#
#

data = open("input.txt").read().splitlines()


def solve_1():
	nodes = {}
	instructions = []
	for chr in data[0]:
		if chr == 'L':
			instructions.append(0)
		elif chr == 'R':
			instructions.append(1)

	for line in data[2:]:
		key = line[0:3]
		value = (line[7:10], line[12:15])
		nodes[key] = value

	current = nodes['AAA']
	steps = 0
	while True:
		for instr in instructions:
			steps += 1
			key = current[instr]
			current = nodes[key]
			if key == 'ZZZ':
				return steps

first_solution = solve_1()
print(first_solution)
assert first_solution == 24253