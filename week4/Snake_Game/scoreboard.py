from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0 # Starting score of 0
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 22, "normal"))
        
        

    def update_score(self):
        self.clear()
        self.score += 1 # Add one to score
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 22, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 22, "normal"))
