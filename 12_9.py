import sys
import re
from itertools import permutations

# Almost thought I'd have to implement Djikstra's algorithm... phew!

def main():
	node = []
	edge = {}
	distances = []	
	for line in open(sys.argv[1]):
		line = line.strip()
		places, dist = line.split(' = ')
		start, end = places.split(' to ')
		if start not in node:
			node.append(start)
			edge[start] = []
		if end not in node:
			node.append(end)
			edge[end] = []
		edge[start].append((end, int(dist) ))
		edge[end].append((start, int(dist) ))
		#Alternative, shorter way to init dict or set it...
		#edge.setdefault(start, dict())[end] = int(dist)
	
	# Brute force this sucker
	for n in permutations(node, len(node)):
		combo_dist = 0
		for i in range(len(n)-1):
			start = n[i]
			end = n[i+1]
			# Increment distance for the order of this permutation
			for e in edge[start]:
				if e[0] == end:
					combo_dist += e[1]
		distances.append(combo_dist)
	
	print("Answer 1 - {0}".format(min(distances)))
	print("Answer 2 - {0}".format(max(distances)))			

if __name__ == '__main__':
	main()
	sys.exit(0)
