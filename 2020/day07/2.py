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


def pack_color(color):
    if contains.get(color, None) is None:
        print('%s does not contain any bag' % color)
        return 0
    else:
        keys = list(contains[color].keys())
        print('%s contains %s' % (color, contains[color]))
        return sum(contains[color][k] for k in keys) +\
               reduce(lambda x, y: x+y,
                      (contains[color][k] * pack_color(k) for k in keys), 0)

print(pack_color('shiny gold'))


