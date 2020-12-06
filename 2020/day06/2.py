from functools import reduce

with open('input') as rawinput:
    groups = rawinput.read().split('\n\n')


def count_individual_answers(individual):
    def reducer(accumulator, letter):
        accumulator[letter] = accumulator.get(letter, 0) + 1
        return accumulator
    return reduce(reducer, individual, {})


def count_group_answers(group):
    true_group = [g for g in group.split('\n') if g.strip() != '']
    def reducer(accumulator, individual):
        counted = count_individual_answers(individual)
        def update(_accumulator, question):
            _accumulator[question] = _accumulator.get(question, 0) +\
                                     counted[question]
            return _accumulator
        return reduce(update, counted.keys(), accumulator)
    group_answers = reduce(reducer, true_group, {})
    print("Group %s: %s" % (group, group_answers))
    
    return reduce(
        lambda x,y: x+y,
        map(
            lambda q: (group_answers[q] == len(true_group)) and 1 or 0,
            group_answers
        )
    )


total_count = reduce(lambda x,y: x+y, map(count_group_answers, groups), 0)

print("Total count: %s" % total_count)


