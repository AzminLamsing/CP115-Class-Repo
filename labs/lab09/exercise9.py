applicant_age = int(input("Enter your age : "))
vision_test = input("Enter your vision test : ")
written_score = int(input("Enter your written score : "))
driving_score = int(input("Enter your driving score : "))
medical_clearance = input("Enter your medical clearance : ")

# TODO: Your code here
requirements_met = 0

if(applicant_age >= 21) :
    requirements_met += 1
elif(applicant_age >= 18) :
    requirements_met += 1
if(vision_test == "Must pass") :
    requirements_met += 1
if(written_score >= 0.8) :
    requirements_met += 1
if(driving_score >= 0.85) :
    requirements_met += 1
if(medical_clearance == "Must pass") :
    requirements_met += 1

if(requirements_met == 5 and applicant_age >= 21) :
    license_class = "Class A"
elif(requirements_met == 4 and applicant_age >= 18) :
    license_class = "Class B"
elif(requirements_met >= 2) :
    license_class = "Restricted License"
else :
    license_class = "Application Denied"

print(license_class)