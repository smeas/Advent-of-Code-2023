#
# Day 11
# Solution 1: 9521550
# Solution 2: 298932923702
#
#

data = open("input.txt").read().splitlines()
data = [*map(list, data)]

def find_expanded(cols, rows):
	EMPTY_ROW = '.' * len(data[0])
	index = 0
	while index < len(data):
		if data[index] == list(EMPTY_ROW):
			rows.append(index)

		index += 1

	index = 0
	while index < len(data[0]):
		is_empty = True
		for row_index in range(len(data)):
			if data[row_index][index] != '.':
				is_empty = False
				break

		if is_empty:
			cols.append(index)

		index += 1

def manhattan_distance_with_expansion(a, b, expanded_cols, expanded_rows, expansion_factor):
	extra_distance = 0
	lo_x, hi_x = sort2(a[0], b[0])
	for i in range(lo_x, hi_x):
		if i in expanded_cols:
			extra_distance += expansion_factor - 1

	lo_y, hi_y = sort2(a[1], b[1])
	for i in range(lo_y, hi_y):
		if i in expanded_rows:
			extra_distance += expansion_factor - 1

	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + extra_distance

def sort2(a, b):
	return (a, b) if a < b else (b, a)

def solve(expansion_factor=1):
	expanded_cols = []
	expanded_rows = []
	find_expanded(expanded_cols, expanded_rows)

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
			total += manhattan_distance_with_expansion(
				points[a], points[b], expanded_cols, expanded_rows, expansion_factor)
			b += 1

		a += 1

	# for line in data:
	# 	print(line)

	return total


solution_1 = solve(2)
print(solution_1)
solution_2 = solve(1000000)
print(solution_2)
