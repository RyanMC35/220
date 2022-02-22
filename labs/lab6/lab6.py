"""
Ryan Campbell
lab6.py
Problem Description - To take a user input message and key and create an output encoded message.
Certificate of Authenticity - I, Ryan Campbell, certify that this lab is entirely my own work.


"""
import graphics


def vigenere():
    win = graphics.GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)
    box = graphics.Rectangle(graphics.Point(4, 5.5), graphics.Point(6, 4.5))
    text_box = graphics.Text(graphics.Point(5, 5), "Encode")
    text_message = graphics.Text(graphics.Point(2, 8), "Message to Code")
    text_password = graphics.Text(graphics.Point(2.5, 7), "Enter Password")
    message_box = graphics.Entry(graphics.Point(6.5, 8), 30)
    password_box = graphics.Entry(graphics.Point(6, 7), 20)
    box.draw(win)
    text_box.draw(win)
    text_message.draw(win)
    text_password.draw(win)
    message_box.draw(win)
    password_box.draw(win)
    win.getMouse()
    box.undraw()
    text_box.undraw()
    message_var = message_box.getText()
    message_edited = (message_var.replace(" ", "")).upper()
    length_of_message = len(message_edited)
    password_var = password_box.getText()
    password_edited = (password_var.replace(" ", "")).upper()
    length_of_password = len(password_var)
    encoded_message = ""
    for i in range(length_of_message):
        letter_ = message_edited[i]
        password_number = i % length_of_password
        password_letter = password_edited[password_number]
        letter_encoded_ = ord(letter_) - 65
        password_letter_encoded = ord(password_letter) - 65
        encoded_moved = ((letter_encoded_ + password_letter_encoded) % 26) + 65
        encoded_message = encoded_message + chr(encoded_moved)
    resulting_message = graphics.Text(graphics.Point(5, 5), "Resulting Message")
    resulting_message.draw(win)
    text_encoded_message = graphics.Text(graphics.Point(5, 4.5), encoded_message.upper())
    text_encoded_message.draw(win)
    click_to_close_message = graphics.Text(graphics.Point(5, 1.5), "Click Anywhere to Close Window")
    click_to_close_message.draw(win)
    win.getMouse()
    win.close()
