def chairs(values, n, index, people):
    if len(people) == n:
        print(', '.join(people))
        return

    for i in range(index, len(values)):
        people.append(values[i])
        chairs(values, n, i + 1, people)
        people.pop()


names = input().split(', ')
count = int(input())
chairs(names, count, 0, [])
