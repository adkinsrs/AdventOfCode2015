import sys

vowels = 'aeiou'
bad_combos = set(['ab', 'cd', 'pq', 'xy'])

def at_least_three_vowels(string):
	''' Nice strings have at least 3 vowels '''
	count = 0
	count = sum(string.count(v) for v in vowels)
	if count >=3:
		return True
	else:
		return False

def double_letter_present(string):
	''' Nice strings have at least one instance of same, consecutive letters '''
	for i in range(len(string)):
		# Iterate, return if double letters exist, when index is out of bounds
		try:
			if string[i] == string[i+1]:
				return True
		except IndexError:
				return False

def bad_combos_present(string):
	''' Nice strings do not have any pattern from the bad_combo hash above '''
	for i in bad_combos:
		if i in string:
			return False
	return True

def twice_occuring_dbls_present(string):
	''' Nice strings have a pair appear again later in the string (no overlaps) '''
	for i in range(len(string)):
		try:
			pair = ''.join(string[i:i+2])
			if pair in string[i+2:]:
				return True
		except IndexError:
			continue
	return False

def sandwiched_letter_present(string):
	''' Nice strings must a letter sandwiched by 2 letters '''
	for i in range(len(string)):
		sandwich = string[i]
		try:
			if string[i+2] == sandwich:
				return True
		except IndexError:
			continue
	return False

def main():
	nice_str1 = 0
	nice_str2 = 0
	file = sys.argv[1]
	for line in open(file,'r'):
		line = line.strip()
		
		answer1_list = [at_least_three_vowels(line), double_letter_present(line), bad_combos_present(line)]
		for cmd in answer1_list:
			if not cmd:
				break
		else:
			nice_str1 += 1
		
		answer2_list = [twice_occuring_dbls_present(line), sandwiched_letter_present(line)] 
		for cmd in answer2_list:
			if not cmd:
				break
		else:	# Execute after successful for-loop run
			nice_str2 += 1

	print("Answer 1 - {0}".format(str(nice_str1)))
	print("Answer 2 - {0}".format(str(nice_str2)))

if __name__ == '__main__':
	main()
	sys.exit(0)
