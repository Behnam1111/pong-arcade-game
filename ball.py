from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, position):
        new_x = self.xcor() + position
        new_y = self.ycor() + position
        self.goto(new_x, new_y)
