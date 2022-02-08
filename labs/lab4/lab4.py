import graphics
import time
"""

Ryan Campbell
lab4.py
Problem Description - To create an animated Valentine's day card using graphics functions and loops.  
Certificate of Authenticity - I, Ryan Campbell, certify that this lab is entirely my own work.

"""


def greeting_card():
    win = graphics.GraphWin("Greetings Card", 700, 700)
    win.setCoords(0, 0, 10, 10)
    greetings = graphics.Text(graphics.Point(5, 9), "Happy Valentine's Day!!!")
    greetings.setSize(36)
    background_ = graphics.Rectangle(graphics.Point(0, 0), graphics.Point(10, 10))
    background_.setFill("purple")
    circle_one = graphics.Circle((graphics.Point(4.5, 7)), .75)
    circle_two = graphics.Circle((graphics.Point(5.5, 7)), .75)
    greetings.setOutline("Pink")
    circle_one.setFill("red")
    circle_two.setFill("red")
    circle_one.setOutline("red")
    circle_two.setOutline("red")
    triangle_ = graphics.Polygon(graphics.Point(3.75, 6.825), graphics.Point(6.25, 6.825), graphics.Point(5, 4.6))
    triangle_.setFill("red")
    triangle_.setOutline("red")
    main_line = graphics.Polygon(graphics.Point(-4, 6.25), graphics.Point(-1, 6.25))
    head_of_arrow_top = graphics.Polygon(graphics.Point(-1.25, 6.5), graphics.Point(-1, 6.25))
    head_of_arrow_bottom = graphics.Polygon(graphics.Point(-1.25, 6), graphics.Point(-1, 6.25))
    tail_of_arrow_one = graphics.Polygon(graphics.Point(-4.2, 6.5), graphics.Point(-4, 6.25))
    tail_of_arrow_two = graphics.Polygon(graphics.Point(-4.2, 6), graphics.Point(-4, 6.25))
    tail_of_arrow_three = graphics.Polygon(graphics.Point(-4, 6.5), graphics.Point(-3.8, 6.25))
    tail_of_arrow_four = graphics.Polygon(graphics.Point(-4, 6), graphics.Point(-3.8, 6.25))
    tail_of_arrow_five = graphics.Polygon(graphics.Point(-3.8, 6.5), graphics.Point(-3.6, 6.25))
    tail_of_arrow_six = graphics.Polygon(graphics.Point(-3.8, 6), graphics.Point(-3.6, 6.25))
    background_.draw(win)
    greetings.draw(win)
    circle_one.draw(win)
    circle_two.draw(win)
    triangle_.draw(win)
    main_line.draw(win)
    head_of_arrow_top.draw(win)
    head_of_arrow_bottom.draw(win)
    tail_of_arrow_one.draw(win)
    tail_of_arrow_two.draw(win)
    tail_of_arrow_three.draw(win)
    tail_of_arrow_four.draw(win)
    tail_of_arrow_five.draw(win)
    tail_of_arrow_six.draw(win)
    for i in range(15):
        main_line.move(0.5, 0)
        head_of_arrow_bottom.move(0.5, 0)
        head_of_arrow_top.move(0.5, 0)
        tail_of_arrow_one.move(0.5, 0)
        tail_of_arrow_two.move(0.5, 0)
        tail_of_arrow_three.move(0.5, 0)
        tail_of_arrow_four.move(0.5, 0)
        tail_of_arrow_five.move(0.5, 0)
        tail_of_arrow_six.move(0.5, 0)
        time.sleep(.125)
    click_to_close_box = graphics.Rectangle(graphics.Point(4, 3), graphics.Point(6, 4))
    click_to_close = graphics.Text(graphics.Point(5, 3.5), "Click to Close")
    click_to_close.setOutline("pink")
    click_to_close_box.setFill("white")
    click_to_close_box.setOutline("white")
    click_to_close_box.draw(win)
    click_to_close.draw(win)
    win.getMouse()
    win.close()


