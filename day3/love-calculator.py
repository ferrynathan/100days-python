# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name_composed = (name1 + name2).lower()

# Test for true

t = int(name_composed.count('t'))
r = int(name_composed.count('r'))
u = int(name_composed.count('u'))
e = int(name_composed.count('e'))

true_score = t + r + u + e

# Test for love

l = int(name_composed.count('l'))
o = int(name_composed.count('o'))
v = int(name_composed.count('v'))
e = int(name_composed.count('e'))

love_score = l + o + v + e

combined_score = int(str(true_score) + str(love_score))

if combined_score < 10 or combined_score > 90:
    print(
        f"Your score is {combined_score}, you go together like coke and mentos.")
elif combined_score >= 40 and combined_score <= 50:
    print(f"Your score is {combined_score}, you are alright together.")
else:
    print(f"Your score is {combined_score}.")
