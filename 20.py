# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 20

import sys
import re
import time
import itertools
import math

# calculating execution time
start_time = time.time()

# vars
ret1 = ret2 = 0

# limit
num = 34000000

# counting how many presents are present in each house (pun intended)
houses = [0 for x in range(num//10)]

# part A
for i in range(1, num//10):
	# every i-th house
	for j in range(i, num//10, i):
		houses[j] += 10 * i
	# check
	if houses[i] >= num:
		ret1 = i
		break

# reset and part B
houses = [0 for x in range(num//10)]
for i in range(1, num//10):
	# only the next 50 houses
	for j in range(50):
		if i +j*i >= num//10:
			break
		houses[i + j*i] += 11 * i
	# check
	if houses[i] >= num:
		ret2 = i
		break	

# print the output
print("Solution: ", ret1, ret2)
# 786240 831600

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))