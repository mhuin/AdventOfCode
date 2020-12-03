import re

pattern = re.compile(r'^(?P<lower>\d+)-(?P<upper>\d+) (?P<char>\w): (?P<password>\w+)$')

with open('input') as rawinput:
    passwords = [pattern.match(x).groupdict() for x in rawinput.readlines()]

def isvalid(entry) -> bool:
    lower, upper = int(entry['lower']), int(entry['upper'])
    counter = [1 if x == entry['char'] else 0 for x in entry['password']]
    return lower <= sum(counter) <= upper

valid_count = 0

for entry in passwords:
    if isvalid(entry):
        valid_count += 1

print(valid_count)
