import sys
import re

test = [r'""',r'"abc"',r'"aaa\"aaa"',r'"\x27"']

def main():
	literal_len = 0
	encoded_len = 0
	#for line in test:
	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		line = line[1:-1]	# Gotta remove so \\" at end doesn't match
		literal_len += 2	# Subtract for dbl quotes
		escape_slash = re.findall(r'\\\\',line)
		literal_len += len(escape_slash)
		line = re.sub(r'\\\\','',line)	# Get those pesky backslashes out of here
		escape_quote = re.findall(r'\\"',line)
		literal_len += len(escape_quote)
		escape_hex = re.findall(r'\\x',line)	# easier than doing full hex regex
		literal_len += 3*len(escape_hex)	# 4-characters in code
		#print(line, " -> ", literal_len)
	
	#for line in test:	
	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		line = line[1:-1]	# Gotta remove so \\" at end doesn't match
		encoded_len += 4	# Add 2 for each new encoded dbl quotes
		escape_slash = re.findall(r'\\',line)	# All slashes will be encoded
		encoded_len += len(escape_slash)
		line = re.sub(r'\\\\','',line)	# Get those pesky backslashes out of here
		escape_quote = re.findall(r'\\"',line)
		encoded_len += len(escape_quote)	# Slash previously encoded, now do dbl-quote
		#escape_hex = re.findall(r'\\x',line)
		#encoded_len += 3*len(escape_hex)	# Slash was encoded previously
		print(line, " -> ", encoded_len)
	print("Answer 1 - {0}".format(literal_len))
	print("Answer 2 - {0}".format(encoded_len))
	
	# Reddit solution
	#print(sum(len(s[:-1]) - len(eval(s)) for s in open(sys.argv[1])))

if __name__ == '__main__':
	main()
	sys.exit(0)