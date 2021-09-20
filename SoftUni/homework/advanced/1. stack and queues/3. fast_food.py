from collections import deque

food_quantity = int(input())
sequence = deque(map(int, input().split()))
queue = []
max_num = max(sequence)

for i in range(len(sequence)):
    if sequence[0] <= food_quantity:
        food_quantity -= sequence.popleft()
    else:
        queue.append(' '.join([str(x) for x in sequence]))
        break

if queue:
    print(max_num)
    print(f"Orders left: {' '.join(queue)}")
else:
    print(max_num)
    print("Orders complete")



