from itertools import permutations


def possible_permutations(param):
    for permutation in permutations(param):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]