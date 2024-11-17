FONT = ("Courier", 24, "bold")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! ", align="center", font=FONT)
        self.goto(0, -35)
        self.write(f"You reached level:{self.level}", align="center", font=FONT)