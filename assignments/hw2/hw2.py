"""
Name: Ryan Campbell
<hw2>.py

Problem: The purpose of this assignment is to set up program that will
accumulate and compute a user's input
Certification of Authenticity: I certify that this assignment is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?:"))
    sum_threes = 0
    for i in range(3, upper_bound + 1, 3):
        sum_threes = sum_threes + i
    print("sum of threes is", sum_threes)


def multiplication_table():
    for i in range(10):
        for j in range(10):
            product = (i + 1) * (j + 1)
            print(product, end="/t")


def triangle_area():
    side_a = eval(input("What is the length of side a?:"))
    side_b = eval(input("What is the length of side b?:"))
    side_c = eval(input("What is the length of side c?:"))
    sides = (side_a + side_b + side_c) / 2
    area = math.sqrt(sides * (sides - side_a) * (sides - side_b) * (sides - side_c))
    print("The area of the triangle is:", area)


def sum_squares():
    lower_range = eval(input("Enter the lower range?:"))
    upper_range = eval(input("Enter the upper range?:"))
    square_sum = 0
    for i in range(lower_range, upper_range + 1):
        square = i * i
        square_sum = square_sum + square
    print(square_sum)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    base_product = 1
    for i in range(exponent):
        i = i + 1
        base_product = base * base_product
        print(base, "^", exponent, "=", base_product)


if __name__ == '__main__':
    pass
