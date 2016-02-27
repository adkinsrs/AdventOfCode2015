import sys
import re
from collections import defaultdict

def main():
    # Elements are key, and what they evolve into are values
    elements = defaultdict(list)
    elements_done = False
    molecule = ''
    m_list = []
    
    for line in open(sys.argv[1], 'r'):
        line = line.strip()
        if not len(line):
            elements_done = True
        
        if elements_done:
            molecule = line
        else:
            parts = line.split(' => ')
            elements[parts[0]].append(parts[1])

    # Part 1 - Number of distinct molecules with just one replacement from original molecule
    elem_substr = []
    molecules_set = set()
    for c in range(len(molecule)):
        # If uppercase char is hit and isn't the first letter in molecule, we have our element
        if molecule[c].isupper() and len(elem_substr):
            substr = ''.join(elem_substr)
            if elements[substr]:
                index_offset = c - len(substr)
                # Create new molecule and add to set if unique
                for r in elements[substr]:
                    fixed_mol = molecule[:index_offset] + re.sub(substr, r, molecule[index_offset:c]) + molecule[c:]
                    molecules_set.add(fixed_mol)
            elem_substr = []
            elem_substr.append(molecule[c])
        else:
            elem_substr.append(molecule[c])
    
    # Take care of final upper-case
    substr = ''.join(elem_substr)
    if elements[substr]:
        index_offset = len(molecule) - len(substr)
        # Create new molecule and add to set if unique
        for r in elements[substr]:
            fixed_mol = molecule[:index_offset] + re.sub(substr, r, molecule[index_offset:])
            molecules_set.add(fixed_mol)
                    
    print("Answer 1 - {}".format(len(molecules_set)))

    # Part 2 - fewest number of steps to go from 'e' to the input molecule
    # Honestly I kind of cheated with looking at the Day 19 in the AdventOfCode subreddit
    # Didn't look at code answers per se, but the theory answer
    # This is over 2 months since Advent of Code took place and so I honestly don't have too much ambition haha

    # X->XX => # steps = len(substring) - 1
    # X->X(X) => # steps = len(substring) - count["(",")"] - 1
    # X->X(X,X) => # steps = len(substring) - count["(",")"] - count[","]*2 - 1
    # "(" = Rn, ")" = Ar, "," = Y

    steps = 0
    molecule = molecule[::-1]		# Reverse the molecule input
    reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', open(sys.argv[1], 'r').read())}
    def rep(x):
        return reps[x.group()]
    while molecule != 'e':
        # Join all keys that match, and substitute in the value to make the new molecule but only 1 sub at a time
        molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
        steps +=1
    print("Answer 2 - {}".format(str(steps)))

if __name__ == '__main__':
    main()
    sys.exit(0)