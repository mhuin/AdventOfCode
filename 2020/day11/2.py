from functools import reduce

with open('input') as f:
    seats = [l.strip() for l in f.readlines() if l.strip() != 0]

# lines
width = len(seats)
# cols
length = len(seats[0])

def get(line, col, seats_map):
    if line < 0 or col < 0:
        return '.'
    try:
        return seats_map[line][col]
    except IndexError:
        # if out of bounds, consider it to be ground.
        return '.'


def find_nearest_neighbor(line, col, slope, seats_map):
    i, j = slope
    while (0 <= line + i < width) and (0 <= col + j < length):
        candidate = get(line+i, col+j, seats_map)
        if candidate in ['#', 'L']:
            return candidate
        else:
            i += slope[0]
            j += slope[1]
    return '.'


def get_neighbors(x, y, seats_map):
    return [find_nearest_neighbor(x, y, (-1, -1), seats_map),
            find_nearest_neighbor(x, y, (-1, 0), seats_map),
            find_nearest_neighbor(x, y, (-1, 1), seats_map),
            find_nearest_neighbor(x, y, (0, -1), seats_map),
            find_nearest_neighbor(x, y, (0, 1), seats_map),
            find_nearest_neighbor(x, y, (1, -1), seats_map),
            find_nearest_neighbor(x, y, (1, 0), seats_map),
            find_nearest_neighbor(x, y, (1, 1), seats_map)]


def get_state(x, y, seats_map):
    current = get(x, y, seats_map)
    neighbors = get_neighbors(x, y, seats_map)
    if current == 'L' and all(s != '#' for s in neighbors):
        to_return = '#'
    elif current == '#' and sum(map(lambda x: x == '#' and 1 or 0, neighbors)) >= 5:
        to_return = 'L'
    else:
        to_return = current
    #print('%s at (%s,%s) becomes %s' % (current, x, y, to_return))
    return to_return


old_map = seats
width = len(seats)
length = len(seats[0])
new_map = [''.join([get_state(line, col, old_map) for col in range(length)]) for line in range(width)]


while old_map != new_map:
    buf = [''.join([get_state(line, col, new_map) for col in range(length)]) for line in range(width)]
    old_map = new_map
    new_map = buf
    #for line in new_map:
    #    print(line)
    #print('\n')

occupied_seats = reduce(
    lambda x, y: x+y,
    map(lambda x: x == '#' and 1 or 0,
        ''.join(new_map)))

print(occupied_seats)


