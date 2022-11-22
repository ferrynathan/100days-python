# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

column_number = int(position[0])
line_number = int(position[1])

if line_number >= 1 and line_number < 4:
    if column_number >= 1 and column_number < 4:
        if line_number == 1:
            row1[column_number - 1] = 'X'
        elif line_number == 2:
            row2[column_number - 1] = 'X'
        elif line_number == 3:
            row3[column_number - 1] = 'X'
    else:
        print("Numéro de colonne incorrect!")
else:
    print("Numéro de ligne incorrect!")


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
