from collections import deque

data = input()
queue = deque()

while not data == "End":

    if data == "Paid":
        for x in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(data)

    data = input()

print(f"{len(queue)} people remaining.")
