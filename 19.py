# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 19

import sys
import re
import time
import itertools

# calculating execution time
start_time = time.time()

# IO
in_file = open("19.in")

# vars
ret1 = ret2 = 0
rules = []
created = set()

# process input
lines = in_file.readlines()
for i in range(43):
	tokens = lines[i].strip().split()
	rules.append( (tokens[0], tokens[2]) )
s = lines[43].strip()
slen = len(s)

# part A: try all possible replacements and count them
for i in range(43):
	for j in range(slen):
		if s[j:j + len(rules[i][0])] == rules[i][0]:
			created.add(s[:j] + rules[i][1] + s[j + len(rules[i][0]):])
ret1 = len(created)

# part B: 
# was pretty stumped here, tbh

# it can be proven that the number of steps will always be the same
# the only thing we have to do is to somehow parse the input string
# and count the number of production rules used
# 1. X => XX (X is not Rn, Y, or Ar)
# 2. X => X Rn X Ar | X Rn X Y X Ar | X Rn X Y X Y X Ar
ret2 = len(re.findall(r"[A-Z]", s)) - 1 - s.count("Rn") - s.count("Ar") - 2 * s.count("Y")

# TODO: CYK

# fetch and print the output
print("Solution: ", ret1, ret2)
# 0 0

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))