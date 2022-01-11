def n_set(numbers):
    first = set()
    for _ in range(numbers):
        number = int(input())
        first.add(number)
    return first


def m_set(numbers):
    second = set()
    for _ in range(numbers):
        number = int(input())
        second.add(number)
    return second


def intersection_of_two_sets(set_1, set_2):
    return set_1.intersection(set_2)


n, m = [int(x) for x in input().split()]
first_set = n_set(n)
second_set = m_set(m)

print('\n'.join(map(str, intersection_of_two_sets(first_set, second_set))))
