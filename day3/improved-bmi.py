# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = float(weight) / float(height) ** 2
rounded_bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your bmi is {rounded_bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your bmi is {rounded_bmi}. You are normal.")
elif bmi < 30:
    print(f"Your bmi is {rounded_bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your bmi is {rounded_bmi}. You are obese.")
else:
    print(f"Your bmi is {rounded_bmi}. You are clinically obese")
