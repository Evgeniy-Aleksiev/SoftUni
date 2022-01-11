students = {}

for _ in range(int(input())):
    line = tuple(input().split())
    name, grade = line

    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    average = (sum(grades)) / len(grades)
    str_grades = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    print(f"{student} -> {str_grades} (avg: {average:.2f})")
