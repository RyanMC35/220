"""
Name: Ryan Campbell
lab12.py
Problem Description -writing functions without using for loops,
list manipulation, and performing linear searches
I Ryan Campbell certify this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(lists, value):
    location = lists.index(value)
    lists.remove(value)
    lists.insert(location, "ryan")


def good_input():
    user_input = input("enter a number:")
    while not (1 <= eval(user_input) <= 10):
        if eval(user_input) < 1:
            print("number is to low")
            user_input = input("enter a number:")
        elif eval(user_input) > 10:
            print("number is to high")
            user_input = input("enter a number:")
    return eval(user_input)


def num_digits():
    user_input = eval(input("enter a number (enter 0 or negative number to end):"))
    while user_input > 0:
        number_of_digits = 0
        divided_number = user_input
        while divided_number != 0:
            divided_number = divided_number // 10
            number_of_digits += 1
        print("number of digits: {}". format(number_of_digits))
        user_input = eval(input("enter a number (enter 0 or negative number to end):"))


def hi_lo_game():
    random_number = randint(1, 100)
    user_guess = 1
    user_input = input("enter a number:")
    while user_guess != 7 and eval(user_input) != random_number:
        if eval(user_input) > random_number:
            print("your guess is too high")
            user_guess += 1
        elif eval(user_input) < random_number:
            print("your guess is too low")
            user_guess += 1
        user_input = input("enter a number:")
    if eval(user_input) == random_number:
        print("You win in {} guesses".format(user_guess))
    else:
        print("Sorry you lose. The number was {}".format(random_number))



