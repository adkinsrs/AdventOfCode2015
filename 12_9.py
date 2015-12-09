import sys
import re

def main():
	node = {}
	edge = {}
	min_dist = 0
	for line in open(sys.argv[1]):
		line = line.strip()
		towns, dist = line.split(' = ')
		start, end = line.split(' to ')
		# Initialize min_distances
		if not node[start]:
			node[start] = min_dist
		if not node[end]:
			node[end] = min_dist
		edge[start].append(end, dist)
		edge[end].append((start, dist)

	

if __name__ == '__main__':
	main()
	sys.exit(0)