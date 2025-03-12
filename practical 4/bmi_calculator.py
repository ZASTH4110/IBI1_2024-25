# Pseudocode:
# 1. Prompt the user to input their weight in kg.
# 2. Prompt the user to input their height in meters.
# 3. Convert the inputs into floating-point numbers for calculation.
# 4. Calculate BMI using the formula: BMI = weight / (height ** 2).
# 5. Use conditional statements to determine the BMI category:
#    - BMI < 18.5 → "Underweight"
#    - 18.5 ≤ BMI < 30 → "Normal weight"
#    - BMI ≥ 30 → "Obese"
# 6. Display the BMI result along with the category.


x = input("Enter your weight in kg: ")  # Get weight input
y = input("Enter your height in m: ")  # Get height input


w = float(x)
h = float(y)

bmi = w / (h ** 2)

if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 30:
    category = "normal weight"
else:
    category = "obese"

# Step 6: Print the result
print("Your BMI is " + str(round(bmi, 2)) + ", which means you are " + category + ".")
