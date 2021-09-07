command = input()

events = "coding,dog,cat,movie"
big_events = "CODING,DOG,CAT,MOVIE"
coffee_cnt = 0

while not command == "END":
    if command in events:
        coffee_cnt += 1
    elif command in big_events:
        coffee_cnt += 2
    command = input()

if coffee_cnt > 5:
    print("You need extra sleep")
else:
    print(coffee_cnt)