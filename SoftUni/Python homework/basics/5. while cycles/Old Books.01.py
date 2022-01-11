book_name = input()
current_book = input()
founded_book = False
books_count = 0

while current_book != "No More Books":
    if current_book == book_name:
        founded_book = True
        break
    else:
        books_count += 1
        current_book = input()
if founded_book:
    print(f"You checked {books_count} books and found it." )
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
