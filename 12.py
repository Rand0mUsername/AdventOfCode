# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 12

import sys
import re
import time
import json

# calculating execution time
start_time = time.time()

# IO
in_file = open("12.in")
raw_json = in_file.readline().strip()

# regex for part A
nums = re.compile(r"-?[\d]+")

# ret
ret1 = 0
ret2 = 0

# Part A: find all numbers using nums regex
ret1 = sum( map(int, nums.findall(raw_json)) )

# Part B: parse
def parse(items):
	ret = 0
	# iterate
	for it in items:
		# branch list/dict
		if isinstance(items, dict):
			value = items[it]
		else:
			value = it
	    # actual parsing
		if isinstance(value, list):
			ret += parse(value)
		elif isinstance(value, dict):
			ret += parse(value)
		elif isinstance(value, int):
			ret += value
		elif isinstance(value, str):
			if isinstance(items, dict) and value == "red":
				return 0
		else:
			raise TypeError("ERROR")
	# return the sum of all numbers
	return ret
	
ret2 = parse( json.loads(raw_json) )

# print the solution
print("Solution: ", ret1, ret2)
# 156366 96852

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))