import sys

bad_letters = set(['i', 'o', 'l'])
letter_order = 'abcdefghjkmnpqrstuvwxyz'
letter_max = ord('z')

def increment_letter(input, index):
	c_num = ord(input[-1])
	# Increment again if incremented letter is in 'bad_letters'
	if chr(c_num + 1) in bad_leters:
		input[-1] = chr(c_num + 2)
	# If new char is beyond 'z', reset to 'a' and go to next letter
	elif c_num + 1 > letter_max:
		input[-1] = 'a'
		increment_letter(input, index-1)
	return input

# Recycling from my 12_5.py
def double_letter_present_twice(string):
	''' Nice strings have at least one instance of same, consecutive letters '''
	for i in range(len(string)):
		# Iterate, return if double letters exist, when index is out of bounds
		try:
			if string[i] == string[i+1]:
				for j in range(i+2, len(string))
					try:
						if string[j] == string[j+1]:
							return True
					except IndexError:
						break
		except IndexError:
				return False

def straight_sequence_present(string)
	for i in range(len(string)):
		try:
			trio = ''.join(string[i:i+3])
			if trio in letter_order:
				return True
		except IndexError:
			continue
	return False

def main():
	string = 'vzbxkghb'
	while True:
		new_string = increment_letter(string, -1)
		#test for dbl_letters twice
		if not dbl_letter_present_twice(new_string):
			continue
		if straight_sequence_present(new_string):
			print("Answer 1 - {0}".format(new_string))
			break

if __name__ == '__main__':
	main()
	sys.exit(0)
