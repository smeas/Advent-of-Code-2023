#
# Day 15
# Solution 1: 517315
# Solution 2: 247763
#
#

input = open("input.txt").read()

def HASH(s):
	acc = 0
	for char in s:
		acc += ord(char)
		acc *= 17
		acc %= 256
	return acc

def solve_1():
	total = sum(map(HASH, input.split(",")))
	return total

#
# Part 2
#

class HASHMAP:
	def __init__(self):
		self.buckets = []
		for i in range(256):
			self.buckets.append([])

	def set(self, key, value):
		h = HASH(key)
		if h > 255: print(h)
		bucket = self.buckets[h]
		for i, pair in enumerate(bucket):
			if pair[0] == key:
				bucket[i] = (key, value)
				return

		bucket.append((key, value))

	def remove(self, key):
		h = HASH(key)
		bucket = self.buckets[h]
		for i, pair in enumerate(bucket):
			if pair[0] == key:
				return bucket.pop(i)

		return None

def solve_2():
	total = 0
	hmap = HASHMAP()
	for elem in input.split(","):
		if elem.endswith("-"):
			key = elem.split("-")[0]
			hmap.remove(key)
		elif "=" in elem:
			key, value = elem.split("=")
			hmap.set(key, int(value))

	for bucket_i, bucket in enumerate(hmap.buckets):
		for slot_i, pair in enumerate(bucket):
			focus_power = (1 + bucket_i) * (1 + slot_i) * pair[1]
			total += focus_power

	return total


print(solve_1())
print(solve_2())
