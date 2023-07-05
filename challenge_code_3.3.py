print("Welcome to the rollercoaster!")

while True:
    height = input("What is your height in cm?: ")
    if height.isdigit():
        height = int(height)
        if height >= 120:
            break
        else:
            print("Sorry, you have to grow taller before you can ride.")
    else:
        print("Invalid input! Please enter a valid height.")

bill = 0

print("You can ride the rollercoaster")
while True:
    age = input("What is your age?: ")
    if age.isdigit():
        age = int(age)
        if age < 12:
            bill = 5
            print("Child tickets $5.")
            break
        elif age <= 18:
            bill = 7
            print("Youth tickets $7.")
            break
        else:
            bill = 12
            print("Adult tickets $12.")
            break
    else:
        print("Invalid input! Please enter a valid age.")

while True:
    wants_photo = input("Do you want a photo? (Y/N): ")
    if wants_photo == "Y" or wants_photo == "N":
        if wants_photo == "Y":
            bill += 3
        break
    else:
        print("Invalid input! Please enter Y for yes or N for no.")

print(f"Your final bill is: ${bill}")
