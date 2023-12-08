#
# Day 08
# Solution 1: 24253
# Solution 2: 12357789728873
#
#

# Starting at the nodes where the key ends with 'A', we get 6 different paths that eventually reaches a cycle repeating
# indefinetly. (think PRNG)
#
# I used the following code to figure out when the paths starts to cycle:
#
# def figure_out_cycles(node: Node, instructions, start_index=0, prev_result=None, total_count=0):
# 	# (node, instruction_index)
# 	cache = set()
# 	print("start:", node)

# 	current = node
# 	cache.add((current, 0))
# 	ends = []
# 	count = 0
# 	while True:
# 		for i in range(start_index, len(instructions)):
# 			instr = instructions[i]
# 			count += 1
# 			current = current.get_next(instr)
# 			pair = (current, i)
# 			if pair in cache:
# 				print("Repeat!", current, i, count, ends, total_count + count)
# 				result = (current, i, count)
# 				if result == prev_result:
# 					print(f"Done: '{node}' {i=} {count=} {ends=} totalCount={total_count + count}")
# 					return

# 				return figure_out_cycles(current, instructions, start_index=i+1, prev_result=result, total_count=total_count + count)
# 			cache.add(pair)
# 			if current.is_end:
# 				ends.append((count, total_count + count))
# 		start_index = 0
#
# I figured out that the ending nodes (key ends with 'Z') started repeating at a constant interval after:
# 72759 43594 43287 48813 41138 39603 steps on each of the six paths, with the intervals being:
# 24253 21797 14429 16271 20569 13201.
#
# For some reason (the input data playing nice?) the intervals are all divisible by the steps it took to get to the
# repeating pattern: 3 2 3 3 2 3
#
# This means that as long as the answer is higher than where the points of repeat are (which I know it isn't,
# because if it was, the brute force solution would complete almost instantly), we can take a big shortcut and just
# need to find a multiple of all the intervals where their values become the same. Essentially we can just assume the
# path is in a constant cycle from the start. So there is no need to actually compute where the cycles lie in the paths.

import math
from typing import Self, Dict, List
data = open("input.txt").read().splitlines()

class Node:
	key: str
	value: (str, str)
	left: Self
	right: Self
	is_start: bool
	is_end: bool

	def get_next(self, instr):
		if instr == 'L':
			return self.left
		elif instr == 'R':
			return self.right

	def __str__(self) -> str:
		return f"{self.key} = {self.value}"

def find_distance_to_end(node: Node, instructions):
	current = node
	count = 0
	print("start:", node)
	while True:
		for instr in instructions:
			count += 1
			current = current.get_next(instr)
			if current.is_end:
				print("end:", count)
				return count

def solve_2():
	nodes = {} # type: Dict[str, Node]
	instructions = data[0]

	for line in data[2:]:
		key = line[0:3]
		value = (line[7:10], line[12:15])

		node = Node()
		node.key = key
		node.value = value
		node.is_start = key.endswith('A')
		node.is_end = key.endswith('Z')
		nodes[key] = node

	start_nodes = [] # type: List[Node]
	for node in nodes.values():
		node.left = nodes[node.value[0]]
		node.right = nodes[node.value[1]]
		if node.is_start:
			start_nodes.append(node)

	end_repeat_intervals = []
	for node in start_nodes:
		end_repeat_intervals.append(find_distance_to_end(node, instructions))

	return math.lcm(*end_repeat_intervals)


second_solution = solve_2()
print(second_solution)
assert second_solution == 12357789728873


