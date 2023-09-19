from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=650)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle((0, -300))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle.go_left, key="Left")
screen.onkey(fun=paddle.go_right, key="Right")


bricks = []
for i in range(5):
    for j in range(7):
        brick = Brick(x=-362 + (j * 120), y=250 - (i * 50))
        bricks.append(brick)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if len(bricks) == 0:
        game_is_on = False
        scoreboard.game_win()

    for brick in bricks:
        if ball.distance(brick) < 54:
            bricks.remove(brick)
            brick.hideturtle()
            ball.bounce_y()

    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() > 420 or ball.xcor() < -420:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 80 and ball.ycor() < -275:
        ball.bounce_y()

#     Detect when paddle misses the ball
    if ball.ycor() < -315:
        ball.reset_position()
        scoreboard.lives_left()
        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
