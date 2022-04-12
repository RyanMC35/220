"""
Name: Ryan Campbell
lab12.py
Problem Description - writing functions without using for loops,
list manipulation, and performing linear searches
I Ryan Campbell certify this assignment is entirely my own work.
"""


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



