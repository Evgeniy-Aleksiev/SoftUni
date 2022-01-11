str1, str2 = input().split()

total_sum = 0

if len(str1) == len(str2):
    for index in range(len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])
elif len(str1) > len(str2):
    str2_index = len(str2) - len(str1)
    for index in range(len(str2)):
        total_sum += ord(str1[index]) * ord(str2[index])
    for i in range(-1, str2_index -1, -1):
        total_sum += ord(str1[i])
else:
    str1_index = len(str1) - len(str2)
    for index in range(len(str1)):
        total_sum += ord(str2[index]) * ord(str1[index])
    for i in range(-1, str1_index - 1, -1):
        total_sum += ord(str2[i])

print(total_sum)