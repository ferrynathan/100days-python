# Write your code below this line 👇

def prime_checker(number):
    for divider in range(2, number):
        if number % divider == 0:
            print("This is not a prime number.")
            exit()
    print("This is a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
