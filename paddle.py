from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.05, stretch_len=8, outline=15)
        self.color("#FFFF00")
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 28
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 28
        self.goto(new_x, self.ycor())


