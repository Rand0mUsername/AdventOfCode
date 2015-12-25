# RandomUsername (Nikola Jovanovic)
# AdventOfCode
# Day 23

import sys
import re
import time
import itertools
from collections import namedtuple
# calculating execution time
start_time = time.time()

# IO
in_file = open("23.in")

# ret values
ret1 = ret2 = 0

# we will store our program in this array of named tuples
Instruction = namedtuple('Instruction', 'op arg0 arg1')
program = []
# registers
reg = dict()

# evaluate a single instruction
def do_inst(PC):
	# fetch the instruction
	inst = program[PC]
	# hlf r sets register r to half its current value, then continues with the next instruction
	if inst.op == "hlf":
		reg[inst.arg0] //= 2
		PC += 1
	# tpl r sets register r to triple its current value, then continues with the next instruction
	elif inst.op == "tpl":
		reg[inst.arg0] *= 3
		PC += 1
	# inc r increments register r, adding 1 to it, then continues with the next instruction	
	elif inst.op == "inc":
		reg[inst.arg0] += 1
		PC += 1
	# jmp offset is a jump; it continues with the instruction offset away relative to itself
	elif inst.op == "jmp":
		PC += int(inst.arg0)
	# jie r, offset is like jmp, but only jumps if register r is even ("jump if even")
	elif inst.op == "jie":
		if not reg[inst.arg0] & 1:
			PC += int(inst.arg1)
		else:
			PC += 1
	# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd)
	elif inst.op == "jio":
		if reg[inst.arg0] == 1:
			PC += int(inst.arg1)
		else:
			PC += 1
	# this should never happen
	else:
		print("ERROR")
		exit(0)
	# return the new program counter
	return PC

# run the program with initial register values a and b
def run_program(a, b):
	# set the initial values
	reg['a'] = a 
	reg['b'] = b
	PC = 0
	# run
	while PC < program_size:
		PC = do_inst(PC)
	# return register values
	return reg['a'], reg['b']

# parse  the input
lines = in_file.readlines()
for line in lines:
	line = list(filter(bool, re.split(r'[\s,]', line.strip())))
	if len(line) == 2:
		line.append('0')
	program.append( Instruction(line[0], line[1], line[2]) )

# save the program size
program_size = len(program) 

# evaluate

# part A
a, b = run_program(0, 0)
ret1 = b
# part B
a, b = run_program(1, 0)
ret2 = b

# print the solution
print("Solution: ", ret1, ret2)
# 170 247

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))