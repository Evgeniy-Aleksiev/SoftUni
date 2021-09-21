def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def average_grade(values):
    return sum(values) / len(values)


students_and_grades = input_to_list(int(input()))
students = {}

for line in students_and_grades:
    name, grade = line.split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items():
    grade_str = ' '.join(map(lambda grade: f'{grade:.2f}', value))
    average = average_grade(value)
    print(f"{key} -> {grade_str} (avg: {average:.2f})")

