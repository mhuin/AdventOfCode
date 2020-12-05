from functools import reduce

with open('input') as rawinput:
    encoded_seats = [s for s in rawinput.read().split('\n') if s != '']

def decode_column(encrypted_columns):
    def unbin(accumulator, i):
        if encrypted_columns[i] == 'L':
            return accumulator
        else:
            return accumulator + 2**(2-i)
    return reduce(unbin, range(3), 0)

def decode_row(encrypted_rows):
    def unbin(accumulator, i):
        if encrypted_rows[i] == 'F':
            return accumulator
        else:
           return accumulator + 2**(6-i)
    return reduce(unbin, range(7), 0)

def decode_seat(seat):
    column = decode_column(seat[-3:])
    row = decode_row(seat[:7])
    return column + row * 8


ordered_seats = sorted(encoded_seats, key=decode_seat)

min_seat, max_seat = ordered_seats[0], ordered_seats[-1]
min_seat_id, max_seat_id = decode_seat(min_seat), decode_seat(max_seat)

print('Min seat is %s (ID %s)' % (min_seat, decode_seat(min_seat)))
print("Got %s boarding passes" % len(ordered_seats))
print("Got %s possible seats" % (decode_seat(max_seat) - decode_seat(min_seat) + 1))

#TODO can we break a reduce?
for i in range(min_seat_id, max_seat_id):
    if decode_seat(ordered_seats[i-min_seat_id]) != i:
        missing_seat = i
        print("Missing seat ID: %s" % missing_seat)
        break

# Validation
print(missing_seat not in [decode_seat(s) for s in encoded_seats])
