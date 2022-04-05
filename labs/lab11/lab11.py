"""
Name: Ryan Campbell
lab10.py
Problem Description - to create a graphical three door game using classes previously
created.
I Ryan Campbell certify this assignment is entirely my own work.
"""
from door import Door
from button import Button
from random import randint
import graphics


def three_door_game():
    win = graphics.GraphWin("three door game", 500, 500)
    win.setCoords(0, 0, 10, 10)
    door_1_graphics = graphics.Rectangle(graphics.Point(1, 2), graphics.Point(3, 7))
    door_1_text = graphics.Text((door_1_graphics.getCenter()), "Door 1")
    door_1 = Door(door_1_graphics, door_1_text)
    door_1.close("brown", "Door 1")
    door_2_graphics = graphics.Rectangle(graphics.Point(4, 2), graphics.Point(6, 7))
    door_2_text = graphics.Text((door_2_graphics.getCenter()), "Door 2")
    door_2 = Door(door_2_graphics, door_2_text)
    door_2.close("brown", "Door 2")
    door_3_graphics = graphics.Rectangle(graphics.Point(7, 2), graphics.Point(9, 7))
    door_3_text = graphics.Text((door_3_graphics.getCenter()), "Door 2")
    door_3 = Door(door_3_graphics, door_3_text)
    door_3.close("brown", "Door 3")
    button_graphics = graphics.Rectangle(graphics.Point(7, 8), graphics.Point(9, 9))
    button_ = Button(button_graphics, "Quit")
    wins_box = graphics.Rectangle(graphics.Point(1, 8), graphics.Point(2, 9))
    losses_box = graphics.Rectangle(graphics.Point(2, 8), graphics.Point(3, 9))
    wins_text = graphics.Text(graphics.Point(1.5, 9.2), "wins")
    losses_text = graphics.Text(graphics.Point(2.5, 9.2), "losses")

    click_to_guess_text = graphics.Text(graphics.Point(5, 1), "Click to guess which is the secret door")
    i_have_secret_door_text = graphics.Text(graphics.Point(5, 8), "I have a secret door")
    you_win_text = graphics.Text(graphics.Point(5, 8), "you win!")
    incorrect_text = graphics.Text(graphics.Point(5, 8), "sorry, incorrect!")
    click_anywhere_play_again = graphics.Text(graphics.Point(5, 1), "click anywhere to play again")

    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)
    button_.draw_win(win)
    click_to_guess_text.draw(win)
    i_have_secret_door_text.draw(win)
    wins_box.draw(win)
    wins_text.draw(win)

    losses_box.draw(win)
    losses_text.draw(win)

    number_of_wins = graphics.Text((wins_box.getCenter()), 0)
    number_of_losses = graphics.Text((losses_box.getCenter()), 0)
    number_of_wins.draw(win)
    number_of_losses.draw(win)
    user_click = win.getMouse()
    wins = 0
    losses = 0
    while not button_.is_clicked(user_click):

        list_doors = [door_1, door_2, door_3]
        random_door = randint(0, 2)
        secret_door = list_doors[random_door]
        secret_door.set_secret("secret")

        if door_1.is_clicked(user_click):
            if door_1.secret:
                door_1.color_door("green")
                wins = wins + 1
                number_of_wins.setText(wins)
                i_have_secret_door_text.undraw()
                you_win_text.draw(win)
            else:
                door_1.color_door("red")
                secret_door.color_door("green")
                losses = losses + 1
                number_of_losses.setText(losses)
                i_have_secret_door_text.undraw()
                incorrect_text.draw(win)
        elif door_2.is_clicked(user_click):
            if door_2.secret:
                door_2.color_door("green")
                wins = wins + 1
                number_of_wins.setText(wins)
                i_have_secret_door_text.undraw()
                you_win_text.draw(win)
            else:
                door_2.color_door("red")
                secret_door.color_door("green")
                losses = losses + 1
                number_of_losses.setText(losses)
                i_have_secret_door_text.undraw()
                incorrect_text.draw(win)
        elif door_3.is_clicked(user_click):
            if door_3.secret:
                door_3.color_door("green")
                wins = wins + 1
                number_of_wins.setText(wins)
                i_have_secret_door_text.undraw()
                you_win_text.draw(win)

            else:
                door_3.color_door("red")
                secret_door.color_door("green")
                losses = losses + 1
                number_of_losses.setText(losses)
                i_have_secret_door_text.undraw()
                incorrect_text.draw(win)
        else:
            i_have_secret_door_text.undraw()

        click_to_guess_text.undraw()
        click_anywhere_play_again.draw(win)
        user_click = win.getMouse()
        if button_.is_clicked(user_click):
            win.close()
        elif user_click:
            door_1.color_door("brown")
            door_2.color_door("brown")
            door_3.color_door("brown")
            secret_door.set_secret(False)
            you_win_text.undraw()
            incorrect_text.undraw()
            i_have_secret_door_text.draw(win)
            click_anywhere_play_again.undraw()
            click_to_guess_text.draw(win)
            user_click = win.getMouse()

    win.close()













