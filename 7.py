# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 7

import sys
import re
import time
import queue

# calculating execution time
start_time = time.time()

# IO
in_file = open("7.in")
lines = in_file.readlines()

# Possible data stucture approaches:
# 1. Use four dictionaries for edges, indegree, values, and production rules
# 2. Create a class Node and use one dictionary which maps id to an index in a list of nodes
# I decided to use 1, what's good practice?

# vars
identifier = re.compile(r"^[a-z]*$") 
edges = dict()
indeg = dict()
vals = dict()
production = dict()
ret1 = ret2 = 0

# get a value of a wire or just extract raw numerical value
def getVal(token):
	if identifier.search(token):
		return vals[token] # wire
	else:
		return int(token) # numeric value

# calculate a value of a wire
def calcValue(key, part):
	# prod can be: x OR y, x AND y, x RSHIFT y, x LSHIFT y, NOT x, x
	prod = production[key]
	plen = len(prod)
	# for part B we add a -> b
	if key == 'b' and part == 'B':
		vals[key] = ret1
	# hotwired value
	elif plen == 1:
		vals[key] = getVal(prod[0])
	# not
	elif plen == 2:
		vals[key] = ~getVal(prod[1])
	# other binary operations
	elif prod[1] == 'OR':
		vals[key] = getVal(prod[0]) | getVal(prod[2])
	elif prod[1] == 'AND':
		vals[key] = getVal(prod[0]) & getVal(prod[2])
	elif prod[1] == 'RSHIFT':
		vals[key] = getVal(prod[0]) >> getVal(prod[2])
	elif prod[1] == 'LSHIFT':
		vals[key] = getVal(prod[0]) << getVal(prod[2])
	# 16 bit numbers, truncate (still works without this line though, no idea how)
	vals[key] &= 0xFFFF

# topological sorting
def toposort(part):
	# init queue
	q = queue.Queue()

	# find nodes with indegree zero
	for key, value in indeg.items():
		if value == 0:
			q.put(key)

    # loop
	while q.qsize():
		# get current node and calculate the value
		curr = q.get()
		calcValue(curr, part)
		# add new nodes
		if curr in edges:
			for v in edges[curr]:
				indeg[v] -= 1
				if indeg[v] == 0:
					q.put(v)

# calculate all the values
def solve(part):
	# init
	edges.clear(); indeg.clear(); vals.clear(); production.clear()
	# process lines
	for line in lines:
		tokens = line.split()
		# a target wire, set its indegree and production rule
		target = tokens[len(tokens) - 1]
		indeg[target] = 0
		production[target] = tokens[0:len(tokens)-2] 
		# find identifiers 
		for token in tokens:
			if token != target and identifier.search(token):
				# for each identifier found, add a corresponding edge
				if not token in edges:
					edges[token] = []
				edges[token].append(target)
				indeg[target] += 1

    # do a topological sorting
	toposort(part)

	return vals['a']

# solve both parts
ret1 = solve('A') # b is 1674
ret2 = solve('B') # b is ret1

# print the solution
print("Solution: ", ret1, ret2)
# 46065 14134

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))