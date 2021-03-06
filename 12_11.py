import sys

bad_letters = set(['i', 'o', 'l'])
letter_order = 'abcdefghjkmnpqrstuvwxyz'
letter_max = ord('z')

def create_new_password(new_string):
	while True:
		new_string = increment_letter(new_string, -1)
		#test for dbl_letters twice
		if not dbl_letter_present_twice(new_string):
			continue
		if straight_sequence_present(new_string):
			return new_string

def increment_letter(input, index):
	# Strings are immutable so convert to list first.
	input_list = list(input)
	c_num = ord(input_list[index])
	# Increment again if incremented letter is in 'bad_letters'
	if chr(c_num + 1) in bad_letters:
		input_list[index] = chr(c_num + 2)
		input = ''.join(input_list)
	# If new char is beyond 'z', reset to 'a' and go to next letter
	elif c_num + 1 > letter_max:
		input_list[index] =  'a'
		input = ''.join(input_list)
		input = increment_letter(input, index-1)
	else:
		input_list[index] = chr(c_num + 1)
		input = ''.join(input_list)
	return input

# Recycling from my 12_5.py
def dbl_letter_present_twice(string):
	''' Nice strings have at least one instance of same, consecutive letters '''
	for i in range(len(string)):
		# Iterate, return if double letters exist, when index is out of bounds
		try:
			if string[i] == string[i+1]:
				for j in range(i+2, len(string)):
					try:
						if string[j] == string[j+1]:
							return True
					except IndexError:
						break
		except IndexError:
				return False

def straight_sequence_present(string):
	for i in range(len(string)):
		try:
			trio = ''.join([string[i], string[i+1], string[i+2]])
			if trio in letter_order:
				return True
		except IndexError:
			continue
	return False

def main():
	new_string = string = 'vzbxkghb'
	print("Answer 1 - {}".format(create_new_password(new_string)))
	
	new_string = string2 = 'vzbxxyzz'
	print("Answer 2 - {}".format(create_new_password(new_string)))

if __name__ == '__main__':
	main()
	sys.exit(0)
