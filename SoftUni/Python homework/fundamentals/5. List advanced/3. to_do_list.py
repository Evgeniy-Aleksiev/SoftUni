notes = [0] * 10
command = input()

while not command == "End":
    importance, text = command.split("-")
    index = int(importance) - 1
    notes[index] = text
    command = input()

print([el for el in notes if not el == 0])