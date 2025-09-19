# shopping_data.py
# This is your own module with useful data

# Product name
product1 = "Iphone"
product2 = "Bag"
product3 = "Laptop"

# Price information
price1 = 5999
price2 = 150
price3 = 2500

# Quantity information
bil1 = 10
bill2 = 233
bill3 = 70

# Calculations
totalcost1 = (price1 * bil1)
totalcost2 = (price2 * bill2)
totalcost3 = (price3 * bill3)

# shopping_data.py

import shopping_data

# Use variables from your own module
print("=== Using My Own Module ===")
print(f"Product_name: {shopping_data.product1}")
print(f"Price: {shopping_data.price1}")
print(f"quantity: {shopping_data.bil1}%")
print(f"totalcost: {shopping_data.totalcost1}")