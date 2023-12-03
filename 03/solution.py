#
# Day 03
# Solution 1: 527446
# Solution 2: 73201705
#
#

import re

# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()
data = open("input.txt").read().splitlines()
line_length = len(data[0])
gear_map = {}

def check_symbols_around(x, y, length, value):
	for check_y in range(y - 1, y + 1 + 1):
		if not 0 <= check_y < len(data):
			continue

		for check_x in range(x - 1, x + length + 1):
			if not 0 <= check_x < line_length:
				continue

			char = data[check_y][check_x]
			if char == "*":
				pos = (check_x, check_y)
				gear_list = gear_map.get(pos, [])
				gear_map[pos] = gear_list
				gear_list.append(value)

			if char != "." and not char.isdigit():
				return True

	return False

first_solution = 0
for line_index, line in enumerate(data):
	for number_match in re.finditer("[0-9]+", line):
		begin, end = number_match.span()
		value = int(number_match.group())
		if check_symbols_around(begin, line_index, end - begin, value):
			#print(value)
			first_solution += value

second_solution = 0
for k,v in gear_map.items():
	if len(v) == 2:
		second_solution += v[0] * v[1]

print("Solution 1:", first_solution)
print("Solution 2:", second_solution)
