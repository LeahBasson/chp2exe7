hourly_wage = input("Enter hourly wage:R")
total_regular_hours = input("Enter total regular hours:")
total_overtime_hours = input("Enter total overtime hours:")
overtime_pay = float(total_overtime_hours)*1.5
total_weekly_pay = float(hourly_wage)*float(total_regular_hours)+float(overtime_pay)
message = "Total weekly pay:"

print(message, total_weekly_pay)