from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("gray")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(380, 290)
        self.write(f'Lives:{self.lives}', align="center", font=FONT)

    def lives_left(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -10)
        self.write("GAME OVER", align="center", font=FONT)

    def game_win(self):
        self.goto(0, -10)
        self.write("YOU WON!", align="center", font=FONT)
