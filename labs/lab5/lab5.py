"""
Ryan Campbell
lab5.py
Problem Description - Use graphics to create shapes using user input, and
use user_input for shapes to do computation. Also using strings and lists to produce outputs.
Certificate of Authenticity - I, Ryan Campbell, certify that this lab is entirely my own work.


"""
import graphics
from graphics import *

def triange():
    win = GraphWin("Circle", 700, 700)
    win.setCoords(0, 0, 10, 10)
    instructions = Text(Point(5, 5), "Click three times to create triangle:")
    instructions.draw(win)
    user_input_one = win.getMouse()
    first_x = user_input_one.getX()
    first_y = user_input_one.getY()
    user_input_two = win.getMouse()
    second_x = user_input_two.getX()
    second_y = user_input_two.getY()
    user_input_three = win.getMouse()
    third_x = user_input_three.getX()
    third_y = user_input_three.getY()
    triangle = Polygon(Point(first_x, first_y), Point(second_x, second_y), Point(third_x, third_y))
    triangle.setFill("green")
    triangle.draw(win)
    dx1 = abs(first_x - second_x)
    dy1 = abs(first_y - second_y)
    a = (((dx1 ** 2) + (dy1 ** 2)) ** (1/2))
    dx2 = abs(second_x - third_x)
    dy2 = abs(second_y - third_y)
    b = (((dx2 ** 2) + (dy2 ** 2)) ** (1/2))
    dx3 = abs(third_x - first_x)
    dy3 = abs(third_y - first_y)
    c = (((dx3 ** 2) + (dy3 ** 2)) ** (1/2))
    perimeter = a + b + c
    s = perimeter / 2
    area = ((s * (s - a) * (s - b) * (s - c)) ** (1/2))
    text_perimeter = Text(Point(5, 7), ("Perimeter", perimeter))
    text_perimeter.draw(win)
    textarea = Text(Point(5, 7.5), ("Area:", area))
    textarea.draw(win)
    click_to_close = Text(Point(5, 6), "Click to Close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry_box = Entry(Point(225, 240), 10)
    red_entry_box.draw(win)
    green_entry_box = Entry(Point(225, 270), 10)
    green_entry_box.draw(win)
    blue_entry_box = Entry(Point(225, 300), 10)
    blue_entry_box.draw(win)
    for i in range(5):
        win.getMouse()
        red_entry = eval(red_entry_box.getText())
        green_entry = eval(green_entry_box.getText())
        blue_entry = eval(blue_entry_box.getText())
        win.getMouse()
        shape.setFill(color_rgb(red_entry, green_entry, blue_entry))


    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_input = input("Enter a string:")
    first_character = user_input[0]
    print(first_character)
    last_character = user_input[-1]
    print(last_character)
    two_five = user_input[2: 6]
    print(two_five)
    concatenation = first_character + last_character
    print(concatenation)
    first_three = user_input[0: 3]
    print(first_three * 10)
    number_of_characters = len(user_input)
    for i in range(number_of_characters):
        print(user_input[i])
    print(number_of_characters)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2" ]
    x1 = values[1] + values[3]
    print(x1)
    x21 = values[0]
    x22 = values[2]
    print(x21 + x22)
    x3 = values[1] + values[1] + values[1] + values[1] + values[1]
    print(x3)
    x41 = values[2]
    x42 = values[3]
    x43 = values[4]
    x4_list = [x41, x42, x43]
    print(x4_list)
    x51 = values[2]
    x52 = values[3]
    x53 = values[0]
    x5_list = [x51, x52, x53]
    print(x5_list)
    x61 = values[2]
    x62 = values[0]
    x63 = float(values[5])
    x6_list = [x61, x62, x63]
    print(x6_list)
    x71 = values[2]
    x72 = values[0]
    x73 = float(values[5])
    print(x71 + x72 + x73)
    number_of_item_list = len(values)
    print(number_of_item_list)


def another_series():
    n = eval(input("Enter number of terms:"))
    number = n * 2
    total = 0
    for i in range(0, number * 2, 2):
        term = i % 6
        total = total + term
    print("sum =", total)


def target():
    win = GraphWin("Target", 400, 400)
    win.setCoords(0, 0, 10, 10)
    big_circle = Circle(Point(5, 5), 5)
    big_circle.setFill("white")
    big_circle.setOutline("white")
    big_circle.draw(win)
    second_circle = Circle(Point(5, 5), 4)
    second_circle.setFill("black")
    second_circle.setOutline("black")
    second_circle.draw(win)
    third_circle = Circle(Point(5, 5), 3)
    third_circle.setFill("blue")
    third_circle.setOutline("blue")
    third_circle.draw(win)
    fourth_circle = Circle(Point(5, 5), 2)
    fourth_circle.setFill("red")
    fourth_circle.setOutline("red")
    fourth_circle.draw(win)
    center_circle = Circle(Point(5, 5), 1)
    center_circle.setFill("yellow")
    center_circle.setOutline("yellow")
    center_circle.draw(win)
    click_to_close = Text(Point(5,5), "Click to Close")
    click_to_close.setOutline("lime green")
    click_to_close.draw(win)
    win.getMouse()
    win.close()
