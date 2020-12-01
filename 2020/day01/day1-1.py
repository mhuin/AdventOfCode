import sys

with open('input') as rawinput:
    _values = [int(x) for x in rawinput.readlines()]

values = sorted(_values)

magicsum = 2021
d = len(values)

print("%s values to process" % d)

i, j = 0, d

iterations = 0

while i < len(values):
    if magicsum == 2020:
        break
    while j > 0:
        iterations += 1
        magicsum = values[i] + values[j-1]
        if magicsum == 2020:
            break
        elif magicsum < 2020:
            # print("we're too low, increase lower number")
            i += 1
            break
        else:
            # print("we're too high, decrease higher number")
            j -= 1
            break


print("Result found in %s iterations" % iterations)
print('values are %s and %s' % (values[i],values[j-1]))
print('%s x %s = %s' % (values[i], values[j-1], values[i]*values[j-1]))
