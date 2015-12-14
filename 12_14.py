import sys
import re

def main():
	specs = []
	time = int(sys.argv[2])	# Because I don't feel like hardcoding this time
	for deer in open(sys.argv[1], 'r'):
		deer = deer.strip()
		nums = re.findall('\d+', deer)
		nums = [int(i) for i in nums]
		specs.append(tuple(nums))
	
	# Initialize list for determining accumulated distance per reindeer
	distance = [0] * len(specs)
	# Initialize list for giving points to leaders
	lead = [0] * len(specs)

	for t in range(1,time+1):
		for i in range(len(specs)):
			speed = specs[i][0]
			run_time = specs[i][1]
			rest_time = specs[i][2]
			total_time = run_time + rest_time
			# Could actually shift time range to just range(time) and go
			## if t%total_time < run_time:
			## But this way is less confusing
			if t % total_time <= run_time and t % total_time > 0:
				distance[i] += speed
		# Determine leader after this point in time and assign points
		max_distance = max(distance)
		for j,val in enumerate(distance):
			if val==max_distance:
				lead[j] += 1
				
			

	print("Answer 1, t=2503 - {}".format(max(distance)))
	print("Answer 2, t=2503 - {}".format(max(lead)))

if __name__ == '__main__':
	main()
	sys.exit(0)