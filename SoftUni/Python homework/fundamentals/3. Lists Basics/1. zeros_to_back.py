numbers = input().split(", ")

zeros_list = []
zeros_count = 0

for index in range(len(numbers)):
    if numbers[index] == "0":
        zeros_count += 1
    else:
        zeros_list.append(int(numbers[index]))

for x in range(zeros_count):
    zeros_list.append(0)
print(zeros_list)



