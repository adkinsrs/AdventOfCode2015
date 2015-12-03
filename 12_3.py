import sys

def answer_2(file):
	# What some people did in reddit was the specify the amount of Santas
	# This would allow for storing each Santa's coords in a 2d array and iterating who moves with modulo	

	#Initialize Santa and Robo coords
	santa_x = 0
	robo_x = 0
	santa_y = 0
	robo_y = 0
	coords = [(robo_x, robo_y)]
	santa_turn = True

	with open(file, 'r') as fh:
		for line in fh:
			line = line.strip()
			for dir in line:
				if dir == '^':
					# Ternary form wouldn't work
					if santa_turn:
						santa_y +=1
					else:
						robo_y +=1
				elif dir == 'v':
					if santa_turn:
						santa_y +=-1
					else:
						robo_y +=-1
				elif dir == '>':
					if santa_turn:
						santa_x +=1
					else:
						robo_x +=1
				elif dir =='<':
					if santa_turn:
						santa_x +=-1
					else:
						robo_x +=-1

				if santa_turn:
					if (santa_x, santa_y) not in coords:
						coords.append((santa_x, santa_y))
					santa_turn = False
				else:
					if (robo_x, robo_y) not in coords:
						coords.append((robo_x, robo_y))
					santa_turn = True

		print ("Answer 2 - ", str(len(coords)))

def main():
	# Initialize first coordinate
	x_coord = 0
	y_coord = 0
	coords = [(x_coord, y_coord)]
	# If I had made coords a 'set' type, I could have avoided the if statement later by using set.add()	

	file = sys.argv[1]
	with open(file, 'r') as fh:
		# There's only 1 line in this file
		for line in fh:
			line = line.strip()
			for dir in line:
				if dir == '^':
					y_coord += 1
				elif dir == 'v':
					y_coord += -1
				elif dir == '>':
					x_coord += 1
				elif dir == '<':
					x_coord += -1
				
				if (x_coord, y_coord) not in coords:
					coords.append((x_coord, y_coord))
		print ("Answer 1 - ", str(len(coords)))

	answer_2(file)

if __name__ == '__main__':
	main()
	sys.exit(0)
