#
# Day 05
# Solution 1: 157211394
# Solution 2: ???
#
#

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()
data = open("input.txt").read().splitlines()
maps = []

def extract_numbers(s):
	#print("extract: ", s)
	return [*map(int, s.split())]

def map_seed_to_location(value):
	for map in maps:
		for mappping in map:
			if value in mappping[1]:
				#print(f"mapping {value} to {(value - mappping[1].start) + mappping[0].start}")
				value = (value - mappping[1].start) + mappping[0].start
				break
	return value

first_solution = 0
second_solution = 0

# Parse maps
seeds = extract_numbers(data[0].split(": ")[1])
print(seeds)

current_line = 3
current_map = []
while current_line < len(data):
	line = data[current_line]
	if line == "":
		maps.append(current_map)
		current_map = []
		current_line += 2
		continue

	s1, s2, l = extract_numbers(line)
	current_map.append((range(s1, s1 + l), range(s2, s2 + l)))
	current_line += 1

maps.append(current_map)

print(maps)

locations1 = []
for seed in seeds:
	value = map_seed_to_location(seed)
	locations1.append(value)

first_solution = min(locations1)

# TODO: Brute force not possible. Seed ranges are too large.
locations2 = []
for s, l in zip(seeds[::2], seeds[1::2]):
	for seed in range(s, s + l):
		value = map_seed_to_location(seed)
		locations2.append(value)

second_solution = min(locations2)

print("Solution 1:", first_solution)
print("Solution 2:", second_solution)
