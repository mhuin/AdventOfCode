import sys
import time

with open('input') as rawinput:
    _values = [int(x) for x in rawinput.readlines()]

values = sorted(_values)

magicsum = 2021
d = len(values)

#print("%s values to process" % d)

i, j, k = 0, 1, d

iterations = 0

start = time.time()
while i < j < len(values):
    if magicsum == 2020:
        break
    while k > 0:
        magicsum = values[i] + values[j] + values[k-1]
        if magicsum == 2020:
            iterations += 1
            break
        elif magicsum > 2020:
#            print("we're too high, decrease k")
            k -= 1
            iterations += 1
            break
        else:
            while i < j:
                iterations += 1
                magicsum = values[i] + values[j] + values[k-1]
                if magicsum == 2020:
                    break
                elif magicsum < 2020:
#                    print("too low, increase i")
                    i += 1
                else:
#                    print("too high, increase j and reset i")
                    j += 1
                    i = 0
                    break
            if i == j:
#                print("completed inner loop, increase j and reset i")
                j += 1
                i = 0
stop = time.time()

print("Result found in %s iterations, %.3f ms" % (iterations, (stop-start)*1000.))
print('%s + %s + %s = %s' % (values[i], values[j], values[k-1], values[i] + values[j] + values[k-1]))
print('%s x %s x %s = %s' % (values[i], values[j], values[k-1], values[i]*values[j]*values[k-1]))
