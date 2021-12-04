from turtle import Screen, Turtle
from shapes import Brick
from board import set_board
import time

SCREEN_WIDTH = 220
SCREEN_HEIGHT = 420


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# screen.bgcolor("green")
screen.title("Tetris")
screen.tracer(0)  # sets turtle animation off

set_board(SCREEN_WIDTH, SCREEN_HEIGHT)

#
# brick = Brick("square")
# brick = Brick("long")
# brick = Brick("tee")
# brick = Brick("zet")
brick = Brick("el")


screen.listen()
screen.onkey(brick.move_left, "Left")
screen.onkey(brick.move_right, "Right")


while True:
    screen.update()
    time.sleep(0.3)

#
# bottom = False
# while not bottom:
#     brick.move_brick(DOWN)
#     screen.update()
#     time.sleep(0.3)


screen.exitonclick()
