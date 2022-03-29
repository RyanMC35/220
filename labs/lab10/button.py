from graphics import *
"""
Name: Ryan Campbell
lab10.py
Problem Description - creating our own classes.
I Ryan Campbell certify this assignment is entirely my own work.
"""


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw_win(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, p):
        ux = p.getX()
        uy = p.getY()
        if (self.shape.getP1().getX() <= ux <= self.shape.getP2().getX()) and \
                (self.shape.getP1().getY() <= uy <= self.shape.getP2().getY()):
            return True
        else:
            return False

    def color_button(self):
        self.shape.setFill(color_rgb(0, 0, 0))

