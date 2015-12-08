# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 3

import sys
import re
import time

# calculating execution time
start_time = time.time()

# variables
visited = set()
i = j = 0
ri = rj = si = sj = 0
ret1 = ret2 = 0

# IO
in_file = open("3.in")
line = in_file.readline().strip()

# process data part A
visited.add( (i, j) )
for ch in line:
	if ch == '>':
		i += 1
	elif ch == '<':
		i -= 1
	elif ch == 'v':
		j += 1
	elif ch == '^':
		j -= 1
	# add update coords to set
	visited.add( (i, j) )
# count different points visited
ret1 = len(visited)

# clear the set
visited.clear()

# process data part B
visited.add( (ri, rj) )
it = 0
for ch in line:
	# update according to parity
	if ch == '>':
		si += (it & 1)
		ri += 1 - (it & 1)
	elif ch == '<':
		si -= (it & 1)
		ri -= 1 - (it & 1)
	elif ch == 'v':
		sj += (it & 1)
		rj += 1 - (it & 1)
	elif ch == '^':
		sj -= (it & 1)
		rj -= 1 - (it & 1)
	# add update coords to set
	visited.add( (si, sj) )
	visited.add( (ri, rj) )
	it += 1
# count different points visited
ret2 = len(visited)

# print the solution
print("Solution: ", ret1, ret2)
# 2592 2360

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))