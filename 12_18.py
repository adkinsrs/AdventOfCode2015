import sys

# This is the Conway's Game of Life simulation

def main():
	steps = sys.argv[2]
	for line in open(sys.argv[1], 'r'):
		line = line.strip()

if __name__ == '__main__':
	main()
	sys.exit(0)