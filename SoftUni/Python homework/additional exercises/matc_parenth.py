expression = list(input())
parentheses = []

for index, value in enumerate(expression):
    if value == '(':
        parentheses.append(index)

    elif value == ')':
        current_index = parentheses.pop()
        print(''.join(expression[current_index: index +1]))