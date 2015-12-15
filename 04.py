# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 4

import sys
import re
import time
import hashlib

# calculating execution time
start_time = time.time()

# md5 hash function
def md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

# base string and result
res = ""
base = "iwrupvqb"

# part A : five zeroes
i = 0
while res[0:5] != '00000':
	i += 1
	res = md5(base + str(i))

# part B : six zeroes
j = 0
while res[0:6] != '000000':
	j += 1
	res = md5(base + str(j))

# print the solution
print("Solution: ", i, j)
# 346386 9958218

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))