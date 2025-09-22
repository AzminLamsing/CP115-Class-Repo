student_gpa = float(input("Enter your gpa : "))
total_score = int(input("Enter your total score : "))
number_extracurricular = int(input("Enter your number extracurricular : "))
completed_interview = input("Enter your interview : ")

# TODO: Your code here

if(student_gpa >= 3.0) :
    requirements_met1 = 1
if(total_score >= 1200) :
    requirements_met2 = 1
if(number_extracurricular >= 1) :
    requirements_met3 = 1
if(completed_interview.lower() == "yes") :
    requirements_met4 = 1

total_requirements_met = (requirements_met1 + requirements_met2 + requirements_met3 + requirements_met4)
if(total_requirements_met == 4) :
    admission_status = "Accepted"
elif(total_requirements_met == 3) :
    admission_status = "Waitlisted"
else :
    admission_status = "Rejected"

print(admission_status)