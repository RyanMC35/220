"""
Name: Ryan Campbell
lab10.py
Problem Description - creating our own classes.
I Ryan Campbell certify this assignment is entirely my own work.
"""
import graphics

from button import Button
from door import Door


def main():
    win = graphics.GraphWin("Test", 500, 500)
    button_rectangle = graphics.Rectangle(graphics.Point(150, 75), graphics.Point(350, 150))
    button = Button(button_rectangle, "exit")
    button.draw_win(win)
    door_rectangle = graphics.Rectangle(graphics.Point(150, 200), graphics.Point(350, 450))
    door_text = graphics.Text((button_rectangle.getCenter()), "Close")
    door = Door(door_rectangle, door_text)
    door.close("red", "Close")
    door.draw(win)
    number = 0
    user_click = win.getMouse()
    while not button.is_clicked(user_click):
        if door.is_clicked(user_click) and (number % 2) == 0:
            door.open("white", "Open")
            number = number + 1
        elif door.is_clicked(user_click) and (number % 2) == 1:
            door.close("red", "Close")
            number = number + 1
        user_click = win.getMouse()
    win.close()

