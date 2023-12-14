#
# Day 13
# Solution 1: 34202
# Solution 2:
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
			total += 100 * (y_to_check + 1)

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
			total += x_to_check + 1

	return total

def solve_1():
	total = 0
	for puzzle in puzzles:
		value = calc_puzzle(puzzle.splitlines())
		total += value
		#print(total, value)

	return total

solution_1 = solve_1()
print(solution_1)
