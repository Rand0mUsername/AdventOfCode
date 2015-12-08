# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 2

import sys
import re
import time

# calculating execution time
start_time = time.time()

# variables
P = R = 0

# IO
in_file = open("2.in")
lines = in_file.readlines()
for line in lines:
	# extract data and calculated according to formulae
	a, b, c = map(int, re.split('x', line.strip()))
	P += 2*(a*b+b*c+c*a) + min(min(a*b,b*c), c*a)
	R += a*b*c + 2 * min(min(a+b,b+c), c+a)

# print the solution
print("Solution: ", P, R)
# 1588178 3783758

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))