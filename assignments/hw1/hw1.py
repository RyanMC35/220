"""
Name: Ryan Campbell
<hw1>.py

Problem: The point of this assignment is to test our understanding of how to set up simple
programs to compute simple equations.
Certification of Authenticity:I certify that this assignment is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume:", volume)


def shooting_percentage():
    total = eval(input("Enter  the player's total number of shots:"))
    made = eval(input("Enter how many shots the player made:"))
    percentage = (made / total) * 100
    print("Shooting Percentage:", percentage, "%")


def coffee():
    total = eval(input("How many pounds of coffee would you like:"))
    price = total * 10.50 + total * 0.86 + 1.50
    print("Your total is: $", price)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel"))
    miles = kilometers/1.61
    print("That's", miles, "miles")


if __name__ == '__main__':
    pass
