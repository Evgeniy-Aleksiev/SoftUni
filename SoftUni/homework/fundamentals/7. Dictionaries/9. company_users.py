data = input()

company_users = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

    data = input()

ascending_order = sorted(company_users.items(), key=lambda kvp: kvp[0])

for company_name_key, id_value in ascending_order:
    print(company_name_key)
    for index in range(len(id_value)):
        print(f"-- {id_value[index]}")