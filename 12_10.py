import sys

def see_and_say(input, repeats):
 	#Repeat for required number of steps
	for i in range(repeats):
#		print(i,'-',len(input))
		# Initialize new string and count
		new_input = ''
		count = 1
		# Loop through the latest input
		for c in range(len(input)-1):
			# If current char = next char, increase count
			if input[c] == input[c+1]:
				count += 1
			else:
				# Otherwise, reset count and append to new input string
				new_input += str(count) + input[c]
				count = 1
		# Handle the final character and append to final new input
		if input[-1] == input[-2]:
			count += 1
		new_input += str(count) + input[-1]
		input = new_input
	return len(input)

def main():
	input='1113222113'

	print("Answer 1 - {0}".format(see_and_say(input, 40)))
	print("Answer 2 - {0}".format(see_and_say(input, 50)))

if __name__ == '__main__':
	main()
	sys.exit(0)