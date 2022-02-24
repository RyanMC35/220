"""
Name: Ryan Campbell
hw6.py

Problem: Manipulate people's input to encode a word or message, and
using local scopes and arguments to compute a function.

Certification of Authenticity:I, Ryan Campbell, certify that this assignment is entirely
my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def cash_converter():
    number_ = eval(input("enter an integer"))
    print("This is ${}0".format(float(number_)))


def encode():
    message_ = input("enter a message:")
    key_ = eval(input("enter a key:"))
    length_ = len(message_)
    encoded_message = ""
    for i in range(length_):
        letter = message_[i]
        encode_ = ord(letter) + key_
        decode_ = chr(encode_)
        encoded_message = encoded_message + decode_
    print(encoded_message)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    summation = 0
    for i in range(1, number + 1):
        summation = summation + i
    return summation


def sum_n_cubes(number):
    summation = 0
    for i in range(1, number + 1):
        cubed_ = i ** 3
        summation = summation + cubed_
    return summation


def encode_better():
    message_ = input("enter a message:")
    key_ = input("enter a key:")
    length_key = len(key_)
    length_message = len(message_)
    encoded_message = ""
    for i in range(length_message):
        letter_message = message_[i]
        key_number = i % length_key
        letter_key = key_[key_number]
        encoded_letter_message = ord(letter_message) - 65
        encoded_letter_key = ord(letter_key) - 65
        combined_encoding = encoded_letter_key + encoded_letter_message
        encode_moved = (combined_encoding % 58) + 65
        decoded_ = chr(encode_moved)
        encoded_message = encoded_message + decoded_
    print(encoded_message)




if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
