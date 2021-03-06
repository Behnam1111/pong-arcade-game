import time
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)

    def restart(self, x_pos, y_pos):
        self.goto(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
