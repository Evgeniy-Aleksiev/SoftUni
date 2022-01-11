data = input()

exam_results = {}
submissions = {}

while not data == "exam finished":
    if "banned" in data:
        user = data.split("-")
        exam_results.pop(user[0])
    else:
        username, language, points = data.split("-")
        points = int(points)
        if username not in exam_results:
            exam_results[username] = points
        else:
            if points > exam_results[username]:
                exam_results[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

    data = input()

print("Results:")
[print(f"{key} | {value}") for key, value in sorted(exam_results.items(), key=lambda kvp: (-kvp[1], kvp[0]))]
print(f"Submissions:")
[print(f"{lang} - {cnt_sub}") for lang, cnt_sub in sorted(submissions.items(), key=lambda kvp: (-kvp[1], kvp[0]))]

