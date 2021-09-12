from itertools import combinations_with_replacement

a, b = input().split()
print(*[''.join(x) for x in list(combinations_with_replacement(sorted(a), int(b)))], sep='\n')
