products = {}

for _ in range(int(input())):
    name, space, price = input().rpartition(' ')
    products[name] = products.get(name, 0) + int(price)
for key, value in products.items():
    print(key, value)


