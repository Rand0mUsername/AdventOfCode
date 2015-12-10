# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 10

import sys
import re
import time

# calculating execution time
start_time = time.time()

# my puzzle input
s = "1321131112"

# i felt like doing a one liner
def transform(s):
	return "".join(map(lambda tpl: str(len(tpl[0])) + tpl[1], re.findall(r"(([0-9])\2*)", s)))

# repeat the transformation 40 times for part A, and 50 times for part B
for i in range(50):
	s = transform(s)
	if i == 39:
		ret1 = len(s)
ret2 = len(s)

# print the solution
print("Solution: ", ret1, ret2)
# 492982 6989950

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))