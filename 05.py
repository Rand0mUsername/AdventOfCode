# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 5

import sys
import re
import time

# calculating execution time
start_time = time.time()

# regex for part A
double = re.compile(r"(\w)\1") # should match
banned = re.compile(r"ab|cd|pq|xy") # should not match
vowel = re.compile(r"[aeiou]") # len() should be at least 3

# regex for part B
twice = re.compile(r"(\w\w).*\1") # should match
three = re.compile(r"(\w)\w\1") # should match

# return variables
ret1 = ret2 = 0

# IO
in_file = open("5.in")
lines = in_file.readlines()

# process data
for line in lines:
	s = line.strip()
	# part A
	if len(vowel.findall(s)) >= 3 and double.search(s) and not banned.search(s):
		ret1 += 1
	# part B
	if twice.search(s) and three.search(s):
		ret2 += 1

# print the solution
print("Solution: ", ret1, ret2)
# 236 51

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))