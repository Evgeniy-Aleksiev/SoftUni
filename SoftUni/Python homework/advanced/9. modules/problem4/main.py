from constants import operattion_mapper

num_1, operator, num_2 = input().split()
num_1, num_2 = float(num_1), float(num_2)

print(f"{operattion_mapper[operator](num_1, num_2):.2f}" if operattion_mapper.get(operator) else 'Invalid operator')