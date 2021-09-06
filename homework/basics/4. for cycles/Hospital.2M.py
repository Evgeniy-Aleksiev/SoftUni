period_of_calculations = int(input())
medics = 7
treated_patients = 0
untreated_patients = 0

for inspection_per_day in range(1, period_of_calculations + 1):
    patient = int(input())
    if inspection_per_day % 3 == 0 and untreated_patients > treated_patients:
        medics += 1
    if patient >= medics:
        treated_patients += medics
        untreated_patients += patient - medics
    else:
        treated_patients += (medics + patient) - medics
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
