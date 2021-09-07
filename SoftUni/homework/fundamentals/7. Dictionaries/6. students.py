data = input()
courses = {}

while ":" in data:
    name, student_id, course = data.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][student_id] = name
    data = input()

name_of_course = ' '.join(data.split("_"))
for key, value in courses.items():
    if key == name_of_course:
        [print(f"{name_stud} - {id_stud}") for (id_stud, name_stud) in value.items()]
