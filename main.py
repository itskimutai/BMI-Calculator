# BMI Calculator V 2.0
height = float(input("Please enter your height (in meters): "))
weight = float(input("Please enter your weight (in kgs): "))
BMI = weight / (height * height)
newBMI = round(BMI, 1)

if newBMI < 18.5:
    print("You are underweight")
elif newBMI <= 25:
    print("Your weight is normal")
elif newBMI <= 30:
    print("YOur are overweight")
elif newBMI <= 35:
    print("You are obese")
else:
    print("You are clinically obese")