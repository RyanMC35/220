"""
Name: Ryan Campbell
lab13.py
Problem Description - list manipulation and creating sorting algorithms
I Ryan Campbell certify this assignment is entirely my own work.
"""
from graphics import *


def read_data(file_name):
    file_ = open(file_name, "r")
    values = []
    line = file_.readline()
    while line != "":
        i = 0
        split_values = line.rstrip().split(" ")
        while i < len(split_values):
            values.append(eval(split_values[i]))
            i += 1
        line = file_.readline()
        print(1)
    return values


def is_in_linear(search_val, values):
    index_value = 0
    while index_value < len(values):
        if search_val == values[index_value]:
            return True
        index_value += 1
    return False


def selection_sort(values):
    start = 0
    while start < len(values):
        minimum = values[start]
        for i in range(start, len(values)):
            if values[i] < minimum:
                minimum = values[i]
        minimum_index = values.index(minimum)
        a = values[minimum_index]
        values[minimum_index] = values[start]
        values[start] = a
        start += 1


def calc_area(rect):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    length = abs(point_1.getX() - point_2.getX())
    width = abs(point_1.getY() - point_2.getY())
    area = length * width
    return area


def rectangle_sort(rectangles):
    rectangles.sort(key=calc_area)

