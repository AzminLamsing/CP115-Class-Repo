day_type = input("Enter yaour day type : ")
show_time = int(input("Enter your time : "))
customer_type = input("Enter tour customer type : ")
is_student = input("Are you student? : ")

# Determine base price using separate if statements (no nesting)
base_price = 0

# Weekend Adult pricing
if day_type == "Weekend" and customer_type == "Adult":
    base_price = 18

# Weekend Child pricing  
if day_type == "Weekend" and customer_type == "Child":
    base_price = 12

# Weekend Senior pricing
if day_type == "Weekend" and customer_type == "Senior":
    base_price = 15

# Weekday Adult pricing
if day_type == "Weekday" and customer_type == "Adult":
    base_price = 15

# Weekday Child pricing
if day_type == "Weekday" and customer_type == "Child":
    base_price = 10

# Weekday Senior pricing
if day_type == "Weekday" and customer_type == "Senior":
    base_price = 12

# Start with base price as final price
final_price = base_price

# Apply evening surcharge (after 6pm = show_time > 18)
if show_time > 18:
    final_price = final_price + 3

# Apply student discount (10% off final price, weekdays only)
if day_type == "Weekday" and is_student == "Yes":
    final_price = final_price * 0.9

# Determine initial price based on day and customer type
if day_type == "Weekday":
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12
elif day_type == "Weekend":
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15
if show_time > 18:
    base_price = base_price + 3
else:
    base_price = base_price

final_price = float(base_price)

if (day_type == "Weekday" and is_student == "yes") :
    final_price = base_price * 0.9 
elif is_student == "no":
    final_price = base_price 



print(base_price)
print(final_price)
