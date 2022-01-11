
# representing count of students that each of the employee can help per hour

first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

student_count = int(input())

time_need = 0

while student_count > 0:
    help_per_h = first_employee + second_employee + third_employee
    student_count -= help_per_h
    time_need += 1

    if time_need % 4 == 0:
        time_need += 1

print(f"Time needed: {time_need}h.")
