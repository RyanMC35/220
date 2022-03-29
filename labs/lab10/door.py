from graphics import *
"""
Name: Ryan Campbell
lab10.py
Problem Description - creating our own classes
I Ryan Campbell certify this assignment is entirely my own work.
"""


class Door:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def is_clicked(self, p):
        ux = p.getX()
        uy = p.getY()
        if (self.shape.getP1().getX() <= ux <= self.shape.getP2().getX()) and \
        (self.shape.getP1().getY() <= uy <= self.shape.getP2().getY()):
            return True
        else:
            return False

    def open(self, color, label):
        self.color_(color)
        self.set_label(label)

    def close(self, color, label):
        self.color_(color)
        self.set_label(label)

    def color_(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret




