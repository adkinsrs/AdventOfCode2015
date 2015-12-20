import sys
import re
from collections import defaultdict

def main():
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

    elem_substr = []
    molecules_set = set()
    for c in range(len(molecule)):
        # If uppercase char is hit and isn't the first letter in molecule, we have our element
        if molecule[c].isUpper() and len(elem_substr):
            substr = ''.join(elem_substr)
            if elements[substr]:
                index_offset = c - len(substr)
                # Create new molecule and add to set if unique
                for r in elements[substr]:
                    fixed_mol = molecule[:index_offset] + re.sub(substr, r, molecule[index_offset:c]) + molecule[c:]
                    molecules_set.add(fixed_mol)
            elem_substr = []
        else:
            elem_substr.append(c)
    
    # Take care of final upper-case
    substr = ''.join(elem_substr)
    if elements[substr]:
        index_offset = len(molecule) - len(substr)
        # Create new molecule and add to set if unique
        for r in elements[substr]:
            fixed_mol = molecule[:index_offset] + re.sub(substr, r, molecule[index_offset:])
            molecules_set.add(fixed_mol)
                    
    print("Answer 1 - {}".format(len(molecules_set)))

if __name__ == '__main__':
    main()
    sys.exit(0)