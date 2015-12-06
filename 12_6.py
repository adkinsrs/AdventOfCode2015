import sys
import re

# 2D array set to off (False)
grid = [[0 for y in range(1000)] for x in range(1000)]

def reset_grid():
	global grid	# Lets python know I want to edit the global var
	grid = [[0 for y in range(1000)] for x in range(1000)]
	return	

# Answer 1 functions

def turn_off(x1, y1, x2, y2):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			grid[i][j] = 0
	return

def turn_on(x1, y1, x2, y2):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			grid[i][j] = 1
	return

def toggle(x1, y1, x2, y2):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			if grid[i][j] == 1:
				grid[i][j] = 0
			else:
				grid[i][j] = 1
	return

def count_grid_lights():
	return sum(i.count(1) for i in grid)
	
# Answer 2 functions

def new_turn_off(x1, y1, x2, y2):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			grid[i][j] += -1
			if grid[i][j] < 0:
				grid[i][j] = 0
	return

def new_turn_on(x1, y1, x2, y2):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			grid[i][j] += 1
	return

def new_toggle(x1, y1, x2, y2):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			grid[i][j] += 2
	return

def total_brightness():
	return sum(sum(i) for i in grid)

# Main

def main():
	turn_on(0,0,999,999)
	print("test 1 - {0} - should be 1000000".format(count_grid_lights()))
	toggle(0,0,999,0)
	print("test 2 - {0} - should be 999000".format(count_grid_lights()))
	turn_off(499,499,500,500)
	print("test 3 - {0} - should be 998996".format(count_grid_lights()))
	reset_grid()
	print("test 4 - {0} - should be 0".format(count_grid_lights()))	

	# Alternative could have done re.findAll on the specific parts, which are stored in a list
	pattern = re.compile(r"(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)")
	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		test = pattern.search(line)
		x1 = int(test.group(2))
		y1 = int(test.group(3))
		x2 = int(test.group(4))
		y2 = int(test.group(5))
		if test.group(1) == 'on':
			turn_on(x1, y1, x2, y2)
		elif test.group(1) == 'off':
			turn_off(x1, y1, x2, y2)
		elif test.group(1) == 'toggle':
			toggle(x1, y1, x2, y2)
		else:
			print("Weird line input - ", line)
					
	print("Answer 1 - {0}".format(count_grid_lights()))
	reset_grid()

	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		test = pattern.search(line)
		x1 = int(test.group(2))
		y1 = int(test.group(3))
		x2 = int(test.group(4))
		y2 = int(test.group(5))
		if test.group(1) == 'on':
			new_turn_on(x1, y1, x2, y2)
		elif test.group(1) == 'off':
			new_turn_off(x1, y1, x2, y2)
		elif test.group(1) == 'toggle':
			new_toggle(x1, y1, x2, y2)
		else:
			print("Weird line input - ", line)

	print("Answer 2 - {0}".format(total_brightness()))

if __name__ == '__main__':
	main()
	sys.exit(0)
