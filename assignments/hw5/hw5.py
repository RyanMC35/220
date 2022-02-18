"""
Name: Ryan Campbell
<hw5>.py

Problem: Manipulation of strings and lists to get a desired output.

Certification of Authenticity: I, Ryan Campbell, certify that this assignment is entirely
my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("enter you name (first, last):")
    split_names = name.split()
    print((split_names[1] + ","),  split_names[0])


def company_name():
    domain = input("Enter a domain:")
    split = domain.split('.')
    website_name = split[1]
    print(website_name)


def initials():
    user_input = eval(input("how many students are in the class?"))
    for i in range(user_input):
        name = input(("What is the name of student", i + 1))
        split_names = name.split()
        number_of_names = len(split_names)
        initial_ = ""
        for j in range(0, number_of_names):
            the_name = split_names[j]
            initial_ = initial_ + the_name[0]
        print(initial_)


def names():
    user_input = input("Enter a list of names:")
    separate_names = user_input.split(",")
    number_of_names = len(separate_names)
    initials_ = ""
    for i in range(0, number_of_names):
        name = separate_names[i]
        first_last = name.split()
        first_name = first_last[0]
        last_name = first_last[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        initials_ = initials_ + " " + (first_initial + last_initial)
    print(initials_.lstrip())


def thirds():
    number_of_sentences = eval(input("Enter number of sentences:"))
    third_letter_list = []
    for i in range(0, number_of_sentences):
        sentence = input(("enter the sentence:", i + 1))
        length_ = len(sentence)
        third_letter = ""
        for j in range(0, length_, 3):
            letter = sentence[j]
            third_letter = third_letter + letter
        third_letter_list.append(third_letter)
    for let in third_letter_list:
        print(let)


def word_average():
    sentence = input("enter a sentence:")
    words = sentence.split()
    number_of_words = len(words)
    length_of_word_total = 0
    for i in range(0, number_of_words):
        word = words[i]
        length_of_word = len(word)
        length_of_word_total = length_of_word + length_of_word_total
    print(length_of_word_total / number_of_words)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin:")
    separate_words = sentence.split()
    number_of_words = len(separate_words)
    plus_ay = ''
    for i in range(number_of_words):
        word = separate_words[i]
        first_letter = word[0]
        ending_word = word[1: ]
        changed_word = ending_word + first_letter
        ay_ending = "ay"
        plus_ay = plus_ay + " " + (changed_word + ay_ending)
    print((plus_ay.lower()).lstrip())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
