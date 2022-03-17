"""
Name: Ryan Campbell
hw8.py

Problem: Modify items in a lists, use conditional statements to determine boolean values
of a set of input data, and modify code in order to test for overlapping of graphics items.

Certification of Authenticity: I, Ryan Campbell, certify this assignment is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math
from graphics import GraphWin, Circle, Text, Point


def add_ten(nums):
    list_ = nums
    length_ = len(nums)
    for i in range(length_):
        list_[i] = int(list_[i] + 10)


def square_each(nums):
    length_ = len(nums)
    for i in range(length_):
        nums[i] = float(nums[i]) ** 2
    return nums


def sum_list(nums):
    length_ = len(nums)
    total_ = 0
    for i in range(length_):
        total_ = total_ + nums[i]
    return total_


def to_numbers(nums):
    length_ = len(nums)
    for i in range(length_):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    length1 = len(nums)
    for i in range(length1):
        nums[i] = nums[i].split(",")
        to_numbers(nums[i])
        squared_ = square_each(nums[i])
        sum_list_ = sum_list(squared_)
        nums[i] = sum_list_
    return nums


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    division_ = year / 4
    string_ = str(division_)
    split_ = string_.split(".")
    decimal_ = split_[1]
    division_2 = year / 100
    string_2 = str(division_2)
    split_2 = string_2.split(".")
    decimal_2 = split_2[1]
    division_3 = year / 400
    string_3 = str(division_3)
    split_3 = string_3.split(".")
    decimal_3 = split_3[1]
    if int(decimal_) == 0 and int(decimal_2) != 0:
        return True
    elif int(decimal_3) == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 +
        (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 +
        (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill('light green')
    circle_two.draw(win)
    text1 = Text(Point(5, 5), "The circles overlap")
    text2 = Text(Point(5, 5), "The circles don't overlap")
    text3 = Text(Point(5, 6), "Click to close")
    if did_overlap(circle_one, circle_two):
        text1.draw(win)
        text3.draw(win)
    else:
        text2.draw(win)
        text3.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    center_1 = circle_one.getCenter()
    center_2 = circle_two.getCenter()
    x_1 = center_1.getX()
    y_1 = center_1.getY()
    x_2 = center_2.getX()
    y_2 = center_2.getY()
    distance = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    sum_of_radius = circle_one.getRadius() + circle_two.getRadius()
    return distance <= sum_of_radius


if __name__ == '__main__':
    pass
