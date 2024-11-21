def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi, category = calculate_bmi(weight, height)
print(f"Your BMI value is {bmi:.2f} and you are '{category}'")
