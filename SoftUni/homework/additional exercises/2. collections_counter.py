import collections

x = int(input())
shoes = []

for i in input().split():
    if len(shoes) < x:
        shoes.append(int(i))

shoe_size = collections.Counter(shoes)
total_price = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoe_size[size]:
        total_price += price
        shoe_size[size] -= 1

print(total_price)
