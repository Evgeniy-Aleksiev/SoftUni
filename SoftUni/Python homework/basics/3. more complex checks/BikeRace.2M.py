juniors_raiders = int(input())
senior_raiders = int(input())
type_of_route = input()
total_raiders = juniors_raiders + senior_raiders
price = 0

if type_of_route == "trail":
    price = juniors_raiders * 5.50 + senior_raiders * 7
elif type_of_route == "cross-country":
    if total_raiders >= 50:
        price = juniors_raiders * 8 + senior_raiders * 9.50
        price *= 0.75
    else:
        price = juniors_raiders * 8 + senior_raiders * 9.50
elif type_of_route == "downhill":
    price = juniors_raiders * 12.25 + senior_raiders * 13.75

elif type_of_route == "road":
    price = juniors_raiders * 20 + senior_raiders * 21.50

costs = price * 0.95
print(f"{costs:.2f}")