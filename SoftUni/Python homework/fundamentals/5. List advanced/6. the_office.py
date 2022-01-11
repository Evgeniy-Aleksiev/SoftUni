employee = input().split()
factor = int(input())
employee_happiness = [int(happiness) * factor for happiness in employee]
average_happiness = [el for el in employee_happiness if el >= sum(employee_happiness) / len(employee_happiness)]

if len(average_happiness) >= len(employee) / 2:
    print(f"Score: {len(average_happiness)}/{len(employee)}. Employees are happy!")
else:
    print(f"Score: {len(average_happiness)}/{len(employee)}. Employees are not happy!")