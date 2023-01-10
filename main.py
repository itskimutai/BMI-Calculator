# BMI Calculator
height = float(input("Please enter your height (in meters): "))
weight = int(input("Please enter your weight (in kgs): "))
BMI = weight / (height * height)
newBMI = round(BMI)
print(newBMI)