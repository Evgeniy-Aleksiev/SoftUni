text = input()
list_text = text.split(", ")
count_sheep = 0
for x in range(len(list_text) -1, -1, -1):
    if list_text[x] == "wolf":
        if not count_sheep:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")
    else:
        count_sheep += 1