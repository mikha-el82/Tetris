from turtle import Turtle


MOVE_DISTANCE = 20
DOWN = 270
START_POS_LONGBRICK = [(0, 0), (20, 0), (40, 0), (60, 0)]
START_POS_SQUAREBRICK = [(0, 0), (0, 20), (20, 0), (20, 20)]
START_POS_TEEBRICK = [(0, 0), (20, 0), (40, 0), (20, 20)]
START_POS_ZETBRICK = [(0, 0), (0, 20), (20, 20), (20, 40)]
START_POS_ELBRICK = [(0, 0), (20, 0), (40, 0), (40, 20)]
BRICK_DEFINITION = {
    "long": START_POS_LONGBRICK,
    "square": START_POS_SQUAREBRICK,
    "tee": START_POS_TEEBRICK,
    "zet": START_POS_ZETBRICK,
    "el": START_POS_ELBRICK,
}


class Brick:
    def __init__(self, type_of_brick):
        self.brick_segments = []
        self.type_of_brick = type_of_brick  # if it is used in functions
        self.create_brick(type_of_brick)

    def create_brick(self, type_of_brick):
        for position in BRICK_DEFINITION[type_of_brick]:
            new_segment = Turtle(shape="square")
            new_segment.color("black")
            new_segment.penup()
            new_segment.goto(position)
            self.brick_segments.append(new_segment)

    def move_left(self):
        self.move_brick(180)
        print("to the left")

    def move_right(self):
        self.move_brick(0)
        print("to the right")

    def move_brick(self, direction):
        for segment in self.brick_segments:
            segment.setheading(direction)
            segment.forward(MOVE_DISTANCE)
