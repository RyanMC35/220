"""
Name: Ryan Campbell
lab13.py
Problem Description - list manipulation and creating sorting algorithms
I Ryan Campbell certify this assignment is entirely my own work.
"""


def trade_alert(file_name):
    input_file = open(file_name, 'r')
    line = input_file.readline().split(" ")
    i = 0
    for i in range(len(line)):
        second = i + 1
        if int(line[i]) == 500:
            print("alert: {} number of trades at second {}".format(line[i], second))
        elif int(line[i]) > 830:
            print("warning: {} number of trades at second {}".format(line[i], second))
        i = i + 1
    input_file.close()



