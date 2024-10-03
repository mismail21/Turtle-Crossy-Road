from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.refresh_turtle()
        self.setheading(90)

    def move_upwards(self):
        self.forward(MOVE_DISTANCE)

    def refresh_turtle(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
