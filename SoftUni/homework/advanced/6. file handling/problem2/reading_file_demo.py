file = open('demo.txt', 'r')
print(file.read(2))
print(file.read(2))
print(file.read(2))
print(file.read())

file.close()

print('-------')

file = open('demo.txt', 'r')
print(file.readline(5))
print(file.readline(5))
print(file.readline(5))
print(file.readline())
print(file.readline(5))

file.close()

print('-------')

file = open("text.txt")
lines = file.readlines()
print(lines)
print('-------')
[print(line, end='') for line in lines]

file.close()

print('-------')

file = open('text.txt', 'r')

for line in file:
    print(line, end='')

file.close()

print('-------')
