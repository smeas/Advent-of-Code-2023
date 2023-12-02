#
# Day 01 (v2)
# Solution 1: 54331
# Solution 2: 54518
#
#

data = open("input.txt").readlines()

numbers = [
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
]

def extract_value_1(s: str):
	digits = list(filter(str.isdigit, s))
	return int(digits[0] + digits[-1])

def extract_value_2(s: str):
	digits = ( try_parse_digit_at(s, index) for index in range(len(s)) )
	digits = [ x for x in digits if x is not None ]
	return digits[0] * 10 + digits[-1]

def try_parse_digit_at(s: str, index: int):
	if s[index].isdigit():
		return int(s[index])

	substr = s[index:]
	for number_index, digit in enumerate(numbers):
		if substr.startswith(digit):
			return number_index + 1

	return None

print(sum(map(extract_value_1, data)))
print(sum(map(extract_value_2, data)))
