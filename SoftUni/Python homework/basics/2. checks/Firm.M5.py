need_hours = int(input())       # Необходимите часове
days = int(input())             # Дните с които  фирмата разполага
workers = int(input())          # Броят на служителите работещи извънредно

training = days - days * 0.10
work_hours = training * 8
overtime = workers * (days * 2)
hours = int(work_hours + overtime)

if hours < need_hours:
    hours = need_hours - hours
    print(f"Not enough time!{int(hours)} hours needed.")
else:
    hours -= need_hours
    print(f"Yes!{int(hours)} hours left.")