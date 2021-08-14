import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

time.sleep(0.1)
first_player = Paddle(350, 0)
second_player = Paddle(-350, 0)

ball = Ball()

screen.listen()
screen.onkey(first_player.up, "Up")
screen.onkey(first_player.down, "Down")
screen.onkey(second_player.up, "w")
screen.onkey(second_player.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    if ball.is_collision_with_wall():
        ball.bounce_from_wall()
    # if ball.distance(first_player) < 10 or ball.distance(second_player) < 10:
        # ball.bounce_from_paddle()
    if first_player.xcor() - ball.xcor() == 10 or second_player.xcor() - ball.xcor() == -10 :
        ball.bounce_from_paddle()
    screen.update()

screen.exitonclick()
