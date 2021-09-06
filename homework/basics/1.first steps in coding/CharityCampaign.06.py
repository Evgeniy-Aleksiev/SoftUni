campaign = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

sweets = cakes * 45 + waffles * 5.80 + pancakes * 3.20
daily = sweets * confectioners
whole_sum = daily * campaign
final_sum = whole_sum - whole_sum / 8

print(final_sum)