height = int(input("What is your height? "))
weight = int(input("What is your weight? "))
h=height/100
bmi=weight/h**2
print("Your BMI is", round(bmi, 2))
if bmi<18.5:
    print("You are underweight.")
elif bmi<25:
    print("You have a normal weight.")
elif bmi<30:
    print("You are overweight.")
else:
    print("You are obese.")
