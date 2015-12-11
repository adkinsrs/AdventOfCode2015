import sys

bad_letters = set(['i', 'o', 'l'])
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

def main():
	string = 'vzbxkghb'
	while True:
		new_string = increment_letter(string, -1)

if __name__ == '__main__':
	main()
	sys.exit(0)