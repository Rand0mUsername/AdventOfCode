# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 11

import sys
import re
import time

# calculating execution time
start_time = time.time()

# input
pwd = "vzbxkghb"
pwd2 = "vzbxxyzz"

# regex
threes = re.compile(r"(?=(\w\w\w))") # divide into segments of 3
banned = re.compile(r"[iol]") # should not match
twopairs = re.compile(r"(\w)\1.*(\w)\2") # should match

# string increment
def inc(s):
	ret = []
	cpy = False
	for c in reversed(s):
		if cpy:
			ret.append(c)
		elif c == 'z':
			ret.append('a')
		else:
			ret.append(chr(ord(c) + 1))
			cpy = True
	return "".join(ret)[::-1]


# check if a 3 char sequence is increasing
def testInc3(l):
	if ord(l[1]) - ord(l[0]) == 1 and ord(l[2]) - ord(l[1]) == 1:
		return True
	else:
		return False

# check if the string is valid
def valid(s):
	#print(type(s))
	if twopairs.search(s) and not banned.search(s) and True in list(map(testInc3, threes.findall(s))):
		return True
	else:
		return False

# find first valid password
vals = 0
ret = []
while vals < 2:
	if valid(pwd):
		ret.append(pwd)
		vals += 1 
	pwd = inc(pwd)

# print the solution
print("Solution: ", ret[0], ret[1])
# vzbxxyzz vzcaabcc

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))