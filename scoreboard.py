from turtle import Turtle

ALIGNMENT_LIVES = "Left"
ALIGNMENT_SCORE = "Right"
FONT = ("Courier", 20, "normal")

ALIGNMENT_GAME_OVER = "Center"
FONT_GAME_OVER = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_lives()
        self.update_score()

    def update_lives(self):
        self.clear()
        self.goto(-380, 260)
        self.write(f"Lives: {self.lives}", align=ALIGNMENT_LIVES, font=FONT)

    def update_score(self):
        self.clear()
        self.goto(280, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT_SCORE, font=FONT)

    def game_over(self):
        self.goto(0, -20)
        self.write("GAME OVER", align=ALIGNMENT_GAME_OVER, font=FONT_GAME_OVER)

    def victory(self):
        self.goto(0, -20)
        self.write("YOU WIN!!!", align=ALIGNMENT_GAME_OVER, font=FONT_GAME_OVER)

    def reduce_lives(self):
        self.lives -= 1
        self.update_lives()

    def increase_score(self):
        self.score += 10
        self.update_score()
