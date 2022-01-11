from collections import deque

def is_valid_order(order):
    return 0 < order <= 10


def pizza_making(orders, employees, total_pizza=0):

    while orders and employees:
        current_order = orders.popleft()

        if not is_valid_order(current_order):
            continue

        current_employee = employees.pop()

        if current_order <= current_employee:
            total_pizza += current_order
            continue

        total_pizza += current_employee
        current_order -= current_employee
        orders.appendleft(current_order)

    return orders, employees, total_pizza

pizza_orders = deque([int(x) for x in input().split(', ')])
employees_pizza_making_capacities = [int(x) for x in input().split(', ')]

pizza_orders, employees_pizza_making_capacities, total_pizza = pizza_making(pizza_orders, employees_pizza_making_capacities)

if not pizza_orders:
    print(f"""All orders are successfully completed!
Total pizzas made: {total_pizza}
Employees: {', '.join(map(str, employees_pizza_making_capacities))}""")
else:
    print(f"""Not all orders are completed.
Orders left: {', '.join(map(str, pizza_orders))}""")