inherited_money = float(input())
year_lives = int(input())
ivan_years = 18

for year in range(1800, year_lives + 1):
    if year % 2 == 0:
        inherited_money -= 12000
        ivan_years += 1
    else:
        inherited_money -= 12000 + (ivan_years * 50)
        ivan_years += 1
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    inherited_money = abs(inherited_money)
    print(f"He will need {inherited_money:.2f} dollars to survive.")