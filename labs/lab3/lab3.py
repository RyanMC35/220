"""

Ryan Campbell
lab3.py
Problem Description - It is to create a program that will loop through and accumulate a series of information.
Certificate of Authenticity - I, Ryan Campbell, certify that this lab is entirely my own work.
"""


def traffic():
    number_of_roads = eval(input("How many roads were surveyed?"))
    total_number_of_vehicles = 0
    for i in range(number_of_roads):
        print("How many days was road", i + 1, "surveyed?")
        number_of_days = eval(input(""))
        total_number_of_vehicles_day = 0
        for j in range(number_of_days):
            print("\t How many cars traveled on day", j + 1, "?")
            number_of_vehicles = eval(input(""))
            total_number_of_vehicles_day = total_number_of_vehicles_day + number_of_vehicles
        total_number_of_vehicles = total_number_of_vehicles + total_number_of_vehicles_day
        print("Road", i + 1, "average vehicles per day:", (total_number_of_vehicles_day / number_of_days))
    print("Total number of vehicles traveled on all roads", total_number_of_vehicles)
    print("Average number of vehicles per road:", round((total_number_of_vehicles / number_of_roads), 2))
