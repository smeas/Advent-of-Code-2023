#
# Day 06
# Solution 1: 2344708
# Solution 2: 30125202
#
#

import math

data = open("input.txt").read().splitlines()

# t1 = T - t0
# v = t0
#
# f(t0) = v * t1
# f(t0) = T*t0 - t0^2
#
# 0 = f(t0) - D
# t0 = (T / 2) + sqrt((-T / 2)^2 - D)
def find_roots(record_time, record_distance):
	a = record_time / 2
	b = math.sqrt((-record_time / 2)**2 - record_distance)
	return math.ceil(a - b), math.floor(a + b)

def solve_1():
	times = [*map(int, data[0].split()[1:])]
	distances = [*map(int, data[1].split()[1:])]
	solution = 1
	for time, dist in zip(times, distances):
		a, b = find_roots(time, dist)
		m = 1 + b - a # number of integers above the curve
		solution *= m
	return solution

def solve_2():
	time = int("".join(data[0].split()[1:]))
	dist = int("".join(data[1].split()[1:]))
	a, b = find_roots(time, dist)
	return 1 + b - a # number of integers above the curve


first_solution = solve_1()
print(first_solution)
assert first_solution == 2344708

second_solution = solve_2()
print(second_solution)
assert second_solution == 30125202