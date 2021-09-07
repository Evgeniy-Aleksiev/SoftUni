file = input().split('\\')

filename = file[-1].split(".")[0]
extension = file[-1].split(".")[1]

print(f"File name: {filename}\nFile extension: {extension}")
