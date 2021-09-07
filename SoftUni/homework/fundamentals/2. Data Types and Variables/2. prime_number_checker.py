number = int(input())

prime_number = True

for i in range(2, number):
    if number % i == 0:
        prime_number = False

print(prime_number)