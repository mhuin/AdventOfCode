import re

pattern = re.compile(r'^(?P<lower>\d+)-(?P<upper>\d+) (?P<char>\w): (?P<password>\w+)$')

with open('input') as rawinput:
    passwords = [pattern.match(x).groupdict() for x in rawinput.readlines()]

def isvalid(entry) -> bool:
    lower, upper = int(entry['lower']), int(entry['upper'])
    lower_test = entry['password'][lower-1] == entry['char']
    upper_test = entry['password'][upper-1] == entry['char']
    return (lower_test and not upper_test) or (upper_test and not lower_test)

valid_count = 0

for entry in passwords:
    if isvalid(entry):
        valid_count += 1

print(valid_count)
