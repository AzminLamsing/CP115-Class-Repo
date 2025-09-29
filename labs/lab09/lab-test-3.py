#Azmin programmer 
#Determine the amount of bill payment every month user usage

#User given input
monthly_usage = int(input("Enter your monthly usage : "))

#Determine the total monthly usage based on input 
if(monthly_usage < 50) :
    discount = 0
elif(monthly_usage <= 100) :
    discount = 0.05
elif(monthly_usage > 100) :
    discount = 0.2


#calculate amount of the bill to be paid after receiving the discount
total_bill = monthly_usage + (monthly_usage * discount)
final_amount_bill = total_bill


#display  amount of the bill to be paid after receiving the discount
print(final_amount_bill)