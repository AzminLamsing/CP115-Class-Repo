main_course = input("Enter your main course : ")
drink = input("Enter your drink : ")
dessert = input("Enter your dessert : ")
customer_age = int(input("Enter your age : "))

# TODO: Your code here

if(main_course == "chicken") :
    price1 = 10
elif(main_course == "beef") :
    price1 = 12
elif(main_course == "fish") :
    price1 = 11
if(drink == "soft drink") :
    price2 = 2
elif(drink == "coffee") :
    price2 = 3
if(dessert == "ice cream") :
    price3 = 4
elif(dessert == "cake") :
    price3 = 5

total_price = price1 + price2 + price3
service_charge = total_price * 0.1
total_amount = total_price - service_charge

if(customer_age >= 60) :
    final_bill = total_amount - (total_amount * 0.15)
else :
    final_bill = total_amount
if(customer_age <= 18) :
    final_bill = total_amount - (total_amount * 0.1)
else :
    final_bill = total_amount



print(f"{final_bill:.2f}")