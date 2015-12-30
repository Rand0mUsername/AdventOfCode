# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 24

import sys
import re
import time
from functools import reduce
import itertools
from operator import mul
from collections import namedtuple
# calculating execution time
start_time = time.time()

# IO
in_file = open("24.in")

# ret values
ret1 = ret2 = 0

# part A
def find_first(nums, part):
	package_sum = {'A' : sum(nums)//3, 'B' : sum(nums)//4}
	for group_sz in range(len(nums)):
		for pak in itertools.combinations(nums, group_sz):
			if sum(pak) == package_sum[part]:
				inner_nums = list(set(nums) - set(pak))
				for inner_sz in range(len(inner_nums)):
					for inner_pak in itertools.combinations(inner_nums, inner_sz):
						if sum(inner_pak) == package_sum[part]:
							if part == "A":
								# we found a match
								# the first match we find is a solution
								print(pak)
								return reduce(mul, pak)
							else:
								# part B has to split once more
								# I should've done this recursively though...
								wtf_nums = list(set(inner_nums) - set(inner_pak))
								for wtf_sz in range(len(wtf_nums)):
									for wtf_pak in itertools.combinations(wtf_nums, wtf_sz):
										if sum(wtf_pak) == package_sum[part]:
											# we found a match
											# the first match we find is a solution
											print(pak)
											return reduce(mul, pak)
						

# parse  the input
nums = list(map(int, in_file.readlines()))
ret1 = find_first(nums, "A")
ret2 = find_first(nums, "B")

# print the solution
print("Solution: ", ret1, ret2)
# 11846773891 80393059

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))