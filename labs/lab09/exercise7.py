monthly_income = int(input("Enter your monthly income"))
employment_status = input("Enter your employment status")
credit_rating = input("Enter your creadit rating")
employment_years = int(input("Enter your employment years"))

# TODO: Your code here
criteria_met = 0

if(monthly_income >= 3000) :
    criteria_met += 1
if(employment_status == "permanent" or "contract") :
    criteria_met += 1
if(credit_rating == "good" or "excellent rating") :
    criteria_met += 1
if(employment_years >= 2) :
    criteria_met += 1
if(criteria_met == 4) :
    approval_status = "Approved"
elif(criteria_met == 3) :
    approval_status = "Conditionally"
else :
    approval_status = "Rejected"

print(approval_status)