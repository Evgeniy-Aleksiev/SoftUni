n = int(input())

high_snowball_snow = 0
high_snowball_time = 0
high_snowball_quality = 0
high_snowball_value = 0

for number_of_snowballs in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snow_value = (snowball_snow // snowball_time) ** snowball_quality
    if snow_value >= high_snowball_value:
        high_snowball_snow = snowball_snow
        high_snowball_time = snowball_time
        high_snowball_quality = snowball_quality
        high_snowball_value = snow_value

print(f"{high_snowball_snow} : {high_snowball_time} = {high_snowball_value} ({high_snowball_quality})")