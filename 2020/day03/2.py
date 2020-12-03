import sys

with open('input') as rawinput:
    _values = [x.rstrip() for x in rawinput.readlines()]

width = len(_values[0])
print(width)

def count_trees(x_step, y_step):
    tree_count = 0

    x, y = 0, 0
    while x < len(_values):
        if _values[x][y] == '#':
            tree_count += 1
        x += x_step
        y = (y + y_step) % width
    return tree_count

t11 = count_trees(1, 1)
print('1,1: %s trees' % t11)
t13 = count_trees(1, 3)
print('1,3: %s trees' % t13)
t15 = count_trees(1, 5)
print('1,5: %s trees' % t15)
t17 = count_trees(1, 7)
print('1,7: %s trees' % t17)
t21 = count_trees(2, 1)
print('2,1: %s trees' % t21)

print("Puzzle answer: %s" % (t11*t13*t15*t17*t21)) 
