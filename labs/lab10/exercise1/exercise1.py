position = input("Enter your position : ")
overtime_hours = int(input("Enter your overtime hours : "))
is_weekend = input("Is weekend : ")

# Your code here
base_hourly_rate = 0
if(position == "manager") :
    base_hourly_rate += 35
elif(position == "supervisor") :
    base_hourly_rate += 25
elif(position == "staff") :
    base_hourly_rate += 18

hourly_rate = base_hourly_rate

overtime_pay = (hourly_rate * overtime_hours) + (overtime_hours * 1.5)

if(is_weekend == "yes") :
    weekend_bonus = (5 * overtime_hours)
elif(is_weekend == "no") :
    weekend_bonus = (1 * overtime_hours)

total_pay = weekend_bonus + overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)