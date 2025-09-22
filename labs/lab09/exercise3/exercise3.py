day_type = input("Enter yaour day type : ")
show_time = int(input("Enter your time : "))
customer_type = input("Enter tour customer type : ")
is_student = input("Are you student? : ")

# TODO your code here

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
