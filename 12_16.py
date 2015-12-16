import sys
import re

ticker_tape = ['children: 3', 'cats: 7', 'samoyeds: 2', 'pomeranians: 3', 'akitas: 0', 'vizslas: 0', 'goldfish: 5', 'trees: 3', 'cars: 2', 'perfumes: 1']

# Must be greater than
cats = 7
trees = 3
# Must be less than
pomeranians = 3
goldfish = 5


def main():
	for sue in open(sys.argv[1], 'r'):
		m = re.match('Sue (\d+):', sue)
		sue_num = m.group(1)
		things = re.findall('\w+: \d+', sue)
		# The nice thing is that the ticker tape matches the input, so we don't have to store as a dict
		if all(thing in ticker_tape for thing in things):			
			print("Answer 1 - {}".format(sue_num))

		for thing in things:
			digit = re.findall('\d+', thing)
			digit = int(digit[0])
			# Must have more than the ticker tape cats and trees values
			if 'cats' in thing:
				if digit <= cats:
					break
			elif 'trees' in thing:
				if digit <= trees:
					break
			# Most have less than the ticker tape pomeranian and goldfish values
			elif 'pomeranians' in thing:
				if digit >= pomeranians:
					break
			elif 'goldfish' in thing:
				if digit >= goldfish:
					break
			# Otherwise, must be in the ticker tape
			else:
				if thing not in ticker_tape:
					break
		else:
			# If we make it through the onslaught of breaks, we know that's the real Sue
			print("Answer 2 - {}".format(sue_num))
		



if __name__ == '__main__':
	main()
	sys.exit(0)