import re
from functools import reduce

termination_rule = re.compile(r'^(?P<container_color>[a-z ]+) bags contain no other bags\.$')
common_rule = re.compile(r'^(?P<container_color>[a-z ]+) bags contain (?P<contained_bags>.+)\.$')
contained_rule = re.compile(r'(?P<amount>[0-9]+) (?P<contained_color>[a-z ]+) bag[s]?')

contains = {}
contained_by = {}
raw_rules = []

with open('input') as rawinput:
    for rule in rawinput.read().split('\n'):
        if rule == '':
            continue
        m = termination_rule.match(rule)
        if m:
            values = m.groupdict()
            contains[values['container_color']] = None
            continue
        m = common_rule.match(rule)
        if m:
            values = m.groupdict()
            container_color = values['container_color']
            if container_color in contains:
                print('%s has at least two rules' % container_color)
            bags = {}
            for _bag in values['contained_bags'].split(','):
                bag = _bag.strip()
                _ = contained_rule.match(bag)
                bags[_['contained_color']] = int(_['amount'])
                contained_by[_['contained_color']] = contained_by.get(_['contained_color'], {})
                contained_by[_['contained_color']][container_color] = True
            contains[container_color] = bags
            continue
        raise Exception('"%s" cannot be matched' % rule)

seen_colors = []

def count_containers_of_color(color):
    if color in seen_colors:
        print('I have already counted "%s"' % color)
        return -1
    seen_colors.append(color)
    if color not in contained_by:
        print('%s is not contained by any color' % color)
        return 0
    else:
        keys = list(contained_by[color].keys())
        print('%s is contained by %s' % (color, keys))
        return len(keys) + reduce(lambda x, y: x+y , map(count_containers_of_color, keys), 0)


print(count_containers_of_color('shiny gold'))


