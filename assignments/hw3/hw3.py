"""
Name: Ryan Campbell
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves,
in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    number_of_grades = eval(input("how many grades will you enter?:"))
    grade_sum = 0
    for i in range(number_of_grades):
        i = i + 1
        grade_value = eval(input("Enter grade:"))
        grade_sum = grade_sum + grade_value
    grade_average = grade_sum / number_of_grades
    print("average is", grade_average)


def tip_jar():
    tip_sum = 0
    for i in range(5):
        i = i + 1
        tip_ = eval(input("how much would you like to donate?:"))
        tip_sum = tip_sum + tip_
    print("total tips:", tip_sum)


def newton():
    number_to_sqrt = eval(input("What number do you want to square root?"))
    number_to_improve = eval(input("How many times should we improve the approximation?"))
    approximation = number_to_sqrt
    for i in range(number_to_improve):
        i = i + 1
        approximation = (approximation + (number_to_sqrt / approximation)) / 2
    print("the square root is approximately:", approximation)


def sequence():
    number_of_term = eval(input("how many terms would you like?:"))
    for i in range(1, number_of_term + 1):
        print((i - 1) + (i % 2))


def pi():
    number_of_terms = eval(input("How many terms in the series?"))
    total_denominator_ = 1
    total_numerator = 1
    for i in range(2, number_of_terms + 2):
        denominator_ = ((i - 1) + (i % 2))
        total_denominator_ = denominator_ * total_denominator_
    for j in range(1, number_of_terms + 1):
        numerator_ = ((j - 1) + (j % 2)) + 1
        total_numerator = numerator_ * total_numerator
    fraction_ = total_numerator / total_denominator_
    print(((round(fraction_, 20)) * 2))


if __name__ == '__main__':
    pass
