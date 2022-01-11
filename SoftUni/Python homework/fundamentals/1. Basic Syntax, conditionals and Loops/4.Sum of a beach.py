word = input()
x = word.lower()
sand = x.count("sand")
water = x.count("water")
fish = x.count("fish")
sun = x.count("sun")
sum_of_words = sand + water + fish + sun
print(sum_of_words)