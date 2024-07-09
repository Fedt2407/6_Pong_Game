from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick, create_bricks
import time

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

s = Screen()
s.setup(800, 600)
s.bgcolor("black")
s.title("Breakout Game Remake") 
s.tracer(0)

p = Paddle(0, -260)

ball = Ball(p)
scoreboard = Scoreboard()
bricks = create_bricks()

s.listen()
s.onkey(ball.launch, "Up")
s.onkey(p.right, "Right")
s.onkey(p.left, "Left")

game_is_on = True

while game_is_on:
    s.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with roof
    if ball.ycor() > 275:
        ball.bounce_y()

    # Detect collision with walls
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(p) < 50 and ball.ycor() < -235:
        ball.bounce_y()

    # Detect collision with floor
    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.reduce_lives()
        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.bounce_y()
            brick.hit()
            bricks.remove(brick)
            scoreboard.increase_score()
            if len(bricks) == 0:
                game_is_on = False
                scoreboard.victory()
                break

# Prevents the window from closing immediately
s.exitonclick()