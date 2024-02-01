from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PyBall Odyssey")
screen.tracer(0)

# Paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Ball
ball = Ball()

# Scoreboard
score = Scoreboard()

# Game rendering on screen
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    # Detect when left_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()





screen.exitonclick()

