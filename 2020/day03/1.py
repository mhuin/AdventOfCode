import sys

with open('input') as rawinput:
    _values = [x.rstrip() for x in rawinput.readlines()]

# move 1 down, 3 right

tree_count = 0
width = len(_values[0])

for x in range(len(_values)):
    y = 3*x
    print("position %s,%s" % (x,y))
    position = y % width
    print("modulo: %s,%s" % (x,position))
    if _values[x][position] == '#':
        tree_count += 1

print("Encountered %s trees" % tree_count)
        
