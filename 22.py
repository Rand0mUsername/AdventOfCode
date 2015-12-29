# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 22

import sys
import re
import time
import itertools
import math
import random
from collections import namedtuple

# calculating execution time
start_time = time.time()

# fake infinity
INF = 1000*1000*1000

# mana costs and spell list
costs = dict()
costs["missile"] = 53
costs["drain"] = 73
costs["shield"] = 113
costs["poison"] = 173
costs["recharge"] = 229
spells = ["missile", "drain", "shield", "poison", "recharge"]

# apply spell effects at the start of each turn
def apply_effects(data, timers):
	# shield
	if timers['shield'] > 0:
		timers['shield'] -= 1
		data['p_ar'] = 7
	else:
		data['p_ar'] = 0
	# poison
	if timers['poison'] > 0:
		timers['poison'] -= 1
		data['e_hp'] -= 3
	# recharge
	if timers['recharge'] > 0:
		timers['recharge'] -= 1
		data['p_mp'] += 101

# play the game in game mode 'mode' with starting parameters from 'data'
def play_game(data, mode):
	# initialization
	timers = {'shield' : 0, 'poison' : 0, 'recharge' : 0}
	mana_spent = 0
	spell_sequence = []

	# game can be an endless loop since it always ends pretty quickly
	while True:
		# -- player turn begins --

		# if the mode is hard lose one random hp
		if mode == "Hard":
			data['p_hp'] -= 1
			if data['p_hp'] <= 0:
				return INF, spell_sequence
		# apply effects
		apply_effects(data, timers)
		# find castable spells, if there are none you lost
		castable_spells = [spell for spell in spells if costs[spell] <= data['p_mp'] and (not spell in timers or timers[spell] == 0)]
		if len(castable_spells) == 0:
			return INF, spell_sequence
		# select a random spell
		curr_spell = random.choice( castable_spells )
		spell_sequence.append(curr_spell)
		mana_spent += costs[curr_spell]
		data['p_mp'] -= costs[curr_spell]
		# cast the chosen spell
		if curr_spell == 'missile':
			data['e_hp'] -= 4
		elif curr_spell == 'drain':
			data['e_hp'] -= 2
			data['p_hp'] += 2
		elif curr_spell == 'shield':
			timers['shield'] = 6
		elif curr_spell == 'poison':
			timers['poison'] = 6
		elif curr_spell == 'recharge':
			timers['recharge'] = 5
		else:
			print("error")
			exit(0)
		# check if the enemy died
		if data['e_hp'] <= 0:
			return mana_spent, spell_sequence

		# -- enemy turn begins -- 

		# apply effects
		apply_effects(data, timers)
		# attack
		data['p_hp'] -= max(1, data['e_dmg'] - data['p_ar'])
		# check if the player died
		if data['p_hp'] <= 0:
			return INF, spell_sequence

# play a lot of random games and hope you played the right game
def monte_carlo(mode, data):
	least_mana = INF 
	best_spells = []
	# 20k = magical number of iterations found by trial and error
	for x in range(20000):
		# play the game
		curr_mana, curr_spells = play_game(dict(data), mode)
		# update the best game
		if curr_mana < least_mana:
			least_mana = curr_mana
			best_spells = curr_spells
	# print the result since it's probably interesting and return the value
	print(best_spells)
	return least_mana

# main
data = {'p_hp' : 50, 'p_mp' : 500, 'p_ar' : 0, 'e_hp' : 55, 'e_dmg' : 8, 'e_ar' : 0}
ret1 = monte_carlo("Easy", data)
ret2 = monte_carlo("Hard", data)

# print the solution
print("Solution: ", ret1, ret2)
# 953 1289

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))