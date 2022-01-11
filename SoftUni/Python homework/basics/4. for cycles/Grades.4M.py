students = int(input())
failed_students = 0
failed_evaluation = 0
middle_student = 0
middle_evaluation = 0
good_students = 0
good_evaluation = 0
very_good_students = 0
very_good_evaluation = 0

for evaluation_exam in range(students):
    evaluation_exam = float(input())
    if evaluation_exam < 3:
        failed_evaluation += evaluation_exam
        failed_students += 1
    elif evaluation_exam < 4:
        middle_evaluation += evaluation_exam
        middle_student += 1
    elif evaluation_exam < 5:
        good_evaluation += evaluation_exam
        good_students += 1
    else:
        very_good_evaluation += evaluation_exam
        very_good_students += 1

print(f"Top students: {(very_good_students / students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(good_students / students * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(middle_student / students * 100):.2f}%")
print(f"Fail: {(failed_students / students * 100):.2f}%")
average = (failed_evaluation + middle_evaluation + good_evaluation + very_good_evaluation) / students
print(f"Average: {average:.2f}")
