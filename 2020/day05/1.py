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


print(max(map(decode_seat, encoded_seats)))
