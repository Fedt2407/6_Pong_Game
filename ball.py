from turtle import Turtle


class Ball(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.shape("circle")
        self.color("#FEE300")
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1
        self.is_launched = False
        self.paddle = paddle
        self.follow_paddle()


    def move(self):
        if self.is_launched:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        else:
            self.follow_paddle()


    def follow_paddle(self):
        self.goto(self.paddle.xcor(), self.paddle.ycor() + 20)


    def launch(self):
        self.is_launched = True


    def bounce_y(self):
        self.y_move *= - 1


    def bounce_x(self):
        self.x_move *= - 1


    def reset_position(self):
        self.home()
        self.bounce_x()
        self.is_launched = False