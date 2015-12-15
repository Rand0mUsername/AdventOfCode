# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 15

import sys
import re
import time
import itertools

# calculating execution time
start_time = time.time()

# IO
in_file = open("15.in")
lines = in_file.readlines()

# we have 4 ingredients so we can just straight brute force through this
# the matrix of properties
mat = [[0 for x in range(5)] for x in range(4)]

# score one distribution of quantites
def score(ts):
	ret = 1
	for j in range(4): # characteristic index, ignore calories
		curr_score = 0 
		for i in range(4): # ingredient index
			curr_score += ts[i] * mat[i][j]
		curr_score = max(0, curr_score) # clamp
		ret *= curr_score
	return ret

# check if the current distribution of quantities has 500 calories
def good_calories(ts):
	ret = 0
	for i in range(4): # ingredient index
		ret += ts[i] * mat[i][4] # calories: mat[][4] 
	return ret == 500

# assign quantities
def assign(idx, left, ts): # ingredient index, teaspoons left, array of teaspoons alloted
	ret = (0, 0) # (ret1, ret2)
	# base case
	if idx == 3:
		sc = score(ts + [left])
		return (sc, sc * good_calories(ts + [left]))
	# recurse
	for curr_ts in range(left+1):
		rec = assign(idx + 1, left - curr_ts, ts + [curr_ts])
		ret = ( max(ret[0], rec[0]), max(ret[1], rec[1]) )
	# return
	return ret

# process input
for i in range(4):
	line = lines[i].strip().split()
	# a cute example of list comprehension + slicing + regex
	mat[i] = [int(num.replace(',', '')) for num in line[2::2]]
	
# start the recursion
ret1, ret2 = assign(0, 100, [])

# print the solution
print("Solution: ", ret1, ret2)
# 222870 117936

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))