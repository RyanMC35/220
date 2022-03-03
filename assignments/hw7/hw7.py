"""
Name: Ryan Campbell
hw7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity: I, Ryan Campbell, certify that this assignment is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import string
import encryption


def number_words(in_file_name, out_file_name):
    in_file_name.read()
    split_ = in_file_name.split("/n")
    second_split_ = [split_.split(" ")]
    length_ = len(split_)
    for i in range(length_):
        number = i + 1
        word_ = second_split_[i]
        combination_ = str(number) + " " + word_
        print(combination_, file=out_file_name)


def hourly_wages(in_file_name, out_file_name):
    file_ = open(in_file_name, 'w')
    for line in file_.readlines():
        split_ = line.split(" ")
        employee_ = split_[0] + split_[1]
        pay_ = split_[2]
        hours_ = split_[3]
        pay_week = float(pay_) * float(hours_)
        bonus_ = 1.65 * float(hours_)
        total_pay = bonus_ + pay_week
        out_line = employee_ + " " + str(total_pay)
        print(out_line, file=out_file_name)


def calc_check_sum(isbn):
    isbn_mod = isbn.replace("-", "")
    length_ = len(isbn_mod)
    product_isbn = 0
    for i in range(length_):
        isbn_number = int(isbn_mod[i])
        multiplier = (length_ - i)
        final_isbn_number = isbn_number * multiplier
        product_isbn = product_isbn + final_isbn_number
    print(product_isbn)


def send_message(file_name, friend_name):
    file_ = open(file_name, "r")
    new_file = friend_name.txt
    print(file_, file=new_file)


def encode(message_, key_):
    length_ = len(message_)
    encoded_message = ""
    for i in range(length_):
        letter = message_[i]
        encode_ = ord(letter) + key_
        decode_ = chr(encode_)
        encoded_message = encoded_message + decode_
    return encoded_message


def send_safe_message(file_name, friend_name, key):
    file_ = file_name.read()
    length_ = len(file_)
    encoded_message = ""
    for i in range(length_):
        letter = file_[i]
        encode_ = ord(letter) + key
        decode_ = chr(encode_)
        encoded_message = encoded_message + decode_
    print(encoded_message, file=friend_name.txt)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    print(encode(file_name.read(), pad_file_name.read()), file=friend_name.txt)


if __name__ == '__main__':
    pass
