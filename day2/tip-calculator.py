# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# ask for inputs
print("Welcome to the tip calculator.")
total = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))
people = int(input("How many people to split the bill ?"))

# calculate
total_with_tip = total + (total * (tip / 100))
#total_with_tip_splitted = round(total_with_tip / people, 2)
# Ici le formattage permet de mettre 2 décimales apres la virgule meme si la 2eme est à 0
total_with_tip_splitted = "{:.2f}".format(total_with_tip / people)

# print result
print(
    f"The total to pay with tip is ${total_with_tip}. With {people} people, each have to pay ${total_with_tip_splitted}.")
