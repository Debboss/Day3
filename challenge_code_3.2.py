print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?: "));

bill = 0;

if (height >= 120):
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: "))

    if (age < 12):
        bill = 5;
        print("Child tikctes 5$.")
    elif (age <= 18):
        bill = 7
        print("Youth tickets 7$.")
    else:
        bill = 12
        print("Adults tickets 12$.")

    wants_photo = input("Do you want a photo? Y/N");

    if(wants_photo == "Y"):
        bill += 3; # bill = bill + 3

    print(f"You final bill is: {bill}");


else:
    print("Sorry, you have to grow taller before you can ride.");