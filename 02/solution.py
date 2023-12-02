#
# Day 02
# Solution 1: 2727
# Solution 2: 56580
#
#

# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()
data = open("input.txt").read().splitlines()
colors = ["red", "green", "blue"]

def parse_hint(hint: str):
	out = [0, 0, 0]
	for color in hint.split(", "):
		num, name = color.split(" ")
		print(num, name)
		out[colors.index(name)] = int(num)

	print("-")
	return out

def check_enough_cubes(hint):
	red, green, blue = hint
	if red > 12 or green > 13 or blue > 14:
		return False

	return True

def calculate_minimum_power(hints):
	max = [0, 0, 0]
	for hint in hints:
		for i in range(3):
			if hint[i] > max[i]:
				max[i] = hint[i]

	r, g, b = max
	power = r * g * b
	print("Max:", max)
	print("Power:", power)
	return power


first_solution = 0
second_solution = 0
for line in data:
	num = line[5:].split(":")[0]
	game_id = int(num)
	print("Game:", game_id)

	line = line.split(": ", 1)[1]
	hints = [ parse_hint(hint) for hint in line.split("; ") ]

	if all(check_enough_cubes(hint) for hint in hints):
		first_solution += game_id

	second_solution += calculate_minimum_power(hints)

print("Solution 1:", first_solution)
print("Solution 2:", second_solution)
