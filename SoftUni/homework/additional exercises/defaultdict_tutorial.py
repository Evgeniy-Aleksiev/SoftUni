from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
new_list = []

for i in range(n):
    d[input()].append(i + 1)

for j in range(m):
    new_list += [input()]

for i in new_list:
    if i in d:
        print(" ".join( map(str, d[i])))
    else:
        print(-1)