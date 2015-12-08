# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 1

import sys
import re
import time

# calculating execution time
start_time = time.time()

# variables
balance = 0
firstUnder = -1
it = 1

# IO
in_file = open("1.in")
line = in_file.readline().strip()

# process data
for ch in line:
	if ch == '(':
		balance += 1
	elif ch == ')':
		balance -= 1
	# first time we went under
	if balance < 0 and firstUnder == -1:
		firstUnder = it 
	it += 1

# print the solution
print("Solution: ", balance, firstUnder)
# 74 1795

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))