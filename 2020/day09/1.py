with open('input') as rawinput:
    numbers = [int(l.strip()) for l in rawinput.read().split('\n') if l.strip() != '']


def is_valid(chunks, number):
    sorted_chunks = sorted(chunks)
    i, j = 0, (len(sorted_chunks) - 1)
    candidate = sorted_chunks[0] + sorted_chunks[-1]
    while i < j:
        if candidate == number:
            print('%s = %s + %s' % (number, sorted_chunks[i], sorted_chunks[j]))
            return True
        elif candidate > number:
            j -= 1
        else:
            i += 1
        candidate = sorted_chunks[i] + sorted_chunks[j]
    return candidate == number


def is_valid_brute(chunks, number):
    for i in chunks:
        for j in chunks:
            if i != j and (i+j == number):
                return True
    return False


k = 25
chunks = numbers[0:25]
print(len(chunks))
number = numbers[k]
while is_valid_brute(chunks, number):
    print('Position %s is fine...' % k)
    k += 1
    chunks = numbers[k-25:k]
    number = numbers[k]

print('%s in position %s is not the sum of any tuple in %s' % (numbers[k], k, numbers[k-25:k-1])) 
    
