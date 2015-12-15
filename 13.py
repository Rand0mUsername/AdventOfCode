# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 13

import sys
import re
import time
import itertools

# calculating execution time
start_time = time.time()

# fake infinity
INF = 1 << 30

# undirected edges
edges = [ [ 0 for x in range(8)] for x in range(8) ]

# IO
in_file = open("13.in")
lines = in_file.readlines()

# process lines and calculate edges
it = 0
for i in range(0, 8):
	for j in range(0, 8):
		if i != j: 
			val = int(lines[it].split()[3])
			# negative edge
			if lines[it].split()[2] == 'lose':
				val *= -1
			edges[i][j] += val
			edges[j][i] += val
			it += 1

ret1 = ret2 = -INF
# try all permutations
for perm in itertools.permutations(range(0, 8)):
	curr = 0
	for i in range(0, 8):
		# for part A we sum all the edges
		curr += edges[ perm[i] ][ perm[(i+1)%8] ]
		# for part B we skip one pair of neighbours
		for skp in range(0, 8):
			ret2 = max(curr - edges[ perm[i] ][ perm[(i+1)%8] ], ret2)
	ret1 = max(curr, ret1)

# print the solution
print("Solution: ", ret1, ret2)
# 709 668

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))