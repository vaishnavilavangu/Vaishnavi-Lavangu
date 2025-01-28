print("BMI Calculater")
def calculate_bmi(w, h):#declaring a function that calculates BodyMassIndex
    bmi = w / (h ** 2)#BMI formula 
    return bmi
#Input weight and Height values
w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))
bmi_val = calculate_bmi(w, h)#function call

if bmi_val < 18.5:
    category = "Underweight" #prints underweight if bmi val is less than 18.5
elif 18.5 <= bmi_val< 24.9:
    category = "Normal" #prints Normal if bmi val is less than 24.5 and greater than 18.5
elif 25 <= bmi_val < 29.9:
    category = "Overweight" #prints Overweight if bmi val is less than 18.5
else:
    category = "Obese" #if none of the conditions it falls then it prints as obese

print(f"Your BMI is: {bmi_val:.2f}")#to print bmi value in 2 decimals
print(f"Category: {category}")#prints the category into which the BMI value falls into
