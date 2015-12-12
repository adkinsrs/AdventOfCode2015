import sys
import re
import json

def scrape_for_digits(json_input):
		''' parse out the values in JSON pair and send to be looped through '''
		digit = 0
		# Ignore any JSON with 'red' as a value, including nested JOSN
		if "red" in json_input.values():
			return 0
		digit += handle_list(json_input.values())
		return digit

def handle_list(l):
	''' determine type of the list item and handle appropriately '''
	digit = 0
	for i in l:
		if isinstance(i, list):
			digit += handle_list(i)
		elif isinstance(i, dict):
			digit += scrape_for_digits(i)
		elif is_int(i):
			digit += i
	return digit

# Stole this from Stack Overflow
def is_int(i):
	try:
		int(i)
		return True
	except ValueError:
		return False

def main():
	with open(sys.argv[1]) as fh:
		for input in fh:
			digits = re.findall(r'-?\d+', input)
			digits = [int(i) for i in digits]
			sum_nums = sum(i for i in digits)
		print("Answer 1 - {}".format(sum_nums))

	# Answer 2 requires legitimate JSON parsing
	for input in open(sys.argv[1], 'r'):
		json_input = json.loads(input)
		print("Answer 2 - {}".format(scrape_for_digits(json_input)))

	test1 = json.loads('{"d":[1,2,3]}')
	test2 = json.loads('{"d":[1,{"c":"red","b":2},3]}')
	test3 = json.loads('{"d":"red","e":[1,2,3,4],"f":5}')
	test4 = json.loads('{"d":[1,"red",5]}')

	print("answer = " + str(scrape_for_digits(test1)))
	print("answer = " + str(scrape_for_digits(test2)))
	print("answer = " + str(scrape_for_digits(test3)))
	print("answer = " + str(scrape_for_digits(test4)))

if __name__ == '__main__':
	main()
	sys.exit(0)