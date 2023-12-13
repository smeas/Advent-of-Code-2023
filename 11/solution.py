#
# Day 11
# Solution 1:
# Solution 2:
#
#

data = open("input.txt").read().splitlines()
data = [*map(list, data)]

EMPTY_ROW = '.' * len(data[0])

def expand():
	index = 0
	while index < len(data):
		if data[index] == list(EMPTY_ROW):
			data.insert(index, list(EMPTY_ROW))
			index += 1

		index += 1

	index = 0
	while index < len(data[0]):
		is_empty = True
		for row_index in range(len(data)):
			if data[row_index][index] != '.':
				is_empty = False
				break

		if is_empty:
			for row_index in range(len(data)):
				data[row_index].insert(index, '.')
			index += 1

		index += 1

def manhattan_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve_1():
	expand()

	points = []
	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == '#':
				points.append((x, y))

	total = 0
	a = 0
	while a < len(points):
		b = a + 1
		while b < len(points):
			total += manhattan_distance(points[a], points[b])
			b += 1

		a += 1

	for line in data:
		print(line)

	return total




solution_1 = solve_1()
print(solution_1)
