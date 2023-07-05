print("Welcome to the Leap Calculator")

year = int(input("Give a year that you want to check: "))

check_a = year % 4
check_b = year % 100
check_c = year % 400

if (check_a == 0 and check_b != 0) or check_c == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
