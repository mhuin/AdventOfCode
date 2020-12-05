import re

passports = []

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid_fields = {
    'byr': lambda x: re.match(r'\d{4}', x) and (1920 <= int(x) <= 2002),
    'iyr': lambda x: re.match(r'\d{4}', x) and (2010 <= int(x) <= 2020),
    'eyr': lambda x: re.match(r'\d{4}', x) and (2020 <= int(x) <= 2030),
    'hgt': lambda x: (re.match(r'^\d{3}cm$', x) and (150 <= int(x[:3]) <= 193)) or \
                     (re.match(r'^\d{2}in$', x) and (59 <= int(x[:2]) <= 76)),
    'ecl': lambda x: x in eye_colors,
    'hcl': lambda x: re.match(r'^#[a-f0-9]{6}$', x),
    'pid': lambda x: re.match(r'^\d{9}$', x),
    'cid': lambda x: True,
}



with open('input') as rawinput:
   for passport_data in rawinput.read().split('\n\n'):
       passport = {}
       l = passport_data.replace(' ', '\n')
       for fields in l.split('\n'):
           if fields:
               key, value = fields.split(':')
               passport[key] = value
       passports.append(passport)

def is_valid(passport):
    for i in valid_fields:
        if not valid_fields[i](passport.get(i, '')):
#            print('%s has invalid %s' % (passport, i))
            return False
    return True

count = 0
for p in passports:
    if is_valid(p):
        count += 1

print(count)
