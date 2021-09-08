# count of people (employee can help per hour)
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_people_count = int(input())

total_time = 0

while not total_people_count == 0:
    employees_can_help = first_employee + second_employee + third_employee

    if employees_can_help >= total_people_count:
        total_people_count = 0
    else:
        total_people_count -= employees_can_help

    total_time += 1
    if total_time % 4 == 0:
        total_time += 1

print(f"Time needed: {total_time}h.")
