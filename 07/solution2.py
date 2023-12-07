#
# Day 07 (part 2)
# Solution 1:
# Solution 2: 250057090
#
#

data = open("input.txt").read().splitlines()

CARDS = "AKQT98765432J"

def parse_line(s):
	hand, bid = s.split()
	return hand, int(bid)

def count_cards(hand):
	counts = [0] * len(CARDS)
	joker_count = hand.count("J")
	for i, card in enumerate(CARDS[:-1]):
		counts[i] = hand.count(card)
	return counts, joker_count

def find_match(num, counts, joker_count, exclude=None):
	for i, count in enumerate(counts):
		value = count + joker_count
		if value >= num and CARDS[i] != exclude:
			jokers_left = value - num
			return CARDS[i], jokers_left
	return None, None

def get_type_order(hand):
	counts, joker_count = count_cards(hand)
	card, _ = find_match(5, counts, joker_count)
	if card: return 0

	card, _ = find_match(4, counts, joker_count)
	if card: return 1

	card1, jokers_left = find_match(3, counts, joker_count)
	if card1:
		card2, _ = find_match(2, counts, jokers_left, exclude=card1)
		if card2: return 2

	card, _ = find_match(3, counts, joker_count)
	if card: return 3

	card1, jokers_left = find_match(2, counts, joker_count)
	if card1:
		card2, _ = find_match(2, counts, jokers_left, exclude=card1)
		if card2: return 4

	card, _ = find_match(2, counts, joker_count)
	if card: return 5

	return 6

def get_second_orderings(hand):
	return [*map(lambda x: CARDS.index(x), hand)]

def solve_2():
	solution = 0
	hands = [*map(parse_line, data)]
	#print([*map(lambda x: (x[0], get_type_order(x[0])), hands)])
	#print("\n".join([*map(lambda x: str((x[0], ["five","four","house","three","2pair","two","no"][get_type_order(x[0])])), hands)]))

	ordered_hands = reversed(sorted(hands, key=lambda x: (get_type_order(x[0]), *get_second_orderings(x[0]))))
	for i, hand in enumerate(ordered_hands):
		#print(i, hand)
		hand, bid = hand
		#print(bid * (i + 1))
		solution += bid * (i + 1)

	return solution


second_solution = solve_2()
print(second_solution)
assert second_solution == 250057090