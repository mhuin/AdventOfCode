
passports = []

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

with open('input') as rawinput:
   for passport_data in rawinput.read().split('\n\n'):
       passport = {}
       # easier to process if all separators are \n
       l = passport_data.replace(' ', '\n')
       for fields in l.split('\n'):
           if fields:
               key, value = fields.split(':')
               passport[key] = value
       passports.append(passport)

print(len(passports))
print(passports)

def is_valid(passport):
    test_fields = set(list(passport.keys()) + ['cid', ])
    if set(valid_fields) == set(test_fields):
        return True
    else:
        print(set(valid_fields) - set(test_fields))
        return False

count = 0
for p in passports:
    if not is_valid(p):
        print(p)
    else:
        count += 1

print(count)
