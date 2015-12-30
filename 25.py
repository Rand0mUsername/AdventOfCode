# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 25

import sys
import re
import time
from functools import reduce
import itertools
from operator import mul
from collections import namedtuple

# calculating execution time
start_time = time.time()

# ret values
ret1 = ret2 = 0

# get the next code
def get_next(code):
	return (code * 252533) % 33554393

# get the code at coords (qi, qj)
def get_code(qi, qj):
	# initial value
	val = 20151125
	# we need codes[3010][3019], where codes is the matrix described in the problem statement
	# in order to make iterating easier we will use a new matrix codes_new[][] where:
	# codes_new[i+j][j] = codes[i][j] (so the first code goes in codes_new[2][1] and we need codes_new[6029][3019])
	# now we can iterate easily:
	for i in range(3, qi+qj+1):
		for j in range(1, i):
			val = get_next(val)
			if i == qi+qj and j == qj:
				return val
	return -1

ret1 = get_code(3010, 3019) 

# print the solution
print("Solution: ", ret1, ret2)
# 170 247

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))