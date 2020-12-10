from functools import reduce


with open('input') as rawinput:
    adapters = [int(l) for l in rawinput.readlines() if l.strip() != '']

sorted_adapters_chain = sorted(adapters, reverse=True) + [0, ]
builtin_adapter_joltage = sorted_adapters_chain[0] + 3

def get_jolt_difference(accumulator, adapter):
    jolt_differences, last_adapter = accumulator
    difference = last_adapter - adapter
    jolt_differences[difference] = jolt_differences.get(difference, 0) +1
    return jolt_differences, adapter


jolt_differences, _ = reduce(get_jolt_difference, sorted_adapters_chain, ({}, builtin_adapter_joltage))

print(jolt_differences)
print(jolt_differences[1] * jolt_differences[3])
