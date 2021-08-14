from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.first_player_score = 0
        self.second_player_score = 0
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.second_player_score}", False, "center", ("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(f"{self.first_player_score}", False, "center", ("Courier", 60, "normal"))

    def first_player_raise_score(self):
        self.first_player_score += 1
        self.update_scoreboard()

    def second_player_raise_score(self):
        self.second_player_score += 1
        self.update_scoreboard()
