"""
Name: Ryan Campbell
hw9.py
Problem: to use functions to create a command line and graphical hang man game
Certification of Authenticity: I, Ryan Campbell, certify this assignment
is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>


"""
from random import randint
import graphics


def get_words(file_name):
    in_file = open(file_name, "r")
    words = []
    for line in in_file.readlines():
        split_line = line.split(" ")
        length = len(split_line)
        for i in range(length):
            words.append(split_line[i])
    return words


def get_random_word(words):
    random_number = randint(0, len(words) - 1)
    secret_word = words[random_number]
    return secret_word.rstrip()


def letter_in_secret_word(letter, secret_word):
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            return True
    return False


def already_guessed(letter, guesses):
    for i in range(len(guesses)):
        if letter == guesses[i]:
            return True
    guesses.append(letter)
    return False


def make_hidden_secret(secret_word, guesses):
    word = ""
    for i in range(0, len(secret_word)):
        for j in range(len(guesses)):
            if guesses[j] == secret_word[i]:
                word = word + guesses[j]
        if not len(word) == i + 1:
            word = word + "_"
    spaced_word = ""
    for i in range(len(word)):
        spaced_word = spaced_word + " " + word[i]
    return spaced_word.lstrip()


def won(guessed):
    for i in range(len(guessed)):
        if guessed[i] == '_' or '':
            return False
    return True


def play_graphics(secret_word):
    win = graphics.GraphWin("Hangman", 500, 500)
    win.setCoords(0, 0, 10, 10)
    line1 = graphics.Line(graphics.Point(0.75, 4), graphics.Point(2.75, 4))
    line2 = graphics.Line(graphics.Point(1.75, 4), graphics.Point(1.75, 8))
    line3 = graphics.Line(graphics.Point(1.75, 8), graphics.Point(3.25, 8))
    line4 = graphics.Line(graphics.Point(3.25, 8), graphics.Point(3.25, 7.5))
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    head = graphics.Circle(graphics.Point(3.25, 7.25), .25)
    body = graphics.Line(graphics.Point(3.25, 7), graphics.Point(3.25, 5.5))
    left_arm = graphics.Line(graphics.Point(3.25, 6.75), graphics.Point(2.75, 6.5))
    right_arm = graphics.Line(graphics.Point(3.25, 6.75), graphics.Point(3.75, 6.5))
    left_leg = graphics.Line(graphics.Point(3.25, 5.5), graphics.Point(2.75, 4.75))
    right_leg = graphics.Line(graphics.Point(3.25, 5.5), graphics.Point(3.75, 4.75))
    user_guesses_box = graphics.Entry(graphics.Point(7, 5), 5)
    user_guesses_box.draw(win)
    text_user_guess_box = graphics.Text(graphics.Point(7, 5.5), "Guess a letter and Click:")
    text_user_guess_box.draw(win)

    guessed_already = []
    guesses_remaining = 6
    hidden = make_hidden_secret(secret_word, guessed_already)
    guesses_remaining_text = graphics.Text(graphics.Point(7, 4.5),
                                           "guesses remaining: {}".format(guesses_remaining))
    guesses_remaining_text.draw(win)
    guessed_already_text = graphics.Text(graphics.Point(5, 3.5),
                                         "already guessed: {}".format(guessed_already))
    guessed_already_text.draw(win)
    secret_graphics = graphics.Text(graphics.Point(7, 6), "{}".format(hidden))
    secret_graphics.draw(win)
    win.getMouse()
    user_guess = user_guesses_box.getText()
    guessed_already.append(user_guess)
    guessed_already_text.setText("already guessed: {}".format(guessed_already))
    while not won(make_hidden_secret(secret_word, guessed_already)) and not guesses_remaining == 0:
        # (graphics.Text(graphics.Point(5, 5), "its working")).draw(win)
        if letter_in_secret_word(user_guess, secret_word):
            secret_graphics.setText("{}".format(make_hidden_secret(secret_word, guessed_already)))
        else:
            guesses_remaining = guesses_remaining - 1
            guesses_remaining_text.setText(guesses_remaining)
            if guesses_remaining == 5:
                head.draw(win)
            if guesses_remaining == 4:
                body.draw(win)
            if guesses_remaining == 3:
                left_arm.draw(win)
            if guesses_remaining == 2:
                right_arm.draw(win)
            if guesses_remaining == 1:
                left_leg.draw(win)
            if guesses_remaining == 0:
                right_leg.draw(win)
        win.getMouse()
        user_guess = user_guesses_box.getText()
        if not already_guessed(user_guess, guessed_already):
            guessed_already_text.setText("already guessed: {}".format(guessed_already))
    if won(make_hidden_secret(secret_word, guessed_already)):
        secret_graphics.setText(make_hidden_secret(secret_word, guessed_already))
        (graphics.Text(graphics.Point(5, 9), "Winner!")).draw(win)
        (graphics.Text(graphics.Point(5, 8.5), "The secret word was {}".format(secret_word))).draw(win)
    if guesses_remaining == 0:
        (graphics.Text(graphics.Point(5, 9), "Sorry you are out of guesses! You Lose!")).draw(win)
        (graphics.Text(graphics.Point(5, 8.5), "The secret word was {}".format(secret_word))).draw(win)
    (graphics.Text(graphics.Point(5, 8), "Click to Close")).draw(win)
    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guessed = []
    guesses_remaining = 6
    print("already guessed = ", guessed)
    print("guesses remaining = {}".format(guesses_remaining))
    print(make_hidden_secret(secret_word, guessed))
    user_input = input("guess a letter:")
    guessed.append(user_input.lower())
    while not won(make_hidden_secret(secret_word, guessed)) and guesses_remaining != 0:
        if letter_in_secret_word(user_input, secret_word):
            if not already_guessed(user_input, guessed):
                print(make_hidden_secret(secret_word, guessed))
        else:
            guesses_remaining = guesses_remaining - 1
        print("already guessed = ", guessed)
        print("guesses remaining", guesses_remaining)
        print(make_hidden_secret(secret_word, guessed))
        user_input = input("guess a letter:")
        if letter_in_secret_word(user_input, secret_word):
            already_guessed(user_input.lower(), guessed)

    if won(make_hidden_secret(secret_word, guessed)):
        print("winner")
        print(secret_word)
    elif guesses_remaining == 0:
        print("sorry you did not guess the word.")
        print("the secret word was {}".format(secret_word))


if __name__ == '__main__':
    game_word = get_random_word(get_words("words.txt"))
    # play_command_line(game_word)
    play_graphics(game_word)
