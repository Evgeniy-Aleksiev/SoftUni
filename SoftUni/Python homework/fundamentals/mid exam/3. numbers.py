sequence_of_numbers = [int(x) for x in input().split()]

above_described_numbers = []
top_five = []
average_sequence = sum(sequence_of_numbers) / len(sequence_of_numbers)
no_elements = False

for element in sequence_of_numbers:
    if element > average_sequence:
        above_described_numbers.append(element)
above_described_numbers.sort(reverse=True)

while not len(top_five) == 5 or len(above_described_numbers) == 0:
    if len(above_described_numbers) == 0:
        no_elements = True
        break
    else:
        catch = above_described_numbers.pop(0)
        top_five.append(catch)

if no_elements:
    print("No")
else:
    str_top_five = [str(x) for x in top_five]
    print(' '.join(str_top_five))
