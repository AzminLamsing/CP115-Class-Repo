age = int(input("Enter your age : "))
accident_count = int(input("Enter your accident count : "))

# Your code here
if(age <= 25):
    base_premium = 2400
elif(age < 51 and age > 25):
    base_premium = 1800
else:
    base_premium = 2000

accident_count = 0

if(accident_count == 0):
    discount_amount = 0.9 
elif(accident_count <= 2):
    accidents = 300
else:
    accidents = 600

final_premium = base_premium + (accidents 



print(base_premium)
print(final_premium)
print(discount_amount)