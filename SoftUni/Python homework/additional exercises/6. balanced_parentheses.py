correct_parentheses = {
    '[': ']',
    '{': '}',
    '(': ')'
    }

parentheses_input = input()
parentheses = []
is_balanced = True

for el in parentheses_input:
    if el in '({[':
        parentheses.append(el)
    else:
        if not parentheses:
            is_balanced = False
            break
        last_parentheses = parentheses.pop()

        if not correct_parentheses[last_parentheses] == el:
            is_balanced = False
            break

if not is_balanced or parentheses:
    print('NO')
else:
    print('YES')