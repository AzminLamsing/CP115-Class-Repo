price = float(input("value : "))

# TODO: Your code here
count = 0
total = 0

while price >= 0 :
    total += price
    count += 1
    price = float(input("value : "))

item_count = count
total_cost = total            


print(item_count)
print(f"{total_cost:.2f}")
