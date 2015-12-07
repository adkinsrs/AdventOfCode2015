import sys
import re

one_input = set(['NOT', 'LSHIFT', 'RSHIFT', 'AND'])
two_input = set(['AND', 'OR'])

# Didn't use
def int2bin(num):
	return "{0:b}".format(num)
	# Alternative return str(bin(num))[2:] and the slice removes '0b' at start

# Didn't use
def bin2int(binary):
	return int(binary, 2)

def and_signal(circuits, wires):
	return circuits[wires[0]] & circuits[wires[1]]

def and_single_signal(circuits, wire, shift):
	return circuits[wire] & shift

def or_signal(circuits, wires):
	return circuits[wires[0]] | circuits[wires[1]]

def not_signal(circuits, wire):
	return ~circuits[wire]

def lshift_signal(circuits, wire, shift):
	return circuits[wire] << shift

def rshift_signal(circuits, wire, shift):
	return circuits[wire] >> shift

def fill_wire_signals(circuits):
	''' Fill input signals values for each wire '''
	for key in circuits:
		#print("KEY - {0}".format(key))
		# Either will be 'int' result or 'list'
		get_input_signal(circuits, key)
			
def get_input_signal(circuits, wire):
	''' Recursively get signal value for each wire '''
	#print(wire, " - ", circuits[wire])
	if isinstance(circuits[wire], tuple):
		cmd = circuits[wire][0]
		if cmd in two_input and isinstance(circuits[wire][-1],str):
			wires = circuits[wire][1:3]
			[get_input_signal(circuits, i) for i in wires]
			# Now we should have recursively converted the input wires into signals	
			if cmd == "AND":
				circuits[wire] = and_signal(circuits, wires)
			elif cmd == "OR":
				circuits[wire] = or_signal(circuits, wires)
		else:
			shifting = circuits[wire][-1] # Ignored for NOT
			single = circuits[wire][1]
			get_input_signal(circuits, single)
			# Now we should have recursively converted the single input into a signal	
			if cmd == "NOT":
				circuits[wire] = not_signal(circuits, single)
			elif cmd == "AND":
				circuits[wire] = and_single_signal(circuits, single, shifting)
			elif cmd == "LSHIFT":
				circuits[wire] = lshift_signal(circuits, single, shifting)
			elif cmd == "RSHIFT":
				circuits[wire] = rshift_signal(circuits, single, shifting)
	elif isinstance(circuits[wire], str):
		circuits[wire] = circuits[ circuits[wire] ]

def main():
	circuits = dict()
	stack = list()

	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		#Parse out the line components
		direction, wire = line.split(' -> ')

		# Parse out the line components
		input = re.findall("[a-z]{1,2}", direction)
		number = re.findall(r"\d+", direction)	# At this point don't know if it's a signal or a SHIFT num
		command = re.findall("[A-Z]+", direction)

		# Now make branching paths depending on a) num of wires, then b) direction
		if len(input) == 0:	# direct assignment
			circuits[wire] = int(number[0])
		elif len(input) == 1:	# LSHIFT/RSHIFT/NOT/AND
			if len(command) == 0:	# Direct copy of string for now
				circuits[wire] = input[0]
			else:
				if command[0] == 'NOT':
					circuits[wire] = (command[0], input[0], 0)
				else:
					# must be LSHIFT/RSHIFT/AND
					circuits[wire] = (command[0], input[0], int(number[0]))
		elif len(input) == 2:	# AND/OR		
			circuits[wire] = (command[0], input[0], input[1])

	fill_wire_signals(circuits)
	print("Answer 1 - {0}".format(str(circuits['a'])))
	a_wire = circuits['a']

	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		direction, wire = line.split(' -> ')

		input = re.findall("[a-z]{1,2}", direction)
		number = re.findall(r"\d+", direction)	
		command = re.findall("[A-Z]+", direction)

		if len(input) == 0:
			# This here is the only difference... use 'a' to init 'b'
			if wire == 'b':
				circuits[wire] = a_wire
			else:
				circuits[wire] = int(number[0])
		elif len(input) == 1:	
			if len(command) == 0:
				circuits[wire] = input[0]
			else:
				if command[0] == 'NOT':
					circuits[wire] = (command[0], input[0], 0)
				else:
					circuits[wire] = (command[0], input[0], int(number[0]))
		elif len(input) == 2:
			circuits[wire] = (command[0], input[0], input[1])

	fill_wire_signals(circuits)
	print("Answer 2 - {0}".format(str(circuits['a'])))

if __name__ == '__main__':
	main()
	sys.exit(0)
