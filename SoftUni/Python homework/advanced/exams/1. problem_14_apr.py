from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ') if 0 < int(x) <= 10])
employees = [int(x) for x in input().split(', ')]
total_pizza_count = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()
    employee = employees.pop()

    if order > employee:
        total_pizza_count += employee
        order_left = order - employee
        pizza_orders.appendleft(order_left)
        continue

    total_pizza_count += order

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_count}")
    print(f"Employees: {', '.join(map(str, employees))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
