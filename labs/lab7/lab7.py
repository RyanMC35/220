"""
Ryan Campbell
lab7.py
Problem Description -


"""
import graphics
from random import randint
import math
import time


def get_random(move_amt):
    move_amt_neg = -move_amt
    random_integer = randint(move_amt_neg, move_amt)
    return random_integer


def did_collide(ball, ball2):
    center_1 = ball.getCenter()
    center_2 = ball2.getCenter()
    x1 = center_1.getX()
    y1 = center_1.getY()
    x2 = center_2.getX()
    y2 = center_2.getY()
    radius_1 = ball.getRadius()
    radius_2 = ball.getRadius()
    real_distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return real_distance <= (radius_2 + radius_1)


def hit_vertical(ball, win):
    center_ = ball.getCenter()
    height_ = win.getHeight()
    y_ = center_.getY()
    radius_ = ball.getRadius()
    return y_ + radius_ >= height_ or y_ - radius_ <= 0


def hit_horizontal(ball, win):
    center_ = ball.getCenter()
    width_ = win.getWidth()
    x_ = center_.getX()
    radius_ = ball.getRadius()
    return 0 >= (x_ - radius_) or width_ <= (x_ + radius_)


def get_random_color():
    color_ = graphics.color_rgb(randint(0, 256), randint(0, 256), randint(0, 256))
    return color_


def bumper():
    win = graphics.GraphWin("Joyride", 500, 500)
    circle_1 = graphics.Circle(graphics.Point(randint(0, 500), randint(0, 500)), 25)
    circle_2 = graphics.Circle(graphics.Point(randint(0, 500), randint(0, 500)), 25)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    circle_1.draw(win)
    circle_2.draw(win)
    x1 = get_random(50)
    y1 = get_random(50)
    y2 = get_random(50)
    x2 = get_random(50)
    while not win.checkMouse():
        circle_1.move(x1, y1)
        circle_2.move(x2, y2)
        if did_collide(circle_1, circle_2):
            x1 = x1 * -1
            y1 = y1 * -1
            x2 = x2 * -1
            y2 = y2 * -1
        if hit_vertical(circle_1, win):
            y1 = y1 * -1
        if hit_vertical(circle_2, win):
            y2 = y2 * -1
        if hit_horizontal(circle_1, win):
            x1 = x1 * -1
        if hit_horizontal(circle_2, win):
            x2 = x2 * -1
        time.sleep(0.5)

    win.close()








