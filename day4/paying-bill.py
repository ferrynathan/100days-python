# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
print("Le nombre de prénom est " + str(len(names)))
random_int = random.randint(0, len(names))
print(f"{names[random_int]} is going to buy the meal today!")
