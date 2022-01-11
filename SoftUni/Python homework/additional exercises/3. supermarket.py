from collections import deque

data = input()
queue = deque()

while not data == 'End':
    if data == 'Paid':
        while queue:
            print(queue.popleft())
        data = input()
        continue
    queue.append(data)
    data = input()

print(len(queue), f'people remaining.')