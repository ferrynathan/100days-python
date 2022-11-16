year = int(input("Please enter the year you want to test for leap year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year !")
        else:
            print("Not a leap year !")
    else:
        print("It's a leap year !")
else:
    print("Not a leap year !")
