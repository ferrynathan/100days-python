# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

total_heights = 0
number_heights = 0

print(student_heights)
for height in student_heights:
    total_heights += height
    number_heights += 1
average_height = round(total_heights / number_heights)
print(f"The average height is {average_height}")
