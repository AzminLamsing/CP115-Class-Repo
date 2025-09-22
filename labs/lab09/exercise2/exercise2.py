employee_name = input("Enter your employee name : ")
base_salary = float(input("Enter your base salary : "))
overtime_hours = int(input("Enter your overtime hours : "))
tax_status = input("Enter your tax status : ")

# TODO your code here

EPF = 0.11
SOCSO = 0.005

total_income = (overtime_hours * 35) + base_salary

if(tax_status == "single") :
    if(total_income >= 5000) :
         tax_rate = 0.22 
    else :
         tax_rate = 0.18
elif(tax_status == "married") :
    if(total_income >= 6000) :
          tax_rate = 0.2
    else :
         tax_rate = 0.15
elif(tax_status == "head") :
    if(total_income >= 5500) :
          tax_rate = 0.25
    else :
         tax_rate = 0.19



net_salary = total_income - (total_income * (tax_rate + EPF + SOCSO))

print(f"EMPLOYEE NAME : {employee_name}")
print(f"TAX RATE : {tax_rate}")
print(f"NET SALARY :{net_salary:.2f}")