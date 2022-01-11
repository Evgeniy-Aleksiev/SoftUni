population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

for number in population:
    if number < minimum_wealth:
        max_population = max(population)
        need_wealth = minimum_wealth - number

        if max_population - need_wealth < minimum_wealth:
            print("No equal distribution possible")
            exit()
        else:
            index_of_max_population = population.index(max_population)
            index_of_number = population.index(number)
            population[index_of_number] += need_wealth
            population[index_of_max_population] -= need_wealth

print(population)