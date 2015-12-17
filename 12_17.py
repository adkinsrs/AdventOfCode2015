import sys
from itertools import chain
from itertools import combinations

LITERS = 150

 #Got this from the Python itertools page
def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def main():
	jar_combos = 0
	jars = [int(line.strip()) for line in open(sys.argv[1], 'r')]
	min_length = len(jars)
	for i in powerset(jars):
		if sum(i) == LITERS:
			jar_combos += 1
			if len(i) < min_length:
				min_length = len(i)
				min_jar_combos = 1
			elif len(i) == min_length:
				min_jar_combos += 1

	print("Answer 1 - {}".format(jar_combos))
	print("Answer 2 - {}".format(min_jar_combos))

if __name__ == '__main__':
	main()
	sys.exit(0)
