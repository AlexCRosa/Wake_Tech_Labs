#
# Alex Cesar Rosa
# 5/28/2024
#

hourly_wage = float(input("Enter hourly wage: $"))
regular_hours = int(input("Enter the regular hours: "))
overtime_hours = int(input("Enter the overtime hours: "))

print(f"The total weekly pay is ${(hourly_wage * regular_hours) + (overtime_hours * (hourly_wage * 1.5))}")