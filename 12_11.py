import sys

bad_letters = set(['i', 'o', 'l'])
good_letters = 'abcdefghjkmnpqrstuvwxyz'

def main():
	input = 'vzbxkghb'
	letter_min = ord('a')
	letter_max = ord('z')
	while True:
		c_num = ord(input[-1])
		# Increment again if incremented letter is in 'bad_letters'
		if chr(c_num + 1) in bad_leters:
			input[-1] = chr(c_num + 2)
		# If new char is beyond 'z', reset to 'a'
		elif c_num + 1 > letter_max:
			input[-1] = 'a'

if __name__ == '__main__':
	main()
	sys.exit(0)