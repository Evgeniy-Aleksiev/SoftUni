total_groups = int(input())

total_people = 0
musala_group = 0
monblan_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0
for group in range(total_groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        musala_group += people_in_group
    elif people_in_group <= 12:
        monblan_group += people_in_group
    elif people_in_group <= 25:
        kilimandjaro_group += people_in_group
    elif people_in_group <= 40:
        k2_group += people_in_group
    else:
        everest_group += people_in_group

print(f"{(musala_group / total_people * 100):.2f}%")
print(f"{(monblan_group / total_people * 100):.2f}%")
print(f"{(kilimandjaro_group / total_people * 100):.2f}%")
print(f"{(k2_group / total_people * 100):.2f}%")
print(f"{(everest_group / total_people * 100):.2f}%")
