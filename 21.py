# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 21

import sys
import re
import time
import itertools
import math
from collections import namedtuple

# calculating execution time
start_time = time.time()

# IO: differente
in_file = open("21.in")

# fake infinity
INF = 1000*1000*1000
# gear
Gear = namedtuple('Gear', 'cost dmg armor')
weapons = []
armor = []
rings = []
# ret vars
ret1 = INF
ret2 = 0

# calculating who wins with given parameters
def wins(p_dmg, p_armor, e_hp, e_dmg, e_armor):
	p_hp = 100
	p_dmg = max(1, p_dmg - e_armor)
	e_dmg = max(1, e_dmg - p_armor)
	# comparing the number of rounds the players will live
	if math.ceil(e_hp / p_dmg) <= math.ceil(p_hp / e_dmg):
		return True
	return False

# process input
# weapons
for i in range(5):
	line = list(map(int, in_file.readline().strip().split()[1:]))
	weapons.append(Gear(line[0], line[1], line[2]))
# armor
for i in range(5):
	line = list(map(int, in_file.readline().strip().split()[1:]))
	armor.append(Gear(line[0], line[1], line[2]))
# the easiest way to allow wearing no armor
armor.append(Gear(0, 0, 0)) 
# rings
for i in range(6):
	line = list(map(int, in_file.readline().strip().split()[1:]))
	rings.append(Gear(line[0], line[1], line[2]))
# the easiest way to allow wearing no ring
rings.append(Gear(0, 0, 0)) 
# enemy parameters
e_hp = int(in_file.readline().strip().split()[2])
e_dmg = int(in_file.readline().strip().split()[1])
e_armor = int(in_file.readline().strip().split()[1])


# try all
for w_idx in range(5):
	for a_idx in range(6):
		for r1_idx in range(7):
			for r2_idx in range(7):
				# calculate cost, dmg, armor
				curr_cost = weapons[w_idx].cost + armor[a_idx].cost + rings[r1_idx].cost + rings[r2_idx].cost
				curr_dmg = weapons[w_idx].dmg + armor[a_idx].dmg + rings[r1_idx].dmg + rings[r2_idx].dmg
				curr_armor = weapons[w_idx].armor + armor[a_idx].armor + rings[r1_idx].armor + rings[r2_idx].armor
				# check if player wins
				if wins(curr_dmg, curr_armor, e_hp, e_dmg, e_armor):
					ret1 = min(curr_cost, ret1) # part A
				else:
					ret2 = max(curr_cost, ret2) # part B

# print the solution
print("Solution: ", ret1, ret2)
# 78 148

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))