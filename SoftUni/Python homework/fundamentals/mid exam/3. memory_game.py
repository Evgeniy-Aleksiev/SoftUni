sequence_of_elements = [num for num in input().split()]
command = input()

moves_cnt = 0

while not command == "end":
    i = command.split()
    index1 = int(i[0])
    index2 = int(i[1])
    moves_cnt += 1

    if index1 == index2 or index1 < 0 or index2 < 0 or\
            len(sequence_of_elements) <= index1 or len(sequence_of_elements) <= index2:
        print("Invalid input! Adding additional elements to the board")
        half = len(sequence_of_elements) // 2
        text = f"-{moves_cnt}a"
        sequence_of_elements.insert(half, text)
        sequence_of_elements.insert(half, text)
    else:
        if sequence_of_elements[index1] == sequence_of_elements[index2]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[index1]}!")
            x = sequence_of_elements.pop(index1)
            sequence_of_elements.remove(x)
        else:
            print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {moves_cnt} turns!")
        break
    command = input()

if command == "end":
    print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
