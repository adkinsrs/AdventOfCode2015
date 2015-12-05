import sys
import binascii
import hashlib

input = 'iwrupvqb'

def md5_to_hex(md5_str):
	h = hashlib.md5()
	h.update(md5_str.encode('ascii'))
	return h.hexdigest()

def string2hex(string):
	''' I thought I was supposed to convert the md5 string to hex in this way '''
	''' ... was quite wrong '''
	#return string.encode('hex')		# Hex encoding for this function removed in Python 3
	# Convert to hex, and then make it readable
	return str(binascii.hexlify(string.encode()), 'ascii')

def starts_with_zeroes(hex_md5, num_zeroes):
	zero_str = '0' * num_zeroes
	if hex_md5.startswith(zero_str):
		# Alternatively 'if hex_md5[:num_zeroes] == zero_str`:
		return True
	else:
		return False

def get_md5_key(input, count):
	key = input + str(count)
	return md5_to_hex(key)

def main():
	count = 0
	while True:
		#print("abcdef609043 - ", md5_to_hex('abcdef609043'))
		#print("pqrstuv1048970 - ", md5_to_hex('pqrstuv1048970'))
		#break 

		md5 = get_md5_key(input, count)
		if (starts_with_zeroes(md5, 5)):
			print ("Answer 1 - {0}".format(count))
			break
		count +=1

	count = 0
	while True:
		md5 = get_md5_key(input, count)
		if (starts_with_zeroes(md5, 6)):
			print ("Answer 2 - {0}".format(count))
			break
		count +=1

if __name__ == '__main__':
	main()
	sys.exit(0)