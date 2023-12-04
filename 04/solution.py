#
# Day 04
# Solution 1: 24160
# Solution 2: 5659035
#
#

data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()
data = open("input.txt").read().splitlines()
cards = []

def extract_numbers(s):
	return [*map(int, s.split())]

first_solution = 0
for line in data:
	a = line.split(":")[1].split("|")
	correct = extract_numbers(a[0])
	mine = extract_numbers(a[1])

	num_correct = 0

	for number in mine:
		if number in correct:
			num_correct += 1

	cards.append(num_correct)

	if num_correct > 0:
		first_solution += 2**(num_correct - 1)

print(cards)

second_solution = 0
def handle_card(card_index):
	global second_solution
	second_solution += 1
	value = cards[card_index]
	if value > 0:
		for i in range(value):
			handle_card(card_index + i + 1)

for i in range(len(cards)):
	handle_card(i)

print("Solution 1:", first_solution)
print("Solution 2:", second_solution)
