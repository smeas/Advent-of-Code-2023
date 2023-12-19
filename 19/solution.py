#
# Day 19
# Solution 1: 280909
# Solution 2:
#
#

import operator

data = open("input.txt").read()
PARAMETERS = "xmas"
COMPARATORS = {"<": operator.lt, ">": operator.gt}

def parse_data():
	rules = {}
	parts = []
	rulesdata, partsdata = data.split("\n\n")
	for r in rulesdata.splitlines():
		key, rest = r.split("{")
		conds = rest[:-1].split(",")
		else_rule = conds.pop()
		rules[key] = ([*map(parse_cond, conds)], else_rule)

	for p in partsdata.splitlines():
		params = p[1:-1].split(",")
		assert len(params) == 4
		params = tuple(map(lambda s: int(s.split("=")[1]), params))
		parts.append(params)

	return rules, parts

def parse_cond(s):
	param = PARAMETERS.index(s[0])
	comp = s[1]
	value, next_rule = s[2:].split(":")
	return (param, comp, int(value), next_rule)

def process_part(rules, part, start_rule="in"):
	rule = rules[start_rule]
	while True:
		key = eval_rule(rule, part)
		if key == "A": return True
		elif key == "R": return False

		rule = rules[key]

def eval_rule(rule, part):
	for r in rule[0]:
		parami, comp, value, next_rule = r
		if COMPARATORS[comp](part[parami], value):
			return next_rule

	return rule[1] # else rule

def solve_1():
	total = 0
	rules, parts = parse_data()
	for part in parts:
		result = process_part(rules, part)
		# print(result)
		if result:
			total += sum(part)

	return total

print(solve_1())
