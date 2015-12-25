# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 17

import sys
import re
import time
import itertools

# calculating execution time
start_time = time.time()

# IO
in_file = open("17.in")

# vars
INF = 1000*1000*1000
sizes = []
ret1 = ret2 = 0
# DP[i][j] = achieve j liters using first i containers
DP = [[0 for x in range(155)] for x in range(25)] 
# DP2[i][j] = achieve j liters using first i containers 
# (min number of containers, number of ways)
DP2 = [[(INF, 0) for x in range(155)] for x in range(25)] 

# Honestly, I expected more from AoC. This is Day 17 and I can 
# still bruteforce. I did DP because I'm tired of bruteforcing,
# but I honestly thought that there will be some real challenges here.

# process input
lines = in_file.readlines()
for line in lines:
	sizes.append(int(line))

# do DP
DP[0][0] = 1
for i in range(1, 21):
	DP[i][0] = 1
	for j in range(1, 151):
		# without container i
		DP[i][j] = DP[i-1][j]
		# with container i
		if sizes[i-1] <= j:
			DP[i][j] += DP[i-1][j - sizes[i-1]]
# do DP2
DP2[0][0] = (0, 1)
for i in range(1, 21):
	DP2[i][0] = (0, 1)
	for j in range(1, 151):
		# without container i
		DP2[i][j] = DP2[i-1][j]
		# with container i
		if sizes[i-1] <= j:
			src = DP2[i-1][j - sizes[i-1]]
			# less containers
			if src[0] + 1 < DP2[i][j][0]:
				DP2[i][j] = (src[0] + 1, src[1])
			# same number of containers
			elif src[0] + 1 == DP2[i][j][0]:
				DP2[i][j] = (src[0] + 1, DP2[i][j][1] + src[1])

# print the solution
ret1 = DP[20][150]
ret2 = DP2[20][150][1]
print("Solution: ", ret1, ret2)
# 654 57

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))