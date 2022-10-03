#purpose: to show the calender of a specific year and specific month in that year given by the user

#Updates
    #1. 2022-10-03 18:52:19 : Started this project


def bodymassindex(height, weight):
    return round((weight/height**2),2)


#height and weight (user input)
H = float(input("What is your current height? (in meters): "))
W = float(input("What is your current weight? (in kilograms): "))

#just to give it a little proceessing effect
print("processing...")
import time
time.sleep(2)

print("--------------------")

#Prints Body mass index
bmi = bodymassindex(H, W)
print("your BMI (Body Mass Index) is ", bmi)

print("--------------------")

#prints wether ur unerweight, normal or fat
if bmi <= 18.5:
    print("It seems that you are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight seems pretty normal... keep it up.")
elif 25 < bmi <= 24.9:
    print("You are overweight.")
else:
    print("You are just obese.")

print("--------------------")



