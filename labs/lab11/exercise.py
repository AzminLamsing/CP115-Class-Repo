# The smart way - let Python count for you
print("Printing 5 receipts:")
for receipt_number in range(5):
    print(f"Receipt #{receipt_number + 1} printed")

# Single parameter: range(stop)
print("Basic range counting:")
for count in range(4):
    print(f"Count: {count}")

# Two parameters: range(start, stop)
print("Custom start and stop:")
for number in range(10, 15):
    print(f"Number: {number}")

# Three parameters: range(start, stop, step)
print("Counting by 3s:")
for value in range(0, 12, 3):
    print(f"Value: {value}")

# Counting by 5s
print("Counting by 5s:")
for value in range(0, 25, 5):
    print(f"Value: {value}")

# Count determined by user input
team_size = int(input("How many team members? "))
print(f"Registering {team_size} team members:")

for member in range(1, team_size + 1):
    name = input(f"Enter name for member {member}: ")
    print(f"Member {member}: {name} registered")

print("Team registration complete!")

# Count from calculation
months_in_year = 12
years = 3
total_months = months_in_year * years

print(f"Monthly report for {years} years:")
for month in range(1, total_months + 1):
    year_number = (month - 1) // 12 + 1
    month_in_year = (month - 1) % 12 + 1
    print(f"Month {month}: Year {year_number}, Month {month_in_year}")

# Counter used in calculations
print("Multiplication table for 7:")
for multiplier in range(1, 11):
    result = 7 * multiplier
    print(f"7 x {multiplier} = {result}")

# Basic while loop counter pattern
attempt = 1                    # Step 1: Initialize
while attempt <= 3:            # Step 2: Condition
    print(f"Attempt number: {attempt}")
    attempt += 1               # Step 3: Update

# Counter increment varies
week = 1
while week <= 4:
    points = int(input(f"Week {week} points: "))

    if points >= 100:
        week += 2  # Skip ahead
    else:
        week += 1  # Normal progress

# Multiple counters working together
day = 1
total_sales = 0
successful_days = 0

print("Daily sales tracking:")
while day <= 7:  # One week
    daily_sales = float(input(f"Day {day} sales: RM"))
    total_sales += daily_sales

    if daily_sales >= 1000:
        successful_days += 1
        print(f"Day {day}: Target achieved!")
    else:
        print(f"Day {day}: Below target")

    day += 1

print(f"Week summary: RM{total_sales} total, {successful_days} successful days")

# Custom step pattern
level = 1
step = 1

while level <= 10:
    print(f"Level: {level}")
    level += step
    step += 1  # Increase step each time

# Safe counter practice
attempts = 0
while attempts < 5:
    print(f"Attempt {attempts + 1}")
    attempts += 1  # Never forget this!

# For loop approach
total = 0
for i in range(1, 6):
    total += i
print(f"For loop total: {total}")

# While loop approach
total = 0
current = 1
while current <= 5:
    total += current
    current += 1  # Manual update
print(f"While loop total: {total}")