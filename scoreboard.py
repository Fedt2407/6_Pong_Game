from turtle import Turtle

ALIGNMENT_LIVES = "Left"
FONT_LIVES = ("Courier", 20, "normal")

ALIGNMENT_GAME_OVER = "Center"
FONT_GAME_OVER = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-380, 260)
        self.write(f"Lives: {self.lives}", align=ALIGNMENT_LIVES, font=FONT_LIVES)

    def game_over(self):
        self.goto(0, -20)
        self.write("GAME OVER", align=ALIGNMENT_GAME_OVER, font=FONT_GAME_OVER)

    def victory(self):
        self.goto(0, -20)
        self.write("YOU WIN!!!", align=ALIGNMENT_GAME_OVER, font=FONT_GAME_OVER)

    def reduce_lives(self):
        self.lives -= 1
        self.update_scoreboard()
