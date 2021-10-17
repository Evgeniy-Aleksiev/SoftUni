from collections import deque

food_quantity = int(input())
orders_queue = deque([int(x) for x in input().split()])
print(max(orders_queue))

while orders_queue:
    if orders_queue[0] > food_quantity:
        print(f'Orders left: {" ".join(map(str, orders_queue))}')
        break

    order = orders_queue.popleft()
    food_quantity -= order

if not orders_queue:
    print('Orders complete')