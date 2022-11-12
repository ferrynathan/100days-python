# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

rem_years = 90 - int(age)
rem_months = rem_years * 12
rem_weeks = rem_years * 52
rem_days = rem_years * 365
print(
    f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.")
