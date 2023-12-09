#
# Day 09
# Solution 1: 1757008019
# Solution 2: 995
#
#

data = open("input.txt").read().splitlines()

def all_same(seq):
	a = seq[0]
	for x in seq:
		if x != a:
			return False
	return True

def calc_next_value(values, calc_next):
	if all_same(values):
		return values[0]

	new_seq = []
	for prev, curr in zip(values, values[1:]):
		new_seq.append(curr - prev)

	if calc_next:
		return values[-1] + calc_next_value(new_seq, calc_next)
	else: # prev
		return values[0] - calc_next_value(new_seq, calc_next)

def solve():
	total_1 = 0
	total_2 = 0

	for line in data:
		values = [*map(int, line.split())]
		total_1 += calc_next_value(values, True)
		total_2 += calc_next_value(values, False)

	return total_1, total_2

solution_1, solution_2 = solve()
print(solution_1)
print(solution_2)
