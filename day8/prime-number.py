# Write your code below this line ๐

def prime_checker(number):
    for divider in range(2, number):
        if number % divider == 0:
            print("It's not a prime number.")
            exit()
    print("It's a prime number.")


# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
