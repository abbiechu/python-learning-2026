weight = float(input("Enter weight (kg): "))
height = int(input("Enter height (cm): "))
h=height/100
bmi=weight/(h**2)
print("Your BMI is: ", round(bmi, 2))
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24:
    print("You have a normal weight.")
elif bmi < 27:
    print("You are overweight.")
else:
    print("You are obese.")