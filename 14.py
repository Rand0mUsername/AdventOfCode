# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 14

import sys
import re
import time
import itertools

# just now I googled "python naming convention"
# and realized it involves_underscores and doesn't recommend camelCase
# :(

# calculating execution time
start_time = time.time()

# IO
in_file = open("14.in")
lines = in_file.readlines()

# total time and ret vars
T = 2503
ret1 = 0

# 'reindeer' is a long word, they're just dogs
dogs = []

# calc where the dog is after T seconds
def dog_position(dog_idx, seconds):
	# unpack data
	speed, moving, resting = dogs[dog_idx]
	cycle_len = moving + resting
	# calculate position
	ret = speed * moving * (seconds // cycle_len) #full cycles
	ret += speed * min(seconds % cycle_len, moving) #last cycle
	return ret

# we have 9 dogs, get their data
for it in range(9):
	line = lines[it].strip().split()
	dogs.append( (int(line[3]), int(line[6]), int(line[13])) )

# part A: only the last second
for it in range(9):
	ret1 = max(ret1, dog_position(it, T))

# part B: full simulation
# we will reuse our dog_position function instead of calculating what
# happens in each second since we don't really lose efficiency
ret2 = 0
points = [0 for x in range(9)]
# simulation
for seconds in range(1, T+1):
	best_dogs = (-1, [-1]) # distance, [dog indices]
	for it in range(9):
		# calculate this dog's position and update best_dogs
		pos = dog_position(it, seconds)
		if pos > best_dogs[0]:
			best_dogs = (pos, [it])
		elif pos == best_dogs[0]:
			best_dogs = (pos, best_dogs[1] + [it])
	# award points
	for it in best_dogs[1]:
		points[it] += 1

# find the dog who has the most points
for it in range(9):
	ret2 = max(points[it], ret2)

# print the solution
print("Solution: ", ret1, ret2)
# 2660 1256

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))