print("Hello"[2])
print(123 + 456)

# les _ sont ignorés mais rendent plus lisibles
print(123_456 + 789_123_433)

# Float

13.232

# Boolean
True
False

# Get type

num_char = len(input("What is your name ? "))
print(type(num_char))
new_num_char = str(num_char)
print(type(new_num_char))
print("I see your name has " + new_num_char + " characters !")

# jouer avec les types

print(70 + float("123.4"))
print(str(70) + str(30))

#
print(6 * 3)
print(int(6 / 2))
print(2 ** 3)

# Order
# PEMDAS
# Parentheses
# Exposant
# Multiplication
# Division
# Addition
# Soustraction

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
