import sys
import re
import time

# calculating execution time
start_time = time.time()

# two matrices of lights
M1 = [[0 for x in range(1005)] for x in range(1005)] 
M2 = [[0 for x in range(1005)] for x in range(1005)] 

# IO
in_file = open("6.in")
lines = in_file.readlines()

# process lines
for line in lines:
	words = re.split(',| |l', line.strip())
	# toggle command
	if words[1] == 'e':
		for i in range(int(words[2]), int(words[5]) + 1):
			for j in range(int(words[3]), int(words[6]) + 1):
				M1[i][j] = 1 - M1[i][j]
				M2[i][j] += 2
	#turn on
	if words[1] == 'on':
		for i in range(int(words[2]), int(words[5]) + 1):
			for j in range(int(words[3]), int(words[6]) + 1):
				M1[i][j] = 1
				M2[i][j] += 1
	#turn off
	if words[1] == 'off':
		for i in range(int(words[2]), int(words[5]) + 1):
			for j in range(int(words[3]), int(words[6]) + 1):
				M1[i][j] = 0
				M2[i][j] -= 1
				M2[i][j] = max(0, M2[i][j])

# calculate the result
ret = 0
ret2 = 0
for i in range(0, 1000):
	for j in range(0, 1000):
		ret += M1[i][j]
		ret2 += M2[i][j]

# print the solution
print("Solution: ", ret, ret2)
# 400410 15343601

# execution time
print("Execution time: %.2f seconds" % (time.time() - start_time))