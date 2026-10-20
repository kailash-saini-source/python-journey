#Ask weight (kg) and height (m). Print the BMI with 1 decimal and the
#category: under 18.5 Underweight, under 25 Normal, under 30 Overweight, otherwise Obese.
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi:.1f}")
print(f"Category: {category}")