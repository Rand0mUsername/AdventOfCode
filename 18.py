# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 18

import sys
import re
import time
import itertools

# calculating execution time
start_time = time.time()

# IO
in_file = open("18.in")

# vars
ret1 = ret2 = 0
# grids for two parts
grid = [ ['/' for x in range(100)] for x in range(100) ]
grid2 = [ ['/' for x in range(100)] for x in range(100) ]
# lists that are used to generate neighbours
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
# corners of the matrix
corners = [(0, 99), (99, 0), (0, 0), (99, 99)]

# check if a pair of indices lies inside the matrix
def valid(i, j):
	if i >= 0 and j >= 0 and i < 100 and j < 100:
		return True
	return False

# do a single CGOL transformation
def get_new(grid, skip):
	# return list
	ret = [ ['/' for x in range(100)] for x in range(100) ]
	for i in range(100):
		for j in range(100):
			# corners are treated differently in part B
			if skip and (i, j) in corners:
				ret[i][j] = '#'
			else:
				# count neighbours that are on
				adj_on = 0
				for k in range(8):
					if valid(i + di[k], j + dj[k]) and grid[ i+di[k] ][ j+dj[k] ] == '#':
						adj_on += 1
				# transformation rules
				if grid[i][j] == '#' and (adj_on == 2 or adj_on == 3):
					ret[i][j] = '#'
				elif grid[i][j] == '.' and adj_on == 3:
					ret[i][j] = '#'
				else:
					ret[i][j] = '.'
	return ret

def cnt_on(grid):
	# count the number of lights that are on
	ret = 0
	for i in range(100):
		for j in range(100):
			if grid[i][j] == '#':
				ret += 1
	return ret

# process input
grid2[0][0] = '$'
lines = in_file.readlines()
for i in range(100):
	grid[i] = lines[i].strip()
	# for part B: put '#'s in corners
	if i == 0 or i == 99:
		grid2[i] = '#' + grid[i][1:99] + '#'
	else:
		grid2[i] = grid[i]

# transform 100 times
for it in range(100):
	grid = get_new(grid, False)
	grid2 = get_new(grid2, True)

# fetch and print the output
ret1 = cnt_on(grid)
ret2 = cnt_on(grid2)
print("Solution: ", ret1, ret2)
# 821 886

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))