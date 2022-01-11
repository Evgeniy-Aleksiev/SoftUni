line = input().split('|')
values = []

for line_inx in range(len(line)):
    value = line.pop().split()
    values += value

print(' '.join(values))