electrons = int(input())

filled_shells = []
n = 1

while not sum(filled_shells) == electrons:
    shell = 2 * pow(n, 2)

    if sum(filled_shells) < electrons:
        if sum(filled_shells) + shell > electrons:
            difference = electrons - sum(filled_shells)
            filled_shells.append(difference)
        else:
            filled_shells.append(shell)
    n += 1

print(filled_shells)
