# ð¨ Don't change the code below ð
row1 = ["â¬ï¸", "ï¸â¬ï¸", "ï¸â¬ï¸"]
row2 = ["â¬ï¸", "â¬ï¸", "ï¸â¬ï¸"]
row3 = ["â¬ï¸ï¸", "â¬ï¸ï¸", "â¬ï¸ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

# Write your code below this row ð

column_number = int(position[0])
line_number = int(position[1])

if line_number >= 1 and line_number < 4:
    if column_number >= 1 and column_number < 4:
        map[line_number - 1][column_number - 1] = 'X'
    else:
        print("NumÃ©ro de colonne incorrect!")
else:
    print("NumÃ©ro de ligne incorrect!")


# Write your code above this row ð

# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")
