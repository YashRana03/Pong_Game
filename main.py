from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


# Setting up the window
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# Calling different classes to create the objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

# Links the keyboard keys to the appropriate functions
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.sleep)
    screen.update()
    ball.move()

    # Checks to see if the ball is near the edge of the screen, if so it makes the ball bounce back
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # Checks to see if the ball is close to the right paddle, if so the ball bounces back
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.r_paddle_bounce()
        ball.increase_speed()

    # Checks to see if the ball is close to the left paddle, if so the ball bounces back
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.l_paddle_bounce()
        ball.increase_speed()

    # Checks to see if the ball has gone beyond the right paddle, if so updates the score and resets the ball position
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    # Checks to see if the ball has gone beyond the left paddle, if so updates the score and resets the ball position
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()

    screen.update()

screen.exitonclick()

