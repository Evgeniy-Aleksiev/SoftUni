n = int(input())

student_academy = {}
average_grade = {}

for _ in range(1, n + 1):
    name = input()
    grade = float(input())
    if name not in student_academy:
        student_academy[name] = []
    student_academy[name].append(grade)

for key, value in student_academy.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        average_grade[key] = average

sorted_by_grade = sorted(average_grade.items(), key=lambda kvp: -kvp[1])
for name, grade_value in sorted_by_grade:
    print(f"{name} -> {grade_value:.2f}")
