text = input().split()
word_filter = [print(word) for word in text if len(word) % 2 == 0]