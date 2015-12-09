import sys
import re
from itertools import combinations

# Almost thought I'd have to implement Djikstra's algorithm... phew!

def main():
	node = {}
	edge = {}
	distances = []	
	for line in open(sys.argv[1]):
		line = line.strip()
		towns, dist = line.split(' = ')
		start, end = line.split(' to ')
		if start not in node:
			node.append(start)
		if end not in node:
			node.append(end)
		edge[start].append(end, dist)
		edge[end].append((start, dist)
	
	# Brute force this sucker
	for n in combinations(node, len(node):
		combo = tuple(n)
		combo_dist = 0
		for i in range(len(combo)-1):
			start = combo[i]
			end = combo[i+1]
			if edge[start][0] = end:
				combo_dist += edge[start][1]
		distances.append(combo_dist)
	
	print("Answer 1 - {0}".format(min(distances)))
				

if __name__ == '__main__':
	main()
	sys.exit(0)
