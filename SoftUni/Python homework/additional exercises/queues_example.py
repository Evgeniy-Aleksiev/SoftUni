from collections import deque

queue = deque(["Eric, John, Michael"])
queue.append("Terry")
queue.append("Gosho")
queue.popleft()
queue.popleft()
print(queue)

queue = deque(["Eric, John, Michael"])
queue.appendleft("Terry")
queue.appendleft("Gosho")
queue.pop()
queue.pop()
print(queue)
