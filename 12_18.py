import sys
from pprint import pprint

test_str = ".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.."

# This is the Conway's Game of Life simulation

def main():
	current_grid = []
	steps = int(sys.argv[2])
	#test = test_str.split('\n')
	#for line in test:
	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		current_grid.append(list(line))

	# For Answer 2, always have the corner lights on
	# Should be using len(current_grid[row]) for flexibility but I'm lazy at this point and it's a square
	current_grid[0][0] = '#'
	current_grid[0][len(current_grid)-1] = '#'
	current_grid[len(current_grid)-1][0] = '#'
	current_grid[len(current_grid)-1][len(current_grid)-1] = '#'
	
	for t in range(steps):
		# copying curr_grid to new_grid in the beginning using various methods didn't work, so sticking with this old way of initializing for each loop
		new_grid = []
		# The print looks a bit messy the using str.join for a 2D array seems daunting
		#print ("Step ", t)
		#pprint(current_grid)

		for row in range(len(current_grid)):
			new_grid.append([])
			for col in range(len(current_grid[row])):
				count = 0
				# Keep track of positions of borders
				borders = [(row-1, col-1), (row, col-1), (row+1, col-1), (row-1, col), (row+1, col), (row-1, col+1), (row, col+1), (row+1, col+1)]
				for b in borders:
					if b[0] < 0 or b[1] < 0 or b[0] == len(current_grid) or b[1] == len(current_grid[row]):
						continue
					if current_grid[ b[0] ][ b[1] ] == '#':
						count += 1
				# /for b
				if current_grid[row][col] == '.':
					if count == 3:
						new_grid[row].append('#')
					else:
						new_grid[row].append('.')
				else:
					if not ( count == 2 or count == 3):
						new_grid[row].append('.')
					else:
						new_grid[row].append('#')
			# /for col
		# /for row
		current_grid = new_grid[:]

		# For Answer 2, always have the corner lights on
		# Should be using len(current_grid[row]) for flexibility but I'm lazy at this point and it's a square
		current_grid[0][0] = '#'
		current_grid[0][len(current_grid)-1] = '#'
		current_grid[len(current_grid)-1][0] = '#'
		current_grid[len(current_grid)-1][len(current_grid)-1] = '#'

	# /for t

	#print("Step final")
	#pprint(current_grid)

	lights_on_at_end = sum(i.count('#') for i in current_grid)
	#print("Answer 1 - {}".format(lights_on_at_end))
	print("Answer 2 - {}".format(lights_on_at_end))

# /main

if __name__ == '__main__':
	main()
	sys.exit(0)