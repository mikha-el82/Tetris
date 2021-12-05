from turtle import Turtle
# TODO

def set_board(screen_width, screen_height):
    timmy = Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(screen_width / 2, screen_height / 2)
    timmy.pendown()
    timmy.right(90)
    timmy.forward(screen_height)
    timmy.right(90)
    timmy.forward(screen_width)
    timmy.right(90)
    timmy.forward(screen_height)
    timmy.right(90)
    timmy.forward(screen_width)
