import sys
import re
from itertools import permutations
from collections import defaultdict

def main():
	happiness = []
	guests = defaultdict(list)
	# Read in data and set up dict
	for input in open(sys.argv[1], 'r'):
		input = input.strip()
		names = re.findall('[A-Z]{1}[a-z]+', input)
		digit = re.findall('\d+', input)
		digit = digit[0]
		if 'gain' in input:
			guests[names[0]].append((names[1], int(digit)))
		else:
			guests[names[0]].append((names[1], -int(digit)))  
		
	# This little snippet is for Answer 2 (adding myself - 0 happiness towards all others)
	guest_list =  guests.keys()
	happiness_list = []
	for g in guest_list:
		happiness_list.append((g, 0))
	guests['Me'] = happiness_list

	for n in permutations(guests.keys(), len(guests.keys())):
		# Thought about using itertools.cycle but we only need to repeat the original person
		n = list(n)
		n.append(n[0])
		# This is a repeat of my loop at the end of 12_9.py
		h = 0
		for i in range(len(n)-1):
			guestA = n[i]
			guestB = n[i+1]
			# Both guests have different happiness levels towards the other
			for g in guests[guestA]:
				if g[0] == guestB:
					h += g[1]
			for g2 in guests[guestB]:
				if g2[0] == guestA:
					h += g2[1]
		happiness.append(h)

	#print("Answer 1 - {}".format(max(happiness)))
	print("Answer 2 - {}".format(max(happiness)))

if __name__ == '__main__':
	main()
	sys.exit(0)