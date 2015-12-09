# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 9

import sys
import re
import time

# calculating execution time
start_time = time.time()

# fake infinity
INF = 1 << 30
# 8 cities in total in my input file, 1<<8 bitmasks
# DP[MASK][last][task] = best way to visit all cities that
# correspond to set bits in MASK and end up in 'last'
# task = 0: challenge part A, task = 1: challenge part B
DP = [ [ [INF, 0] for x in range(8)] for x in range(1 << 8) ]

# IO
in_file = open("9.in")
lines = in_file.readlines()

# process lines and calculate base distances
it = 0
for i in range(0, 8):
	for j in range(i+1, 8):
		MASK = (1<<i) + (1<<j)
		DP[MASK][i][0] = DP[MASK][j][0] = int(lines[it].split()[4])
		DP[MASK][i][1] = DP[MASK][j][1] = int(lines[it].split()[4])
		it += 1

# the number of masks
MASKS = 1 << 8
# iterate over the number of set bits
for i in range(3, 9): 
	for MASK in range(0, MASKS): 
		if bin(MASK).count("1") == i: 
			# process all bitmasks with i set bits
			# remove 'bit'
			for bit in range(0, 8):
				if MASK & (1 << bit):
					nMASK = MASK - (1 << bit)
					for nBit in range(0, 8):
						if nMASK & (1 << nBit):
						# make a nBit -> bit transition and update DP[MASK][bit]
							newDist = DP[nMASK][nBit][0] + DP[(1<<bit) + (1<<nBit)][bit][0]
							DP[MASK][bit][0] = min(newDist, DP[MASK][bit][0])
							newDist = DP[nMASK][nBit][1] + DP[(1<<bit) + (1<<nBit)][bit][1]
							DP[MASK][bit][1] = max(newDist, DP[MASK][bit][1])


# find the answer, best among DP[MASKS-1][]
ret = [INF, 0]
for lst in range(0, 8):
	ret[0] = min(DP[MASKS- 1][lst][0], ret[0])
	ret[1] = max(DP[MASKS - 1][lst][1], ret[1])

# print the solution
print("Solution: ", ret[0], ret[1])
# 141 736

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))