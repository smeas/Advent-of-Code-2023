#
# Day 07 (part 1)
# Solution 1: 248812215
# Solution 2:
#
#

#data = open("example.txt").read().splitlines()
data = open("input.txt").read().splitlines()

CARDS = "AKQJT98765432"

def parse_line(s):
	hand, bid = s.split()
	return hand, int(bid)

def get_type_order(hand):
	a, b, c, d, e = sorted(hand)
	if a==b==c==d==e:
		return 0
	if a==b==c==d or b==c==d==e:
		return 1
	if a==b and c==d==e or a==b==c and d==e:
		return 2
	if a==b==c or b==c==d or c==d==e:
		return 3
	if a==b and c==d or a==b and d==e or b==c and d==e:
		return 4
	if a==b or b==c or c==d or d==e:
		return 5
	return 6

def get_second_orderings(hand):
	return [*map(lambda x: CARDS.index(x), hand)]

def solve_1():
	solution = 0
	hands = [*map(parse_line, data)]
	#print([*map(lambda x: (x[0], get_type_order(x[0])), hands)])

	ordered_hands = reversed(sorted(hands, key=lambda x: (get_type_order(x[0]), *get_second_orderings(x[0]))))
	for i, hand in enumerate(ordered_hands):
		#print(i, hand)
		hand, bid = hand
		#print(bid * (i + 1))
		solution += bid * (i + 1)

	return solution


first_solution = solve_1()
print(first_solution)
assert first_solution == 248812215
