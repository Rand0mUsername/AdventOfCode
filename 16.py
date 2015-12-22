# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 16

import sys
import re
import time
import itertools

# calculating execution time
start_time = time.time()

# IO
in_file = open("16.in")

# all the information we have
data = dict()
data["children"] = 3
data["samoyeds"] = 2
data["akitas"] = 0
data["vizslas"] = 0
data["cars"] = 2
data["perfumes"] = 1
data["goldfish"] = 5 # part B: <
data["pomeranians"] = 3 # part B: <
data["trees"] = 3 # part B: >
data["cats"] = 7 # part B: >

# Part B: Check if (key, value) pair matches the required values
def ok(k, v):
	if k == "goldfish" or k == "pomeranians": 
		if v < data[k]:
			return True
		else:
			return False
	elif k == "trees" or k == "cats":
		if v > data[k]:
			return True
		else:
			return False
	elif v == data[k]:
		return True
	else:
		return False

# process input
lines = in_file.readlines()
for line in lines:
	# split the line
	lst = re.split(r'[^\w\d]+', line.strip())
	# part A: simple equality
	if data[ lst[2] ] == int(lst[3]) and data[ lst[4] ] == int(lst[5]) and data[ lst[6] ] == int(lst[7]):
		ret1 = int(lst[1])
	# part B: ok function
	if ok(lst[2], int(lst[3])) and ok(lst[4], int(lst[5])) and ok(lst[6], int(lst[7])):
		ret2 = int(lst[1])

# print the solution
print("Solution: ", ret1, ret2)
# 373 260

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))