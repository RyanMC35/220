"""
Name: Ryan Campbell
hw7.py

Problem: To use files in order to obtain information that can be edited and returned to that file
or sent to another file.

Certification of Authenticity: I, Ryan Campbell, certify that this assignment is
entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import encryption


def number_words(in_file_name, out_file_name):
    infile_ = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w')
    file_ = infile_.read()
    nolines = (file_.replace("\n", " ")).rstrip()
    seperateword = nolines.split(" ")
    for i in range(len(seperateword)):
        combo = str(i + 1) + " " + seperateword[i]
        print(combo, file=outfile)


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w')
    for line in infile.readlines():
        split_ = line.split(" ")
        employee_ = split_[0] + " " + split_[1]
        pay_week = (float(split_[2]) + 1.65) * float(split_[3])
        decimal_dollar = str(pay_week).split(".")
        dollar = decimal_dollar[0]
        change_ = decimal_dollar[1]
        total = "{}.{:0<2}".format(dollar, change_)
        two_decimals = "{0:.2f}".format(float(total))
        out_line = employee_ + " " + two_decimals
        print(out_line, file=outfile)


def calc_check_sum(isbn):
    isbn_mod = isbn.replace("-", "")
    length_ = len(isbn_mod)
    product_isbn = 0
    for i in range(length_):
        isbn_number = int(isbn_mod[i])
        multiplier = (length_ - i)
        final_isbn_number = isbn_number * multiplier
        product_isbn = product_isbn + final_isbn_number
    return product_isbn


def send_message(file_name, friend_name):
    file_ = open(file_name, "r")
    friend_txt = friend_name + ".txt"
    friendfile = open(friend_txt, 'w')
    infor = file_.read()
    print(infor.rstrip(), file=friendfile)


def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, 'r')
    friend_txt = friend_name + ".txt"
    friendfile = open(friend_txt, 'w')
    total_encrypted = ""
    for line in infile.readlines():
        encrypted_line = encryption.encode(line.rstrip(), key)
        total_encrypted = total_encrypted + encrypted_line + "\n"
    print(total_encrypted.rstrip(), file=friendfile)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    infile = open(file_name, 'r')
    padfile = open(pad_file_name, 'r')
    friend_txt = friend_name + ".txt"
    friendname = open(friend_txt, 'w')
    print(encryption.encode_better(infile.read(), padfile.read()), file=friendname)


if __name__ == '__main__':
    pass
