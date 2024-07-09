from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 6)
        self.goto(x, y)

    def left(self):
        new_x = self.xcor() - 40
        self.setx(new_x)
        if self.xcor() < -340:
            self.goto(-340, self.ycor())

    def right(self):
        new_x = self.xcor() + 40
        self.setx(new_x)
        if self.xcor() > 340:
            self.goto(340, self.ycor())
