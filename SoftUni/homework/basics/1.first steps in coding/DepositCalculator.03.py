deposit = float(input())
monthly_interest = int(input())
yearly_interest = float(input())

interest = deposit * yearly_interest / 100
month_interest = interest / 12
sum = deposit + monthly_interest * month_interest

print(sum)