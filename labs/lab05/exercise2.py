# Circle Calculator
import math
 
 #Getting user 

print("Please enter the radius")
radiuscircle =float(input())
circumference = 2 * math.pi * radiuscircle

print(str(circumference) + " cm")

areacircle = math.pi * pow(radiuscircle,2)

print(str(areacircle) + " cm2 ")