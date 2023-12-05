#
# Day 05
# Solution 1: 157211394
# Solution 2: 50855035
#
#

from typing import Tuple, List

#data = open("example.txt").read().splitlines()
data = open("input.txt").read().splitlines()

SEEDS = [] # type: List[int]
MAPS = [] # type: List[List[Tuple[range, range]]]


#
# Solution 1
#

def extract_numbers(s):
	#print("extract: ", s)
	return [*map(int, s.split())]

# Parse maps
def parse_input():
	seeds = extract_numbers(data[0].split(": ")[1])
	#print(seeds)

	maps = []
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
	return seeds, maps

def map_seed_to_location(value):
	for map in MAPS:
		for mappping in map:
			if value in mappping[1]:
				value = (value - mappping[1].start) + mappping[0].start
				break
	return value

def calc_solution_1():
	return min(map(map_seed_to_location, SEEDS))


#
# Solution 2
#

# Split range a into up to three parts. (x, [y, z])
# x    :: the part of a that is contained within b, None if no overlap
# y, z :: parts of a that does not overlap with b
def split_range(a: range, b: range) -> Tuple[range, List[range]]:
	a_start_in_b = a.start >= b.start and a.start < b.stop
	a_stop_in_b = a.stop <= b.stop and a.stop > b.start
	if a_start_in_b and a_stop_in_b:
		# This means that a is fully contained in b
		#   0123456789
		# a   |-|
		# b |-----|
		return (a, [])
	elif a_start_in_b:
		# a starts within b, but ends outside
		#   0123456789
		# a    |-----|
		# b |-----|
		return (range(a.start, b.stop), [range(b.stop, a.stop)])
	elif a_stop_in_b:
		# a starts outside b, but ends within it
		#   0123456789
		# a |-----|
		# b    |-----|
		return (range(b.start, a.stop), [range(a.start, b.start)])
	elif a.start < b.start and a.stop > b.stop:
		# b is contained within a.
		#   0123456789
		# a |-----|
		# b   |-|
		left = range(a.start, b.start)
		right = range(b.stop, a.stop)
		return (b, [left, right])
	else:
		# The ranges do not overlap.
		#   0123456789
		# a |--|
		# b      |--|
		return (None, [])

def apply_range_mapping(in_range, source_range, dest_range):
	diff = dest_range.start - source_range.start
	return range(in_range.start + diff, in_range.stop + diff)

# Take a single range and map it according to a list of range mappings, producing a list of one or more new ranges.
def map_range(mapping_list: List[Tuple[range, range]], seed: range) -> List[range]:
	ranges_to_split = [seed]
	mapped_ranges = []

	# Split the ranges down into parts based on which mapping ranges they belong to / overlap with. This is done until
	# there are no more ranges that map to any mappings in the mapping list.
	while len(ranges_to_split) > 0:
		new_ranges = []

		for range_to_split in ranges_to_split:

			for mapping in mapping_list:
				dest_map_range, source_map_range = mapping
				overlapping_range, split_ranges = split_range(range_to_split, source_map_range)

				if overlapping_range:
					mapped_range = apply_range_mapping(overlapping_range, source_map_range, dest_map_range)
					mapped_ranges.append(mapped_range)
					# Any excess range(s) that was not contained within the mapping range. We need to keep
					# processing them.
					new_ranges.extend(split_ranges)
					break
			else:
				# The range did not overlap with any mapping range. Therefore it maps to itself.
				mapped_ranges.append(range_to_split)

		ranges_to_split = new_ranges

	return mapped_ranges

def calc_solution_2():
	# Construct the initial ranges from the seeds list
	ranges = [*map(
		lambda s: range(s[0], s[0] + s[1]),
		zip(SEEDS[::2], SEEDS[1::2]))]

	# Apply all maps in sequence to the ranges
	for current_map in MAPS:
		new_ranges = []
		for current_range in ranges:
			out = map_range(current_map, current_range)
			new_ranges.extend(out)

		ranges = new_ranges

	# Solution is the lowest range start value.
	return min(map(lambda r: r.start, ranges))


#
# Compute solutions
#

SEEDS, MAPS = parse_input()
first_solution = calc_solution_1()
second_solution = calc_solution_2()
print("Solution 1:", first_solution)
print("Solution 2:", second_solution)
