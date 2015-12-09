# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 8

import sys
import re
import time

# calculating execution time
start_time = time.time()

# vars
codeChars = 0
memChars = 0
ret2 = 0

# IO
in_file = open("8.in")
lines = in_file.readlines()

# process lines
for line in lines:
	line = line.strip()
	# raw length
	codeChars += len(line)
	# evaluate the string as a python expression
	memChars += len(eval(line))
	# \ and " add an additional character + 2 surrounding quotes
	ret2 += line.count('\\') + line.count('"') + 2

# A: calculate the difference
ret1 = codeChars - memChars

# print the solution
print("Solution: ", ret1, ret2)
# 1333 2046

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))