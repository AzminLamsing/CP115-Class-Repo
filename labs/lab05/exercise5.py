#Shopping Cost Calculator

#Getting input from user
item1 = input("enter your item1 name")
price1 = float(input("enter your item1 price"))
item2 = input("enter your item2 name")
price2 = float(input("enter your item2 price"))
item3 = input("enter your item3 name")
price3 = float(input("enter your item3 price"))
 
quantity = 3 
taxrate = 0.06

subtotal = price1 + price2 + price3 
taxamount = subtotal * taxrate
totalcost = subtotal * taxamount 

print("You have buy" , item1 , item2 , item3)
print("price of "  , subtotal)
print("taxamount" , taxamount)
print("totalcost" , totalcost)