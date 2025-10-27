age = (input("Enter your age : "))
ticket_price = (input("Enter the price of the movie ticket : "))

age = int 
ticket_price = float 

discount_category = ""
discount = 0
condition = ""

if(type(age) == str or type(ticket_price) == str):
    condition == "INVALID INPUT"
else:
    if((age <= 0 or ticket_price <= 0)):
        condition = "INVALID INPUT"
    else:
        if(age <= 12):
            discount_category = "Children"
            discount += 0.5
        elif(age >= 13 and age <= 17):
            discount_category = "Teenagers"
            discount += 0.25
        else:
            discount_category = "Adults"
            discount = discount
        
        price_after_discount = ticket_price - (ticket_price * discount)


        print(f"You are eligible for the {discount_category} discount ({discount*100:.0f}% off).")
        print(f"Discounted ticket price: ${price_after_discount:.2f}")

print(condition)

