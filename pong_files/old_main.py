from turtle import Screen
from old_paddle import Paddle
from old_ball import Ball
from old_scoreboard import Scoreboard
import time

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

s = Screen()
s.setup(800, 600)
s.bgcolor("black")
s.title("Breakout Game Remake") 
s.tracer(0)

p1 = Paddle(-350, 0)
p2 = Paddle(350, 0)

ball = Ball()

s.listen()
s.onkey(p1.up, "w")
s.onkey(p1.down, "s")
s.onkey(p2.up, "Up")
s.onkey(p2.down, "Down")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collision with left paddle
    if ball.distance(p2) < 50 and ball.xcor() > 320 or ball.distance(p1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Keep track of scores
    if ball.xcor() > 400:
        scoreboard.increase_l_score()
        ball.reset_position()
    elif ball.xcor() < -400:
        scoreboard.increase_r_score()
        ball.reset_position()

    # End the game
    if scoreboard.r_score == 3 or scoreboard.l_score == 3:
        scoreboard.game_over()
        game_is_on = False


s.exitonclick()
