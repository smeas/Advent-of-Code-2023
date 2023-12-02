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

def e(*x):0
# def parse_hint(hint: str):
# 	out = [0, 0, 0]
# 	e(*map(
# 		lambda s:
# 			(lambda v,n:
# 				out.__setitem__("rgb".index(n[0]), int(v))
# 			)(*s.split(" ")),
# 			hint.split(", ")
# 	))
# 	# for color in hint.split(", "):
# 	# 	num, name = color.split(" ")
# 	# 	#print(num, name)
# 	# 	out["rgb".index(name[0])] = int(num)
# 	return out


def parse_hint(hint: str, o):
	return o,*map(
		lambda s:
			(lambda v,n:
				o.__setitem__("rgb".index(n[0]), int(v))
			)(*s.split()),
			hint.split(", ")
	)

def check_enough_cubes(hint):
	print(hint)
	red, green, blue = hint
	if red > 12 or green > 13 or blue > 14:
		return False

	return True

# def calculate_minimum_power(hints):
# 	r,g,b=map(
# 		lambda i: max(h[i] for h in hints),
# 		range(3))
# 	return r*g*b

def calculate_minimum_power(hints):
	return eval("*".join(map(
		str,
		map(
			lambda i: max(h[i] for h in hints),
			range(3))
	)))


first_solution = 0
second_solution = 0
# for line in data:
# 	num = line[5:].split(":")[0]
# 	game_id = int(num)
# 	print("Game:", game_id)

# 	line = line.split(": ", 1)[1]
# 	hints = [ parse_hint(hint) for hint in line.split("; ") ]

# 	if all(check_enough_cubes(hint) for hint in hints):
# 		first_solution += game_id

# 	second_solution += calculate_minimum_power(hints)


# second_solution = sum(
# 	map(
# 		lambda l: calculate_minimum_power(
# 			#parse_hint(hint) for hint in l.split(": ")[1].split("; ")
# 			map(parse_hint, l.split(": ")[1].split("; "))
# 		),
# 		data
# 	)
# )


# second_solution = sum(
# 	map(
# 		calculate_minimum_power,
# 		map(
# 			lambda l: [*map(
# 				lambda hc: parse_hint(hc,[0,0,0])[0],
# 				l.split(": ")[1].split("; ")
# 			)],
# 			data
# 		)
# 	)
# )


# second_solution = sum(
# 	map(
# 		lambda a:
# 			eval("*".join(map(
# 				str,
# 				map(
# 					lambda i: max(h[i] for h in a),
# 					range(3))
# 			))),
# 		map(
# 			lambda l: [*map(
# 				lambda hc: parse_hint(hc,[0,0,0])[0],
# 				l.split(": ")[1].split("; ")
# 			)],
# 			data
# 		)
# 	)
# )



print(sum(
	map(
		lambda a:
			eval("*".join(map(
				str,
				map(
					lambda i: max(h[i] for h in a),
					[0,1,2])
			))),
		map(
			lambda l: [*map(
				lambda y: (
					lambda c,o: (o,*map(
						lambda s:
							(lambda v,n:
								o.__setitem__("rgb".index(n[0]), int(v))
							)(*s.split()),
							c.split(", ")
						)
					)[0]
				)(y,[0,0,0]),
				l.split(": ")[1].split("; ")
			)],
			open("i").readlines()
		)
	)
))

print(sum(map(lambda a:eval("*".join(map(str,map(lambda i:max(h[i]for h in a),[0,1,2])))),map(lambda l:[*map(lambda y:(lambda c,o:(o,*map(lambda s:(lambda v,n:o.__setitem__("rgb".index(n[0]),int(v)))(*s.split()),c.split(", ")))[0])(y,[0]*3),l.split(": ")[1].split("; "))],open("i").readlines()))))

#second_solution = sum(map(lambda l:check_enough_cubes(map(parse_hint,l.split(": ")[1].split("; "))),data))

#print("Solution 1:", first_solution)
#print("Solution 2:", second_solution)
