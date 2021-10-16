from collections import deque

queue = deque(input().split())
n = int(input())

while True:
    for _ in range(n - 1):
        queue.append(queue.popleft())
    name = queue.popleft()
    if not queue:
        print('Last is', name)
        break
    print('Removed', name)