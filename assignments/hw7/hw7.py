"""
Name: Ryan Campbell
hw7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import string


def number_words(in_file_name, out_file_name):
    in_file_name.read()
    split_ = in_file_name.split(" ")
    length_ = len(split_)
    for i in range(length_):
        number = i + 1
        word_ = split_[i]
        out_file_name = str(number) + " " + word_
    return out_file_name


def hourly_wages(in_file_name, out_file_name):
    in_file_name.readlines()
    split_ = str(in_file_name).split("/n")
    length_ = len(split_)
    for i in range(length_):
        employee_wage = split_[i]
        secondsplit_ = employee_wage.split(" ")
        employee = str(secondsplit_[0]) + str(secondsplit_[1])
        wage = float(secondsplit_[2]) * float(secondsplit_[3])
        wage_bonus = 1.65 * float(secondsplit_[3])
        total_wage = wage + wage_bonus
        combination_ = employee + str(total_wage)
        print(combination_, file=out_file_name)


# in_file_name = ('hourly_wages.txt', "r")
# out_file_name = ('hourly_wages.txt', "w")


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
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file_info = file_name
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
    pass
