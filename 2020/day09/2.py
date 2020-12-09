from functools import reduce


with open('input') as rawinput:
    numbers = [int(l.strip()) for l in rawinput.read().split('\n') if l.strip() != '']


print('Going through %s numbers.' % len(numbers))


def is_valid(chunks, number):
    sorted_chunks = sorted(chunks)
    i, j = 0, (len(sorted_chunks) - 1)
    while i < j:
        candidate = sorted_chunks[i] + sorted_chunks[j]
        if candidate == number:
            #print('%s = %s + %s' % (number, sorted_chunks[i], sorted_chunks[j]))
            return True
        elif candidate > number:
            j -= 1
        else:
            i += 1
    return candidate == number


def is_valid_brute(chunks, number):
    for i in chunks:
        for j in chunks:
            if i != j and (i+j == number):
                return True
    return False


k = 25
chunks = numbers[0:25]
number = numbers[k]
while is_valid(chunks, number):
    # print('Position %s is fine...' % k)
    k += 1
    chunks = numbers[k-25:k]
    number = numbers[k]

print('%s in position %s is not the sum of any tuple in %s' % (numbers[k], k, numbers[k-25:k-1])) 

target = numbers[k]

contiguous_sum = 0
i, j = 0, 1

while j < len(numbers):
    #print('Doing contiguous area [%s:%s] ...' % (i,j), end=' ')
    contiguous_sum = reduce(lambda x, y: x+y, numbers[i:j], 0)
    #print(contiguous_sum)
    if contiguous_sum == target:
        break
    elif contiguous_sum < target:
        j += 1
    else:
        i += 1

print("%s = %s [%s:%s]" % (target, ' + '.join(str(x) for x in numbers[i:j]), i, j))
print("Result found in %s iterations" % (i+j-1))
print("Encryption weakness: %i" % (min(numbers[i:j]) + max(numbers[i:j])))    
