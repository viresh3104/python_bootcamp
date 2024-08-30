# BMI Calculator

# Taking user input for weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Taking user input for height in meters
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Displaying the BMI result
print(f"Your BMI is: {bmi:.2f}")

# Interpreting the BMI result
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
