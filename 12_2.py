import sys
from functools import reduce # not in global namespace in Python3

def main():
	file = sys.argv[1]  # I forget that sys.argv[0] is the script itself
	with open(file, 'r') as fh:
		running_total = 0
		ribbon_total = 0
		for line in fh:
			line = line.strip()
			dimensions = line.split('x')
			dimensions = [int(i) for i in dimensions]			

			l_by_h = dimensions[0] * dimensions[1]
			l_by_w = dimensions[0] * dimensions[2]
			h_by_w = dimensions[1] * dimensions[2]
			areas = list((l_by_h, l_by_w, h_by_w))
			lowest_area = min(areas)
			running_total += sum(2*i for i in areas)	# Think reduce() would work here also
			running_total += lowest_area
			
			lh_perim = 2 * (dimensions[0] + dimensions[1])
			lw_perim = 2 * (dimensions[0] + dimensions[2])
			hw_perim = 2 * (dimensions[1] + dimensions[2])
			perims = list((lh_perim, lw_perim, hw_perim))
			lowest_perim  = min(perims)
			# Reduce - x is accumulated val, y is updated val (next list index)
			### Reduces the list until a scalar is formed
			volume = reduce(lambda x, y: x*y, dimensions)
			ribbon_total += lowest_perim + volume
			
		print ("Answer 1 - ", str(running_total))
		print ("Answer 2 - ", str(ribbon_total))

if __name__ =='__main__':
	main()
	sys.exit(0)
