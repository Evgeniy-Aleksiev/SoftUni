def palindrome_integers(numbers):
    for current_list in numbers:
        if current_list[0] == current_list[-1]:
            print("True")
        else:
            print("False")


list_of_numbers = input().split(", ")
palindrome_integers(list_of_numbers)