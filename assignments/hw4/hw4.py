"""
Name: Ryan Campbell
<hw4>.py

Problem: Use graphics to create objects using user entries, and computing size of objects of shapes
created by user entry.

Certification of Authenticity:I, Ryan Campbell, certify that this assignment is entirely
my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import graphics
from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(175, 175), Point(225, 225))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle

    for i in range(num_clicks):
        i = i + 1
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape = shape.clone()
        shape.draw(win)
        shape.move(change_x, change_y)

    inst_pt = Point(width / 2, height - 250)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 700, 700)
    user_input_1 = win.getMouse()
    first_x = user_input_1.getX()
    first_y = user_input_1.getY()
    user_input_2 = win.getMouse()
    second_x = user_input_2.getX()
    second_y = user_input_2.getY()
    shape_ = Rectangle(Point(first_x, first_y), Point(second_x, second_y))
    shape_.setFill("green")
    shape_.draw(win)
    perimeter = ((abs(first_x - second_x) * 2) + (abs(first_y - second_y) * 2))
    area = ((abs(first_x - second_x)) * (abs(first_y - second_y)))
    text_perimeter = Text(Point(325, 400), "Perimeter:")
    number_perimeter = Text(Point(390, 400), perimeter)
    text_area = Text(Point(325, 425), "Area:")
    number_area = Text(Point(375, 425), area)
    text_area.draw(win)
    text_perimeter.draw(win)
    number_perimeter.draw(win)
    number_area.draw(win)
    click_to_close = Text(Point(350, 350), "Click to Close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 700, 700)
    user_input_one = win.getMouse()
    center_x = user_input_one.getX()
    center_y = user_input_one.getY()
    user_input_two = win. getMouse()
    second_x = user_input_two.getX()
    second_y = user_input_two.getY()
    difference_of_xs = (second_x - center_x) ** 2
    difference_of_ys = (second_y - center_y) ** 2
    square_root_ = (difference_of_xs + difference_of_ys) ** (1/2)
    image = Circle(Point(center_x, center_y), square_root_)
    image.setFill("light blue")
    image.draw(win)
    radius_ = square_root_
    text_radius_ = Text(Point(247.5, 550), "Radius:")
    text_radius_.draw(win)
    number_radius = Text(Point(352.5, 550), radius_)
    number_radius.draw(win)
    click_to_close = Text(Point(350, 350), "Click to Close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()


def pi2():
    number_of_terms = eval(input("enter the number of terms to sum:"))
    terms_ = number_of_terms * 2
    numerator = 4
    fraction = 0
    modifier = 1
    for i in range(2, terms_ + 1, 2):
        denominator_ = ((i - 1) + (i % 2))
        modified = (numerator / denominator_) * modifier
        fraction = fraction + modified
        modifier = modifier * (-1)
    pi_approximation = fraction
    accuracy = math.pi - pi_approximation
    print("pi_approximation", pi_approximation)
    print("accuracy:", accuracy)


if __name__ == '__main__':
    pass
