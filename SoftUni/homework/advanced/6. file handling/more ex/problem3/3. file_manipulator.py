import os

data = input()

while not data == 'End':
    cmd = data.split('-')
    command, file_name = cmd[0], cmd[1]

    if command == 'Create':
        open(file_name, 'w').close()
    elif command == 'Add':
        content = cmd[2]
        with open(file_name, 'a') as f:
            f.write(content)
            f.write('\n')
    elif command == 'Replace':
        old_string, new_string = cmd[2], cmd[3]
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                content = file.read().replace(old_string,new_string)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print("An error occurred")

    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    data = input()