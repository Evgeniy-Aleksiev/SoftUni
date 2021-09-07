text = input().split(", ")
words = input()
new_list = [el for el in text if el in words]
print(new_list)