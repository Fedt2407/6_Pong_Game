from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x, y)

    def hit(self):
        self.goto(1000, 1000)  # Move the brick off-screen
        self.hideturtle()


# Function to create bricks at the beginning of the game
def create_bricks():
    colors = ["red", "orange", "yellow", "green", "blue"]
    bricks = []
    y_start = 200  # Starting y-coordinate for the top row
    for i in range(5):
        y = y_start - i * 25  
        for j in range(-365, 400, 45):  #
            brick = Brick(j, y, colors[i])
            bricks.append(brick)
    return bricks