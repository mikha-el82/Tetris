from turtle import Turtle

def set_board(SCREEN_WIDTH, SCREEN_HEIGHT):
    timmy = Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    timmy.pendown()
    timmy.right(90)
    timmy.forward(SCREEN_HEIGHT)
    timmy.right(90)
    timmy.forward(SCREEN_WIDTH)
    timmy.right(90)
    timmy.forward(SCREEN_HEIGHT)
    timmy.right(90)
    timmy.forward(SCREEN_WIDTH)
