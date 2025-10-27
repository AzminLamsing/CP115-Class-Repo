# TODO: Your code here
found_number = None

for i in range (1,101):

    if (i % 7 == 0 and i % 13 == 0) :
        found_number = i
        break


print(found_number)
