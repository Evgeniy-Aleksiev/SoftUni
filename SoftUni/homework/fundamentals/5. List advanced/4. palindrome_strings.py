text = input().split()
palindrome = input()

palindrome_list = [word for word in text if word == word[::-1]]
print(palindrome_list)
print(f"Found palindrome {text.count(palindrome)} times")