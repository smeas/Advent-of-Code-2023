#
# Day 13
# Solution 1: 34202
# Solution 2: 34230
#
#

puzzles = open("input.txt").read().split("\n\n")

def eq_row(table, a, b):
	return table[a] == table[b]

def eq_col(table, a, b):
	for row in range(len(table)):
		if table[row][a] != table[row][b]:
			return False

	return True

def diff_row(table, a, b) -> (int, int):
	differences = 0
	first_diff_index = -1
	for col in range(len(table[0])):
		if table[a][col] != table[b][col]:
			differences += 1
			if first_diff_index == -1:
				first_diff_index = col

	return (differences, first_diff_index)

def diff_col(table, a, b) -> (int, int):
	differences = 0
	first_diff_index = -1
	for row in range(len(table)):
		if table[row][a] != table[row][b]:
			differences += 1
			if first_diff_index == -1:
				first_diff_index = row

	return (differences, first_diff_index)

def calc_puzzle(data):
	total = 0
	width = len(data[0])
	height = len(data)
	for y_to_check in range(height - 1):
		success = True
		left = y_to_check
		right = y_to_check + 1
		while left >= 0 and right < height:
			if not eq_row(data, left, right):
				success = False
				break
			left -= 1
			right += 1

		if success:
			#print("ymatch:", y_to_check)
			return 100 * (y_to_check + 1), None, y_to_check

	for x_to_check in range(width - 1):
		success = True
		left = x_to_check
		right = x_to_check + 1
		while left >= 0 and right < width:
			if not eq_col(data, left, right):
				success = False
				break
			left -= 1
			right += 1

		if success:
			#print("xmatch:", x_to_check)
			return x_to_check + 1, x_to_check, None

	return 0

def calc_puzzle_2(data, ignore_x, ignore_y):
	width = len(data[0])
	height = len(data)
	for y_to_check in range(height - 1):
		if y_to_check == ignore_y:
			continue

		ignored_errors = 0
		success = True
		left = y_to_check
		right = y_to_check + 1
		while left >= 0 and right < height:
			diffs, first_diff = diff_row(data, left, right)
			if diffs != 0:
				if ignored_errors >= 1 or diffs > 1:
					success = False
					break
				else: # diffs == 1
					ignored_errors += 1

			left -= 1
			right += 1

		if success:
			#print("ymatch:", y_to_check)
			return 100 * (y_to_check + 1)

	for x_to_check in range(width - 1):
		if x_to_check == ignore_x:
			continue

		ignored_errors = 0
		success = True
		left = x_to_check
		right = x_to_check + 1
		while left >= 0 and right < width:
			diffs, first_diff = diff_col(data, left, right)
			if diffs != 0:
				if ignored_errors >= 1 or diffs > 1:
					success = False
					break
				else: # diffs == 1
					ignored_errors += 1

			left -= 1
			right += 1

		if success:
			#print("xmatch:", x_to_check)
			return x_to_check + 1

	return 0

def solve_1():
	total_1 = 0
	total_2 = 0
	for puzzle in puzzles:
		puzzle = puzzle.splitlines()
		value, xindex, yindex = calc_puzzle(puzzle)
		total_1 += value

		value2 = calc_puzzle_2(puzzle, xindex, yindex)
		total_2 += value2
		#print(total_1, total_2, value, value2)

	return total_1, total_2

solution_1, solution_2 = solve_1()
print(solution_1)
print(solution_2)