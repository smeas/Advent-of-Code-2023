#
# Day 12
# Solution 1:
# Solution 2:
#
#

data = open("input.txt").read().splitlines()

def parse_line(line):
	pattern, values = line.split()
	values = [*map(int, values.split(","))]
	return pattern, values

def decode_pattern(pattern):
	group_count = 0
	values = []
	for chr in pattern:
		match chr:
			case "#":
				group_count += 1
			case ".":
				if group_count > 0:
					values.append(group_count)
					group_count = 0

	if group_count > 0:
		values.append(group_count)
	return values

def is_match(pattern, values):
	# print(decode_pattern(pattern), values)
	return decode_pattern(pattern) == values

def solve_1():
	total = 0
	n = 0
	for line in data:
		pattern, values = parse_line(line)
		bits = pattern.count("?")
		for i in range(2**bits):
			pat = list(pattern)
			b = bin(i)[2:].rjust(bits, "0")
			#bin(bin(i)[2:]).rjust(bits, "0").replace("0", ".").replace("1", "#")

			j = 0
			for i, value in enumerate(pat):
				if value != "?":
					continue

				pat[i] = "#" if b[j] == "1" else "."

				# if j < len(b):
				# 	pat[i] = "#" if b[j] == "1" else "."
				# else:
				# 	pat[i] = "."
				j += 1

			#print(pat, b, j)
			# print(pat, values)
			if is_match(pat, values):
				total += 1
		#break
		n += 1
		print(n)

	return total

solution_1 = solve_1()
print(solution_1)
