odd_set = set()
even_set = set()


for row in range(1, int(input()) + 1):
    names = input()
    number = sum([ord(ch) for ch in names]) // row

    if number % 2 == 0:
        even_set.add(number)
    else:
        odd_set.add(number)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(odd_set.union(even_set))
elif odd_sum > even_sum:
    diff = odd_set.difference(even_set)
    print(', '.join(map(str, diff)))
elif odd_sum < even_sum:
    symmetric = odd_set.symmetric_difference(even_set)
    print(', '.join(map(str, symmetric)))

