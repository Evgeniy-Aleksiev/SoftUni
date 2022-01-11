numbers_dictionary = {}

number_as_string = input()

while number_as_string != "Search":
    number = input()
    try:
        number = int(number)
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    number_as_string = input()

searched_number = input()

while searched_number != "Remove":
    try:
        print(numbers_dictionary[searched_number])
    except KeyError:
        print("Number does not exist in dictionary")

    searched_number = input()

num = input()

while num != "End":
    try:
        del numbers_dictionary[num]
    except KeyError:
        print("Number does not exist in dictionary")
    num = input()

print(numbers_dictionary)
