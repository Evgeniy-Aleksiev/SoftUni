data = input()

courses = {}
course_len = {}
while not data == "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
        course_len[course_name] = 0
    courses[course_name].append(student_name)
    course_len[course_name] += 1

    data = input()

descending_order = sorted(course_len.items(), key=lambda kvp: -kvp[1])
for course_key, values in descending_order:
    print(f"{course_key}: {values}")
    for name in sorted(courses[course_key]):
        print(f"-- {name}")
