import sys
import re
from itertools import combinations

def main():
	input = sys.argv[1]
	ing = []	# Ingredient
	scores = []

	for line in open(input, 'r'):
		stats = re.findall('-?\d+', line)
		stats = [int(i) for i in stats]
		ing.append(tuple(stats))

	# Was originally going to do 3 nested loops but I may have "peeked" at a reddit topic ;-)
	# This makes the assumption that each ingredient is represented (no 100/0/0/0 ratio)
	for i in combinations(range(1,100),3):
		first_amt = i[0]
		second_amt = i[1] - i[0]
		third_amt = i[2] - i[1]
		fourth_amt = 100 - i[2]

		amounts = [first_amt, second_amt, third_amt, fourth_amt]
	
		# only capacity [0] and durability [1] may have negative values
		capacity = 0
		durability = 0
		calories = 0
		for c in range(4):
			capacity += ing[c][0] * amounts[c]	# probably should have used a map file
			durability += ing[c][1] * amounts[c]
			calories += ing[c][4] * amounts[c]
		if capacity < 0 or durability < 0:
			continue
		# Calorie-counting is for the second part
		if calories != 500:
			continue

		profile = 1
		zipped_ing = list(zip(*ing))	#Zip creates iterators of tuples where each tuple is the ith element
		# excluding calories for now
		for j in range(4):
			# ^ to iterate over the stats
			stats_profile = 0
			for k in range(len(zipped_ing[j])):
				# ^ to iterate over the ingredients (which equals 'amounts' list)
				stats_profile += zipped_ing[j][k] * amounts[k]
				#print(ing[j][k], "---", amounts[k])
			#print(stats_profile)
			profile *= stats_profile
		#print("---",profile,"---")
		scores.append(profile)

	print ("Answer 1 - best score - {}".format(max(scores)))


if __name__ == '__main__':
	main()
	sys.exit(0)